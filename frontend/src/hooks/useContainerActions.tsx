import { containerAction } from "@/services/api/containers";
import { ContainerAction } from "@/types/container-actions";

export function useContainerActions(containerId: string) {
  const run = async (action: ContainerAction) => {
    try {
      await containerAction(containerId, action);
      // позже: invalidate cache / refetch
    } catch (e) {
      console.error(e);
    }
  };

  return {
    start: () => run("start"),
    stop: () => run("stop"),
    pause: () => run("pause"),
    unpause: () => run("unpause"),
    restart: () => run("restart")
  };
}
