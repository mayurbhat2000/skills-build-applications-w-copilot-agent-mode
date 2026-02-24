from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name='Test User', email='test@example.com', team='Marvel')
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.team, 'Marvel')

class TeamModelTest(TestCase):
    def test_create_team(self):
        user = User.objects.create(name='Test User', email='test@example.com', team='Marvel')
        team = Team.objects.create(name='Marvel')
        team.members.set([user])
        self.assertEqual(team.name, 'Marvel')
        self.assertEqual(list(team.members.all())[0].email, 'test@example.com')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(name='Test User', email='test@example.com', team='Marvel')
        activity = Activity.objects.create(user=user, activity='Running', duration=30)
        self.assertEqual(activity.activity, 'Running')
        self.assertEqual(activity.duration, 30)

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(team='Marvel', points=100)
        self.assertEqual(leaderboard.team, 'Marvel')
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = User.objects.create(name='Test User', email='test@example.com', team='Marvel')
        workout = Workout.objects.create(user=user, workout='Yoga', duration=60)
        self.assertEqual(workout.workout, 'Yoga')
        self.assertEqual(workout.duration, 60)
