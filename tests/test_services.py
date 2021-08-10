from profil3r.app import Core
import os
import pytest

CONFIG = '{}/../profil3r/config/config.json'.format(os.path.dirname(os.path.realpath(__file__)))
profil3r = Core(CONFIG)
profil3r.load_config()

# aboutme
def test_aboutme_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['aboutme']['enabled'] == 'yes':
        assert len(profil3r.aboutme()['accounts']) == 1

def test_aboutme_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['aboutme']['enabled'] == 'yes': 
        len(profil3r.aboutme()['accounts']) == 0

# asciinema
def test_asciinema_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['asciinema']['enabled'] == 'yes':
        assert len(profil3r.asciinema()['accounts']) == 1

def test_asciinema_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['asciinema']['enabled'] == 'yes':
        assert len(profil3r.asciinema()['accounts']) == 0

# bandcamp
def test_bandcamp_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['bandcamp']['enabled'] == 'yes':
        assert len(profil3r.bandcamp()['accounts']) == 1

def test_bandcamp_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['bandcamp']['enabled'] == 'yes':
        assert len(profil3r.bandcamp()['accounts']) == 0

# buymeacoffee
def test_buymeacoffee_valid():
    profil3r.permutations_list = ['givocefo']
    profil3r.separators = []
    if profil3r.config['plateform']['buymeacoffee']['enabled'] == 'yes':
        assert len(profil3r.buymeacoffee()['accounts']) == 1

def test_buymeacoffee_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['buymeacoffee']['enabled'] == 'yes':
        assert len(profil3r.buymeacoffee()['accounts']) == 0

# cashapp
def test_cashapp_valid():
    profil3r.permutations_list = ['john']
    profil3r.separators = []
    if profil3r.config['plateform']['cashapp']['enabled'] == 'yes':
        assert len(profil3r.cashapp()['accounts']) == 1

def test_cashapp_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['cashapp']['enabled'] == 'yes':
        assert len(profil3r.cashapp()['accounts']) == 0

# codementor 
def test_codementor_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['crackedto']['enabled'] == 'yes':
        assert len(profil3r.crackedto()['accounts']) == 1

def test_codementor_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['crackedto']['enabled'] == 'yes':
        assert len(profil3r.crackedto()['accounts']) == 0

# crackedto
def test_crackedto_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['crackedto']['enabled'] == 'yes':
        assert len(profil3r.crackedto()['accounts']) == 1

def test_crackedto_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['crackedto']['enabled'] == 'yes':
        assert len(profil3r.crackedto()['accounts']) == 0

# dailymotion
def test_dailymotion_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['dailymotion']['enabled'] == 'yes':
        assert len(profil3r.dailymotion()['accounts']) == 1

def test_dailymotion_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['dailymotion']['enabled'] == 'yes':
        assert len(profil3r.dailymotion()['accounts']) == 0

# deviantart
def test_deviantart_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['deviantart']['enabled'] == 'yes':
        assert len(profil3r.deviantart()['accounts']) == 1

def test_deviantart_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['deviantart']['enabled'] == 'yes':
        assert len(profil3r.deviantart()['accounts']) == 0

# devto
def test_devto_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['devto']['enabled'] == 'yes':
        assert len(profil3r.devto()['accounts']) == 1

def test_devto_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['devto']['enabled'] == 'yes':
        assert len(profil3r.devto()['accounts']) == 0

# domain
def test_domain_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['domain']['enabled'] == 'yes':
        assert len(profil3r.domain()['accounts']) == 1

def test_domain_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['domain']['enabled'] == 'yes':
        assert len(profil3r.domain()['accounts']) == 0

# ello
def test_ello_valid():
    profil3r.permutations_list = ['john']
    profil3r.separators = []
    if profil3r.config['plateform']['ello']['enabled'] == 'yes':
        assert len(profil3r.ello()['accounts']) == 1

def test_ello_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['ello']['enabled'] == 'yes':
        assert len(profil3r.ello()['accounts']) == 0

# email
def test_email_valid():
    profil3r.permutations_list = ['john']
    profil3r.separators = []
    if profil3r.config['plateform']['email']['enabled'] == 'yes':
        assert all([email['breached'] for email in profil3r.email()['accounts']])

def test_email_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['email']['enabled'] == 'yes':
        assert not any([email['breached'] for email in profil3r.email()['accounts']])

# facebook
def test_facebook_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['facebook']['enabled'] == 'yes':
        assert len(profil3r.facebook()['accounts']) == 1

