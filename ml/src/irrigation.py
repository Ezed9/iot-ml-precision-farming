"""Transparent irrigation decision baseline."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class IrrigationAdvice:
    action: str
    reason: str
    urgency: str


def recommend_irrigation(
    moisture_percent: float,
    target_min_percent: float,
    target_max_percent: float,
    rain_probability_percent: float = 0.0,
) -> IrrigationAdvice:
    if not 0 <= moisture_percent <= 100:
        raise ValueError("moisture_percent must be between 0 and 100")
    if target_min_percent > target_max_percent:
        raise ValueError("target_min_percent must not exceed target_max_percent")
    if moisture_percent < target_min_percent and rain_probability_percent < 60:
        return IrrigationAdvice("irrigate", "soil moisture is below the crop target range", "high")
    if moisture_percent < target_min_percent and rain_probability_percent >= 60:
        return IrrigationAdvice("delay_and_monitor", "rain is likely while moisture is below target", "medium")
    if moisture_percent > target_max_percent:
        return IrrigationAdvice("do_not_irrigate", "soil moisture is above the crop target range", "medium")
    return IrrigationAdvice("no_action", "soil moisture is within the crop target range", "low")

