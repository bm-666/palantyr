import { UIContainerStatus } from "../model";


export const UI_STATUS_COLOR: Record<UIContainerStatus, string> = {
    running: "bg-green-500",
    stopped: "bg-red-500",
    paused: "bg-yellow-400",
};