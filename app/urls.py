from rest_framework.routers import SimpleRouter,DefaultRouter           #(default router is child of simple router)
from .views import *
router = SimpleRouter()

router.register('Artist',ArtistAPI)
router.register('Song',SongAPI)
router.register('Album',AlbumAPI)

urlpatterns = router.urls


