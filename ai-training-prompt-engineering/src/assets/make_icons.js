// Render react-icons to white PNGs for slide icon circles
const React = require('react');
const ReactDOMServer = require('react-dom/server');
const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

const Fi = require('react-icons/fi');
const Fa = require('react-icons/fa');

const icons = {
  brain: Fa.FaBrain,
  chat: Fi.FiMessageSquare,
  search: Fi.FiSearch,
  database: Fi.FiDatabase,
  layers: Fi.FiLayers,
  cpu: Fi.FiCpu,
  shield: Fi.FiShield,
  alert: Fi.FiAlertTriangle,
  check: Fi.FiCheckCircle,
  x: Fi.FiXCircle,
  file: Fi.FiFileText,
  chart: Fi.FiBarChart2,
  image: Fi.FiImage,
  video: Fi.FiVideo,
  mic: Fi.FiMic,
  globe: Fi.FiGlobe,
  tool: Fi.FiTool,
  zap: Fi.FiZap,
  book: Fi.FiBookOpen,
  users: Fi.FiUsers,
  lock: Fi.FiLock,
  key: Fi.FiKey,
  branch: Fi.FiGitBranch,
  robot: Fa.FaRobot,
  memory: Fi.FiHardDrive,
  repeat: Fi.FiRepeat,
  target: Fi.FiTarget,
  eye: Fi.FiEye,
  edit: Fi.FiEdit3,
  list: Fi.FiList,
  layout: Fi.FiLayout,
  compass: Fi.FiCompass,
  translate: Fi.FiGlobe,
  arrow: Fi.FiArrowRight,
  refresh: Fi.FiRefreshCw,
  clock: Fi.FiClock,
  award: Fi.FiAward,
  hand: Fa.FaRegHandPaper,
  scale: Fa.FaBalanceScale,
  flask: Fa.FaFlask,
  arm: Fa.FaRobot,
  send: Fi.FiSend,
  folder: Fi.FiFolder,
  filter: Fi.FiFilter,
  help: Fi.FiHelpCircle,
  star: Fi.FiStar,
  trend: Fi.FiTrendingUp,
  download: Fi.FiDownload,
  terminal: Fi.FiTerminal,
  code: Fi.FiCode,
  command: Fi.FiCommand,
  package: Fi.FiPackage,
  server: Fi.FiServer,
  archive: Fi.FiArchive,
  copy: Fi.FiCopy,
  share: Fi.FiShare2,
  sliders: Fi.FiSliders,
  grid: Fi.FiGrid,
  map: Fi.FiMap,
  flag: Fi.FiFlag,
  dollar: Fi.FiDollarSign,
  activity: Fi.FiActivity,
  inbox: Fi.FiInbox,
  window: Fi.FiMaximize,
  paperclip: Fi.FiPaperclip,
  save: Fi.FiSave,
  tag: Fi.FiTag,
  thumbsup: Fi.FiThumbsUp,
  playcircle: Fi.FiPlayCircle,
  slash: Fi.FiSlash,
  link: Fi.FiLink,
  monitor: Fi.FiMonitor,
  home: Fi.FiHome,
  pen: Fa.FaPenFancy,
  gavel: Fa.FaGavel,
  dragon: Fa.FaDragon,
  history: Fa.FaHistory,
  sitemap: Fa.FaSitemap,
  table: Fa.FaTable,
  html: Fa.FaCode,
};

(async () => {
  const outDir = path.join(__dirname, 'icons');
  fs.mkdirSync(outDir, { recursive: true });
  for (const [name, Comp] of Object.entries(icons)) {
    for (const [variant, color] of [['w', '#FFFFFF'], ['d', '#22303A'], ['t', '#0E7C7B']]) {
      const svg = ReactDOMServer.renderToStaticMarkup(
        React.createElement(Comp, { color, size: 256 })
      );
      await sharp(Buffer.from(svg)).resize(256, 256, { fit: 'contain', background: { r: 0, g: 0, b: 0, alpha: 0 } }).png().toFile(path.join(outDir, `${name}_${variant}.png`));
    }
  }
  console.log('icons done:', Object.keys(icons).length * 3);
})();
