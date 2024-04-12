from views.Router import Router, DataStrategyEnum
from views.index_view import IndexView
from views.profile_view import ProfileView
from views.settings_view import SettingsView

router = Router(DataStrategyEnum.QUERY)

router.routes = {
  "/": IndexView,
  "/profile": ProfileView,
  "/settings": SettingsView,
}