import os, time, threading, json, hashlib
from typing import Any, Optional, Dict

try:
    import redis
except ImportError:
    redis = None

class TTLCache:
    def __init__(self, default_ttl: int = 300):
        self.default_ttl = default_ttl
        self.lock = threading.Lock()
        self.store: Dict[str, tuple[float, Any]] = {}
        
        # Initialize Redis if available
        redis_url = os.getenv("REDIS_URL")
        if redis_url and redis:
            try:
                self.client = redis.StrictRedis.from_url(redis_url, decode_responses=True)
                self.client.ping()
                print("Successfully connected to Redis.")
            except Exception as e:
                print(f"Could not connect to Redis: {e}. Falling back to in-memory cache.")
                self.client = None
        else:
            print("Redis URL not found. Falling back to in-memory cache.")
            self.client = None

    def _serialize(self, value: Any) -> str:
        return json.dumps(value, default=str)

    def _deserialize(self, value: str) -> Any:
        try:
            return json.loads(value)
        except (json.JSONDecodeError, TypeError):
            return value

    def get(self, key: str) -> Optional[Any]:
        if self.client:
            val = self.client.get(key)
            return self._deserialize(val) if val else None
            
        with self.lock:
            if key not in self.store:
                return None
            expires_at, value = self.store[key]
            if time.time() > expires_at:
                del self.store[key]
                return None
            return value

    def set(self, key: str, value: Any, ttl: Optional[int] = None):
        ttl = ttl or self.default_ttl
        
        if self.client:
            self.client.setex(key, ttl, self._serialize(value))
            return
            
        with self.lock:
            expires_at = time.time() + ttl
            self.store[key] = (expires_at, value)

# Create a global cache instance
cache = TTLCache(default_ttl=600)

def make_key(prefix: str, *args, **kwargs) -> str:
    payload = {"args": args, "kwargs": kwargs}
    serialized = json.dumps(payload, default=str, sort_keys=True)
    h = hashlib.sha256(serialized.encode()).hexdigest()
    return f"{prefix}:{h}"