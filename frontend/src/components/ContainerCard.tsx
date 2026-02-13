import { ContainerSchema } from "@/modules/containers/model";
import { StatusBadge } from "./StatusBadge";
import { PlayIcon } from "./icons/PlayIcon";
import { StopIcon } from "./icons/StopIcon";
import { IconButton } from "./ui/IconButton";
import { PauseIcon } from "./icons/PauseIcon";
import { StatusDot } from "@/modules/containers/ui/StatusDot";
import { DOCKER_TO_UI_STATUS } from "@/modules/containers/model";
import { useContainerActions } from "@/hooks/useContainerActions";
import { Console } from "console";
import { ACTION_AVAILABILITY } from "@/modules/containers/ui/containerActionState";
import { RestartIcon } from "./icons/RestartIcon";
/**export function ContainerCard({container}: {container: ContainerSchema}){
    return (
    <div className="p-4 border rounded-xl flex items-center shadow-sm bg-white">
        <div>
          <h2 className="text-lg font-bold">{container.name}</h2>
          <p className="text-sm text-gray-500">{container.status}</p>
        </div>
        <StatusBadge status={container.status} />
      </div>
    );
}
**/

export function ContainerCard({ container }: { container: ContainerSchema }) {
  const uiStatus = DOCKER_TO_UI_STATUS[container.status]
  const {start, stop, pause, unpause, restart } = useContainerActions(container.containerId)
  const availability = ACTION_AVAILABILITY[uiStatus]
  
  return (
    <div className="p-4 border rounded-xl flex items-center gap-3 shadow-sm bg-white hover:shadow-md transition">
    <div className="flex items-center gap-2">
        <StatusDot status={uiStatus} />
        <span className="text-sm font-medium">
          {container.name}
        </span>
      </div>

      {/* Правая часть: кнопки */}
      <div className="flex items-center gap-1">
        <IconButton
          title="Start"
          onClick={start}
          disabled={!availability.start}
          >
          <PlayIcon />
        </IconButton>

        <IconButton
          title="Stop"
          onClick={stop}
          disabled={!availability.stop}  
        >
          <StopIcon />
        </IconButton>
        
        <IconButton 
          title="Pause"
          onClick={pause}
          disabled={!availability.pause}
        >
          <PauseIcon />
        </IconButton>

        <IconButton 
          title="Restart"
          onClick={restart}
        >
          <RestartIcon/>
        </IconButton>
      </div>  

    </div>
  );
}