def test_facebook_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['facebook']['enabled'] == 'yes':
        assert len(profil3r.facebook()['accounts']) == 0

# flickr
def test_flickr_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['flickr']['enabled'] == 'yes':
        assert len(profil3r.flickr()['accounts']) == 1

def test_flickr_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['flickr']['enabled'] == 'yes':
        assert len(profil3r.flickr()['accounts']) == 0

# github
def test_github_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['github']['enabled'] == 'yes':
        assert len(profil3r.github()['accounts']) == 1

def test_github_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['github']['enabled'] == 'yes':
        assert len(profil3r.github()['accounts']) == 0

# goodread
def test_goodread_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['goodread']['enabled'] == 'yes':
        assert len(profil3r.goodread()['accounts']) == 1

def test_goodread_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['goodread']['enabled'] == 'yes':
        assert len(profil3r.goodread()['accounts']) == 0

# hackernews
def test_hackernews_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['hackernews']['enabled'] == 'yes':
        assert len(profil3r.hackernews()['accounts']) == 1

def test_hackernews_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['hackernews']['enabled'] == 'yes':
        assert len(profil3r.hackernews()['accounts']) == 0

# instagram
def test_instagram_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['instagram']['enabled'] == 'yes':
        assert len(profil3r.instagram()['accounts']) == 1

def test_instagram_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['instagram']['enabled'] == 'yes':
        assert len(profil3r.instagram()['accounts']) == 0

# instructables
def test_instructables_valid():
    profil3r.permutations_list = ['john']
    profil3r.separators = []
    if profil3r.config['plateform']['instructables']['enabled'] == 'yes':
        assert len(profil3r.instructables()['accounts']) == 1

def test_instructables_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['instructables']['enabled'] == 'yes':
        assert len(profil3r.instructables()['accounts']) == 0

# jeuxvideo
def test_jeuxvideo_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['jeuxvideo']['enabled'] == 'yes':
        assert len(profil3r.jeuxvideo()['accounts']) == 1

def test_jeuxvideo_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['jeuxvideo']['enabled'] == 'yes':
        assert len(profil3r.jeuxvideo()['accounts']) == 0

# lesswrong
def test_lesswrong_valid():
    profil3r.permutations_list = ['john']
    profil3r.separators = []
    if profil3r.config['plateform']['lesswrong']['enabled'] == 'yes':
        assert len(profil3r.lesswrong()['accounts']) == 1

def test_lesswrong_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['lesswrong']['enabled'] == 'yes':
        assert len(profil3r.lesswrong()['accounts']) == 0

# linktree
def test_linktree_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['linktree']['enabled'] == 'yes':
        assert len(profil3r.linktree()['accounts']) == 1

def test_linktree_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['linktree']['enabled'] == 'yes':
        assert len(profil3r.linktree()['accounts']) == 0

# medium
def test_medium_valid():
    profil3r.permutations_list = ['cryptohayes']
    profil3r.separators = []
    if profil3r.config['plateform']['medium']['enabled'] == 'yes':
        assert len(profil3r.medium()['accounts']) == 1

def test_medium_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['medium']['enabled'] == 'yes':
        assert len(profil3r.medium()['accounts']) == 0

# myspace
def test_myspace_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['myspace']['enabled'] == 'yes':
        assert len(profil3r.myspace()['accounts']) == 1

def test_myspace_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['myspace']['enabled'] == 'yes':
        assert len(profil3r.myspace()['accounts']) == 0

# npm
def test_npm_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['npm']['enabled'] == 'yes':
        assert len(profil3r.npm()['accounts']) == 1


def test_npm_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['npm']['enabled'] == 'yes':
        assert len(profil3r.npm()['accounts']) == 0

# pastebin
def test_pastebin_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['pastebin']['enabled'] == 'yes':
        assert len(profil3r.pastebin()['accounts']) == 1

def test_pastebin_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['pastebin']['enabled'] == 'yes':
        assert len(profil3r.pastebin()['accounts']) == 0

# patreon
def test_patreon_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['patreon']['enabled'] == 'yes':
        assert len(profil3r.patreon()['accounts']) == 1

def test_patreon_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['patreon']['enabled'] == 'yes':
        assert len(profil3r.patreon()['accounts']) == 0

# pinterest
def test_pinterest_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['pinterest']['enabled'] == 'yes':
        assert len(profil3r.pinterest()['accounts']) == 1

