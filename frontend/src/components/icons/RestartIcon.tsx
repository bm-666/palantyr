export function RestartIcon() {
    return (
      <svg
        viewBox="0 0 24 24"
        className="w-5 h-5 text-blue-600"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
      >
        {/* круг */}
        <path d="M21 12a9 9 0 1 1-3-6.7" />
        {/* стрелка */}
        <polyline points="21 3 21 9 15 9" />
      </svg>
    );
  }