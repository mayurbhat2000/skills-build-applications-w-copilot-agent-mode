
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Sample users
        marvel_users = [
            User(name='Iron Man', email='ironman@marvel.com', team='Marvel'),
            User(name='Captain America', email='cap@marvel.com', team='Marvel'),
            User(name='Thor', email='thor@marvel.com', team='Marvel'),
        ]
        dc_users = [
            User(name='Superman', email='superman@dc.com', team='DC'),
            User(name='Batman', email='batman@dc.com', team='DC'),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team='DC'),
        ]
        for user in marvel_users + dc_users:
            user.save()

        # Sample teams
        marvel_team = Team(name='Marvel')
        marvel_team.save()
        marvel_team.members.set([u for u in marvel_users])
        dc_team = Team(name='DC')
        dc_team.save()
        dc_team.members.set([u for u in dc_users])

        # Sample activities
        Activity.objects.create(user=marvel_users[0], activity='Running', duration=30)
        Activity.objects.create(user=dc_users[1], activity='Cycling', duration=45)

        # Sample leaderboard
        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=90)

        # Sample workouts
        Workout.objects.create(user=marvel_users[2], workout='Weightlifting', reps=50)
        Workout.objects.create(user=dc_users[2], workout='Yoga', duration=60)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