def test_pinterest_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['pinterest']['enabled'] == 'yes':
        assert len(profil3r.pinterest()['accounts']) == 0

# pornhub
def test_pornhub_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['pornhub']['enabled'] == 'yes':
        assert len(profil3r.pornhub()['accounts']) == 1

def test_pornhub_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['pornhub']['enabled'] == 'yes':
        assert len(profil3r.pornhub()['accounts']) == 0

# pypi
def test_pypi_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['pypi']['enabled'] == 'yes':
        assert len(profil3r.pypi()['accounts']) == 1

def test_pypi_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['pypi']['enabled'] == 'yes':
        assert len(profil3r.pypi()['accounts']) == 0

# redtube
def test_redtube_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['redtube']['enabled'] == 'yes':
        assert len(profil3r.redtube()['accounts']) == 1

def test_redtube_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['redtube']['enabled'] == 'yes':
        assert len(profil3r.redtube()['accounts']) == 0

# replit
def test_replit_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['replit']['enabled'] == 'yes':
        assert len(profil3r.replit()['accounts']) == 1

def test_replit_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['replit']['enabled'] == 'yes':
        assert len(profil3r.replit()['accounts']) == 0

# rootme
def test_rootme_valid():
    profil3r.permutations_list = ['john']
    profil3r.separators = []
    if profil3r.config['plateform']['rootme']['enabled'] == 'yes':
        assert len(profil3r.rootme()['accounts']) == 1

def test_rootme_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['rootme']['enabled'] == 'yes':
        assert len(profil3r.rootme()['accounts']) == 0

# skype
def test_skype_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['skype']['enabled'] == 'yes':
        assert len(profil3r.skype()['accounts']) == 1

def test_skype_invalid():
    profil3r.permutations_list = ['1111aaaa2222bbbb3333cccc4444']
    profil3r.separators = []
    if profil3r.config['plateform']['skype']['enabled'] == 'yes':
        assert len(profil3r.skype()['accounts']) == 0

# slideshare
def test_slideshare_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['slideshare']['enabled'] == 'yes':
        assert len(profil3r.slideshare()['accounts']) == 1

def test_slideshare_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['slideshare']['enabled'] == 'yes':
        assert len(profil3r.slideshare()['accounts']) == 0

# smule
def test_smule_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['smule']['enabled'] == 'yes':
        assert len(profil3r.smule()['accounts']) == 1

def test_smule_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['smule']['enabled'] == 'yes':
        assert len(profil3r.smule()['accounts']) == 0

# soundcloud
def test_soundcloud_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['soundcloud']['enabled'] == 'yes':
        assert len(profil3r.soundcloud()['accounts']) == 1

def test_soundcloud_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['soundcloud']['enabled'] == 'yes':
        assert len(profil3r.soundcloud()['accounts']) == 0

# spotify
def test_spotify_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['spotify']['enabled'] == 'yes':
        assert len(profil3r.spotify()['accounts']) == 1

def test_spotify_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['spotify']['enabled'] == 'yes':
        assert len(profil3r.spotify()['accounts']) == 0

# steam
def test_steam_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['steam']['enabled'] == 'yes':
        assert len(profil3r.steam()['accounts']) == 1

def test_steam_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['steam']['enabled'] == 'yes':
        assert len(profil3r.steam()['accounts']) == 0

# tiktok
def test_tiktok_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['tiktok']['enabled'] == 'yes':
        assert len(profil3r.tiktok()['accounts']) == 1

def test_tiktok_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['tiktok']['enabled'] == 'yes':
        assert len(profil3r.tiktok()['accounts']) == 0

# tripadvisor
def test_tripadvisor_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['tripadvisor']['enabled'] == 'yes':
        assert len(profil3r.tripadvisor()['accounts']) == 1

def test_tripadvisor_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['tripadvisor']['enabled'] == 'yes':
        assert len(profil3r.tripadvisor()['accounts']) == 0

# twitter
def test_twitter_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['twitter']['enabled'] == 'yes':
        assert len(profil3r.twitter()['accounts']) == 1

def test_twitter_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['twitter']['enabled'] == 'yes':
        assert len(profil3r.twitter()['accounts']) == 0

# vimeo
def test_vimeo_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['vimeo']['enabled'] == 'yes':
        assert len(profil3r.vimeo()['accounts']) == 1

def test_vimeo_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['vimeo']['enabled'] == 'yes':
        assert len(profil3r.vimeo()['accounts']) == 0

