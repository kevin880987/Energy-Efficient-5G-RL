from dataclasses import dataclass
from pathlib import Path

from environments.energy_efficient_5g_rl.env import config as env_cfg
from environments.energy_efficient_5g_rl.traffic import config as traffic_cfg


@dataclass
class CellularNetworkConfiguration:
    """Configuration holder for MultiCellNetEnv with sensible defaults from train scripts."""

    # traffic / timing
    scenario: str = env_cfg.trafficScenario or "RANDOM"
    start_time: str | int = env_cfg.startTime
    accelerate: int = 1200  # matches train.sh default
    episode_len: int | None = None  # use env default if None
    action_interval: int = env_cfg.actionInterval
    time_step: float = env_cfg.timeStep

    # environment shape
    area_size: float | tuple = env_cfg.areaSize
    dpi_sample_rate: float | None = None

    # switches / features
    no_interf: bool = False
    no_offload: bool = False
    max_sleep: int = env_cfg.numSleepModes - 1

    # reward weights (align with train.sh defaults)
    w_qos: float = 4.0
    w_xqos: float = 0.005

    # logging
    stats_dir: Path | str | None = None
    save_trajectory: bool = False
    include_bs_info: bool = False

    # RL compatibility flags
    enable_switch: bool = False  # no separate switch head in this env

    def as_env_kwargs(self) -> dict:
        return dict(
            area_size=self.area_size,
            scenario=self.scenario,
            start_time=self.start_time,
            episode_len=self.episode_len,
            time_step=self.time_step,
            accelerate=self.accelerate,
            action_interval=self.action_interval,
            no_interf=self.no_interf,
            no_offload=self.no_offload,
            max_sleep=self.max_sleep,
            dpi_sample_rate=self.dpi_sample_rate,
            w_qos=self.w_qos,
            w_xqos=self.w_xqos,
            save_trajectory=self.save_trajectory,
            include_bs_info=self.include_bs_info,
            stats_dir=self.stats_dir,
        )
