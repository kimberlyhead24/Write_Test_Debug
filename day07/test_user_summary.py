import unittest
from day07.user_summary import events_summary

class TestUserSummary(unittest.TestCase):
    def test_missing_user_id(self):
        events = [
            {"type": "click", "duration_ms": 50},
            {"user_id": 1, "type": "scroll", "duration_ms": 100},
            {"user_id": 1, "type": "click", "duration_ms": 300},
            {"user_id": 2, "type": "scroll", "duration_ms": 200},   
       ]
        with self.assertRaises(ValueError):
            events_summary(events)
    
    def test_invalid_integer(self):
        events = [
            {"user_id": "two", "type": "click", "duration_ms": 50},
            {"user_id": 1, "type": "scroll", "duration_ms": 100},
            {"user_id": 1, "type": "click", "duration_ms": 300},
            {"user_id": 2, "type": "scroll", "duration_ms": 200},   
       ]
        with self.assertRaises(ValueError):
            events_summary(events)
    
    def test_correct_values(self):
        events = [
            {"user_id": 2, "type": "click", "duration_ms": 50},
            {"user_id": 1, "type": "scroll", "duration_ms": 100},
            {"user_id": 1, "type": "click", "duration_ms": 300},
            {"user_id": 2, "type": "scroll", "duration_ms": 200},
            {"user_id": 2, "type": "scroll", "duration_ms": 450},   
       ]
        output = [
            {
                "user_id": 1,
                "total_duration_ms": 400,
                "event_counts": {"click": 1, "scroll": 1},
            },
            {
                "user_id": 2,
                "total_duration_ms": 700,
                "event_counts": {"click": 1, "scroll": 2},
            },    
        ]
        self.assertEqual(events_summary(events), output)
    def test_order_by_userid(self):
        events = [
            {"user_id": 3, "type": "click", "duration_ms": 50},
            {"user_id": 6, "type": "scroll", "duration_ms": 100},
            {"user_id": 1, "type": "click", "duration_ms": 300},
            {"user_id": 3, "type": "scroll", "duration_ms": 200},
            {"user_id": 2, "type": "scroll", "duration_ms": 450},
            {"user_id": 5, "type": "scroll", "duration_ms": 100},
            {"user_id": 4, "type": "click", "duration_ms": 50}   
       ]
        output = [
            {
                "user_id": 1,
                "total_duration_ms": 300,
                "event_counts": {"click": 1},
            },
            {
                "user_id": 2,
                "total_duration_ms": 450,
                "event_counts": {"scroll": 1},
            },
            {
                "user_id": 3,
                "total_duration_ms": 250,
                "event_counts": {"click": 1, "scroll": 1},
            },
            {
                "user_id": 4,
                "total_duration_ms": 50,
                "event_counts": {"click": 1},
            },
            {
                "user_id": 5,
                "total_duration_ms": 100,
                "event_counts": {"scroll": 1},
            },
            {
                "user_id": 6,
                "total_duration_ms": 100,
                "event_counts": {"scroll": 1},
            },    
        ]
        self.assertEqual(events_summary(events), output)
    def empty_events_list(self):
        events = [
            {}
        ]
        output = [
            {}
        ]
        self.assertEqual(events_summary(events), output)
    
if "name" == "__main__":
    unittest.main()


