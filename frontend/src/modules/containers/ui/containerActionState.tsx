import { UIContainerStatus } from "../model";

export const ACTION_AVAILABILITY : Record<
    UIContainerStatus,
    {start: boolean, pause: boolean, stop: boolean, restart: boolean}
> = {
    running:  { start: false, pause: true,  stop: true, restart: true },
    paused:   { start: true,  pause: false, stop: false, restart: true },
    stopped:  { start: true,  pause: false, stop: false, restart: true },
};