# wikipedia
def test_wikipedia_valid():
    profil3r.permutations_list = ['john']
    profil3r.separators = []
    if profil3r.config['plateform']['wikipedia']['enabled'] == 'yes':
        assert len(profil3r.wikipedia()['accounts']) == 1

def test_wikipedia_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['wikipedia']['enabled'] == 'yes':
        assert len(profil3r.wikipedia()['accounts']) == 0

# wordpress
def test_wordpress_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['wordpress']['enabled'] == 'yes':
        assert len(profil3r.wordpress()['accounts']) == 1

def test_wordpress_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['wordpress']['enabled'] == 'yes':
        assert len(profil3r.wordpress()['accounts']) == 0

# xvideos
def test_xvideos_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['xvideos']['enabled'] == 'yes':
        assert len(profil3r.xvideos()['accounts']) == 1

def test_xvideos_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['xvideos']['enabled'] == 'yes':
        assert len(profil3r.xvideos()['accounts']) == 0

# zeroxzerozerosec
def test_zeroxzerozerosec_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['zeroxzerozerosec']['enabled'] == 'yes':
        assert len(profil3r.zeroxzerozerosec()['accounts']) == 1

def test_zeroxzerozerosec_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['zeroxzerozerosec']['enabled'] == 'yes':
        assert len(profil3r.zeroxzerozerosec()['accounts']) == 0  

# Leagueoflegends
def test_leagueoflegends_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['leagueoflegends']['enabled'] == 'yes' and len(profil3r.config['plateform']['leagueoflegends']['servers']) >= 1:
        assert len(profil3r.leagueoflegends()['accounts']) >= 1

def test_leagueoflegends_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['leagueoflegends']['enabled'] == 'yes' and len(profil3r.config['plateform']['leagueoflegends']['servers']) >= 1:
        assert len(profil3r.leagueoflegends()['accounts']) == 0

# chirpty
def test_chirpty_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['chirpty']['enabled'] == 'yes':
        assert len(profil3r.chirpty()['accounts']) >= 1
        
def test_chirpty_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['chirpty']['enabled'] == 'yes':
        assert len(profil3r.chirpty()['accounts']) == 0

# hubpages
def test_hubpages_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['hubpages']['enabled'] == 'yes':
        assert len(profil3r.chirpty()['accounts']) >= 1
        
def test_hubpages_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['hubpages']['enabled'] == 'yes':
        assert len(profil3r.chirpty()['accounts']) == 0
        
# dota2
def test_dota2_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['dota2']['enabled'] == 'yes':
        assert len(profil3r.dota2()['accounts']) >= 1
        
def test_dota2_invalid():
    profil3r.permutations_list = ['d']
    profil3r.separators = []
    if profil3r.config['plateform']['dota2']['enabled'] == 'yes':
        assert len(profil3r.dota2()['accounts']) == 0

# keybase
def test_keybase_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['keybase']['enabled'] == 'yes':
        assert len(profil3r.keybase()['accounts']) >= 1
        
def test_keybase_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['keybase']['enabled'] == 'yes':
        assert len(profil3r.keybase()['accounts']) == 0

# dribbble
def test_dribbble_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['dribbble']['enabled'] == 'yes':
        assert len(profil3r.dribbble()['accounts']) >= 1
        
def test_dribbble_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['dribbble']['enabled'] == 'yes':
        assert len(profil3r.dribbble()['accounts']) == 0

# kongregate
def test_kongregate_valid():
    profil3r.permutations_list = ['johndoe']
    profil3r.separators = []
    if profil3r.config['plateform']['kongregate']['enabled'] == 'yes':
        assert len(profil3r.kongregate()['accounts']) >= 1
        
def test_kongregate_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['kongregate']['enabled'] == 'yes':
        assert len(profil3r.kongregate()['accounts']) == 0

# livejournal
def test_livejournal_valid():
    profil3r.permutations_list = ['john']
    profil3r.separators = []
    if profil3r.config['plateform']['livejournal']['enabled'] == 'yes':
        assert len(profil3r.livejournal()['accounts']) >= 1
        
def test_livejournal_invalid():
    profil3r.permutations_list = ['Th1s1sN0t4V4l1d4cc0unt123']
    profil3r.separators = []
    if profil3r.config['plateform']['livejournal']['enabled'] == 'yes':
        assert len(profil3r.livejournal()['accounts']) == 0