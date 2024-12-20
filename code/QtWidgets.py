"""
This page contains the API documentation of a compact version of the **PySide6.QtWidgets** module. 
"""

# Module `PySide6.QtWidgets`

import PySide6.QtWidgets
import PySide6.QtCore
import PySide6.QtGui

import enum
from typing import (
    Any,
    ClassVar,
    Dict,
    Iterable,
    List,
    Optional,
    Sequence,
    Text,
    Tuple,
    Type,
    Union,
    overload,
)
from PySide6.QtCore import Signal, SignalInstance
from shiboken6 import Shiboken

NoneType = type(None)


class QWidget:
    """
    <hr>

    The `QWidget` class is the base class of all user interface objects in PySide6.QtWidgets.

    Args:
        parent (PySide6.QtWidgets.QWidget): The parent widget of this widget.

    <hr>

    <h3>Methods</h3>

    <ul>
        <li><a href="#code.QtWidgets.QWidget.resize"><code>resize</code></a></li>
        <li><a href="#code.QtWidgets.QWidget.setLayout"><code>setLayout</code></a></li>
        <li><a href="#code.QtWidgets.QWidget.show"><code>show</code></a></li>
    </ul>

    <br>

    **Examples**
    <hr>
    ``` py
    widget = QtWidgets.QWidget()
    widget.resize(250, 150)

    # QPushButton is a subclass of QWidget
    button = QtWidgets.QPushButton("press me")
    button.resize(100, 50)
    ```
    In the above code we show that we can apply the <a href="#code.QtWidgets.QWidget.resize"><code>resize</code></a> method to all widgets that inherit from `QWidget` such as [`QPushButton`](QPushButton.md).
    Another example with [`QMainWindow`](QMainWindow.md) is shown below:

    ``` py
    # QApplication is required to run the application
    app = QtWidgets.QApplication()

    # QMainWindow is a subclass of QWidget
    window = QtWidgets.QMainWindow()
    window.resize(500, 300)

    # Displays an empty window with a size of 500x300 pixels
    window.show()
    app.exec()
    ```

    <br>
    The following example shows two methods to set a layout manager for a `QWidget`. The two methods are equivalent.
    ```py
    # Create a main window with a central widget
    window = QtWidgets.QMainWindow()
    widget = QtWidgets.QWidget()
    window.setCentralWidget(widget)

    # method 1
    layout = QtWidgets.QVBoxLayout()
    widget.setLayout(layout)

    # method 2
    layout = QtWidgets.QVBoxLayout(widget)
    ```

    <hr>
    <br>
    """

    #     customContextMenuRequested: ClassVar[Signal] = ... # customContextMenuRequested(QPoint)
    #     windowIconChanged        : ClassVar[Signal] = ... # windowIconChanged(QIcon)
    #     windowIconTextChanged    : ClassVar[Signal] = ... # windowIconTextChanged(QString)
    #     windowTitleChanged       : ClassVar[Signal] = ... # windowTitleChanged(QString)

    #     class RenderFlag(enum.Flag):

    #         DrawWindowBackground     : QWidget.RenderFlag = ... # 0x1
    #         DrawChildren             : QWidget.RenderFlag = ... # 0x2
    #         IgnoreMask               : QWidget.RenderFlag = ... # 0x4

    def __init__(self, parent: Optional[PySide6.QtWidgets.QWidget] = None) -> None: ...

    #     def acceptDrops(self) -> bool: ...
    #     def accessibleDescription(self) -> str: ...
    #     def accessibleName(self) -> str: ...
    #     def actionEvent(self, event: PySide6.QtGui.QActionEvent) -> None: ...
    #     def actions(self) -> List[PySide6.QtGui.QAction]: ...
    #     def activateWindow(self) -> None: ...
    #     @overload
    #     def addAction(self, action: PySide6.QtGui.QAction) -> None: ...
    #     @overload
    #     def addAction(self, icon: Union[PySide6.QtGui.QIcon, PySide6.QtGui.QPixmap], text: str) -> PySide6.QtGui.QAction: ...
    #     @overload
    #     def addAction(self, icon: Union[PySide6.QtGui.QIcon, PySide6.QtGui.QPixmap], text: str, callable: object) -> PySide6.QtGui.QAction: ...
    #     @overload
    #     def addAction(self, icon: Union[PySide6.QtGui.QIcon, PySide6.QtGui.QPixmap], text: str, receiver: PySide6.QtCore.QObject, member: bytes, type: PySide6.QtCore.Qt.ConnectionType = ...) -> PySide6.QtGui.QAction: ...
    #     @overload
    #     def addAction(self, icon: Union[PySide6.QtGui.QIcon, PySide6.QtGui.QPixmap], text: str, shortcut: Union[PySide6.QtGui.QKeySequence, PySide6.QtCore.QKeyCombination, PySide6.QtGui.QKeySequence.StandardKey, str, int]) -> PySide6.QtGui.QAction: ...
    #     @overload
    #     def addAction(self, icon: Union[PySide6.QtGui.QIcon, PySide6.QtGui.QPixmap], text: str, shortcut: Union[PySide6.QtGui.QKeySequence, PySide6.QtCore.QKeyCombination, PySide6.QtGui.QKeySequence.StandardKey, str, int], callable: object) -> PySide6.QtGui.QAction: ...
    #     @overload
    #     def addAction(self, icon: Union[PySide6.QtGui.QIcon, PySide6.QtGui.QPixmap], text: str, shortcut: Union[PySide6.QtGui.QKeySequence, PySide6.QtCore.QKeyCombination, PySide6.QtGui.QKeySequence.StandardKey, str, int], receiver: PySide6.QtCore.QObject, member: bytes, type: PySide6.QtCore.Qt.ConnectionType = ...) -> PySide6.QtGui.QAction: ...
    #     @overload
    #     def addAction(self, text: str) -> PySide6.QtGui.QAction: ...
    #     @overload
    #     def addAction(self, text: str, callable: object) -> PySide6.QtGui.QAction: ...
    #     @overload
    #     def addAction(self, text: str, receiver: PySide6.QtCore.QObject, member: bytes, type: PySide6.QtCore.Qt.ConnectionType = ...) -> PySide6.QtGui.QAction: ...
    #     @overload
    #     def addAction(self, text: str, shortcut: Union[PySide6.QtGui.QKeySequence, PySide6.QtCore.QKeyCombination, PySide6.QtGui.QKeySequence.StandardKey, str, int]) -> PySide6.QtGui.QAction: ...
    #     @overload
    #     def addAction(self, text: str, shortcut: Union[PySide6.QtGui.QKeySequence, PySide6.QtCore.QKeyCombination, PySide6.QtGui.QKeySequence.StandardKey, str, int], callable: object) -> PySide6.QtGui.QAction: ...
    #     @overload
    #     def addAction(self, text: str, shortcut: Union[PySide6.QtGui.QKeySequence, PySide6.QtCore.QKeyCombination, PySide6.QtGui.QKeySequence.StandardKey, str, int], receiver: PySide6.QtCore.QObject, member: bytes, type: PySide6.QtCore.Qt.ConnectionType = ...) -> PySide6.QtGui.QAction: ...
    #     def addActions(self, actions: Sequence[PySide6.QtGui.QAction]) -> None: ...
    #     def adjustSize(self) -> None: ...
    #     def autoFillBackground(self) -> bool: ...
    #     def backgroundRole(self) -> PySide6.QtGui.QPalette.ColorRole: ...
    #     def backingStore(self) -> PySide6.QtGui.QBackingStore: ...
    #     def baseSize(self) -> PySide6.QtCore.QSize: ...
    #     def changeEvent(self, event: PySide6.QtCore.QEvent) -> None: ...
    #     @overload
    #     def childAt(self, p: PySide6.QtCore.QPoint) -> PySide6.QtWidgets.QWidget: ...
    #     @overload
    #     def childAt(self, x: int, y: int) -> PySide6.QtWidgets.QWidget: ...
    #     def childrenRect(self) -> PySide6.QtCore.QRect: ...
    #     def childrenRegion(self) -> PySide6.QtGui.QRegion: ...
    #     def clearFocus(self) -> None: ...
    #     def clearMask(self) -> None: ...
    #     def close(self) -> bool: ...
    #     def closeEvent(self, event: PySide6.QtGui.QCloseEvent) -> None: ...
    #     def contentsMargins(self) -> PySide6.QtCore.QMargins: ...
    #     def contentsRect(self) -> PySide6.QtCore.QRect: ...
    #     def contextMenuEvent(self, event: PySide6.QtGui.QContextMenuEvent) -> None: ...
    #     def contextMenuPolicy(self) -> PySide6.QtCore.Qt.ContextMenuPolicy: ...
    #     def create(self, arg__1: int = ..., initializeWindow: bool = ..., destroyOldWindow: bool = ...) -> None: ...
    #     def createWinId(self) -> None: ...
    #     @staticmethod
    #     def createWindowContainer(window: PySide6.QtGui.QWindow, parent: Optional[PySide6.QtWidgets.QWidget] = ..., flags: PySide6.QtCore.Qt.WindowType = ...) -> PySide6.QtWidgets.QWidget: ...
    #     def cursor(self) -> PySide6.QtGui.QCursor: ...
    #     def destroy(self, destroyWindow: bool = ..., destroySubWindows: bool = ...) -> None: ...
    #     def devType(self) -> int: ...
    #     def dragEnterEvent(self, event: PySide6.QtGui.QDragEnterEvent) -> None: ...
    #     def dragLeaveEvent(self, event: PySide6.QtGui.QDragLeaveEvent) -> None: ...
    #     def dragMoveEvent(self, event: PySide6.QtGui.QDragMoveEvent) -> None: ...
    #     def dropEvent(self, event: PySide6.QtGui.QDropEvent) -> None: ...
    #     def effectiveWinId(self) -> int: ...
    #     def ensurePolished(self) -> None: ...
    #     def enterEvent(self, event: PySide6.QtGui.QEnterEvent) -> None: ...
    #     def event(self, event: PySide6.QtCore.QEvent) -> bool: ...
    #     @staticmethod
    #     def find(arg__1: int) -> PySide6.QtWidgets.QWidget: ...
    #     def focusInEvent(self, event: PySide6.QtGui.QFocusEvent) -> None: ...
    #     def focusNextChild(self) -> bool: ...
    #     def focusNextPrevChild(self, next: bool) -> bool: ...
    #     def focusOutEvent(self, event: PySide6.QtGui.QFocusEvent) -> None: ...
    #     def focusPolicy(self) -> PySide6.QtCore.Qt.FocusPolicy: ...
    #     def focusPreviousChild(self) -> bool: ...
    #     def focusProxy(self) -> PySide6.QtWidgets.QWidget: ...
    #     def focusWidget(self) -> PySide6.QtWidgets.QWidget: ...
    #     def font(self) -> PySide6.QtGui.QFont: ...
    #     def fontInfo(self) -> PySide6.QtGui.QFontInfo: ...
    #     def fontMetrics(self) -> PySide6.QtGui.QFontMetrics: ...
    #     def foregroundRole(self) -> PySide6.QtGui.QPalette.ColorRole: ...
    #     def frameGeometry(self) -> PySide6.QtCore.QRect: ...
    #     def frameSize(self) -> PySide6.QtCore.QSize: ...
    #     def geometry(self) -> PySide6.QtCore.QRect: ...
    #     def grab(self, rectangle: PySide6.QtCore.QRect = ...) -> PySide6.QtGui.QPixmap: ...
    #     def grabGesture(self, type: PySide6.QtCore.Qt.GestureType, flags: PySide6.QtCore.Qt.GestureFlag = ...) -> None: ...
    #     def grabKeyboard(self) -> None: ...
    #     @overload
    #     def grabMouse(self) -> None: ...
    #     @overload
    #     def grabMouse(self, arg__1: Union[PySide6.QtGui.QCursor, PySide6.QtCore.Qt.CursorShape, PySide6.QtGui.QPixmap]) -> None: ...
    #     def grabShortcut(self, key: Union[PySide6.QtGui.QKeySequence, PySide6.QtCore.QKeyCombination, PySide6.QtGui.QKeySequence.StandardKey, str, int], context: PySide6.QtCore.Qt.ShortcutContext = ...) -> int: ...
    #     def graphicsEffect(self) -> PySide6.QtWidgets.QGraphicsEffect: ...
    #     def graphicsProxyWidget(self) -> PySide6.QtWidgets.QGraphicsProxyWidget: ...
    #     def hasFocus(self) -> bool: ...
    #     def hasHeightForWidth(self) -> bool: ...
    #     def hasMouseTracking(self) -> bool: ...
    #     def hasTabletTracking(self) -> bool: ...
    #     def height(self) -> int: ...
    #     def heightForWidth(self, arg__1: int) -> int: ...
    #     def hide(self) -> None: ...
    #     def hideEvent(self, event: PySide6.QtGui.QHideEvent) -> None: ...
    #     def initPainter(self, painter: PySide6.QtGui.QPainter) -> None: ...
    #     def inputMethodEvent(self, event: PySide6.QtGui.QInputMethodEvent) -> None: ...
    #     def inputMethodHints(self) -> PySide6.QtCore.Qt.InputMethodHint: ...
    #     def inputMethodQuery(self, arg__1: PySide6.QtCore.Qt.InputMethodQuery) -> Any: ...
    #     def insertAction(self, before: PySide6.QtGui.QAction, action: PySide6.QtGui.QAction) -> None: ...
    #     def insertActions(self, before: PySide6.QtGui.QAction, actions: Sequence[PySide6.QtGui.QAction]) -> None: ...
    #     def internalWinId(self) -> int: ...
    #     def isActiveWindow(self) -> bool: ...
    #     def isAncestorOf(self, child: PySide6.QtWidgets.QWidget) -> bool: ...
    #     def isEnabled(self) -> bool: ...
    #     def isEnabledTo(self, arg__1: PySide6.QtWidgets.QWidget) -> bool: ...
    #     def isFullScreen(self) -> bool: ...
    #     def isHidden(self) -> bool: ...
    #     def isLeftToRight(self) -> bool: ...
    #     def isMaximized(self) -> bool: ...
    #     def isMinimized(self) -> bool: ...
    #     def isModal(self) -> bool: ...
    #     def isRightToLeft(self) -> bool: ...
    #     def isTopLevel(self) -> bool: ...
    #     def isVisible(self) -> bool: ...
    #     def isVisibleTo(self, arg__1: PySide6.QtWidgets.QWidget) -> bool: ...
    #     def isWindow(self) -> bool: ...
    #     def isWindowModified(self) -> bool: ...
    #     def keyPressEvent(self, event: PySide6.QtGui.QKeyEvent) -> None: ...
    #     def keyReleaseEvent(self, event: PySide6.QtGui.QKeyEvent) -> None: ...
    #     @staticmethod
    #     def keyboardGrabber() -> PySide6.QtWidgets.QWidget: ...
    #     def layout(self) -> PySide6.QtWidgets.QLayout: ...
    #     def layoutDirection(self) -> PySide6.QtCore.Qt.LayoutDirection: ...
    #     def leaveEvent(self, event: PySide6.QtCore.QEvent) -> None: ...
    #     def locale(self) -> PySide6.QtCore.QLocale: ...
    #     def lower(self) -> None: ...
    #     @overload
    #     def mapFrom(self, arg__1: PySide6.QtWidgets.QWidget, arg__2: PySide6.QtCore.QPoint) -> PySide6.QtCore.QPoint: ...
    #     @overload
    #     def mapFrom(self, arg__1: PySide6.QtWidgets.QWidget, arg__2: Union[PySide6.QtCore.QPointF, PySide6.QtCore.QPoint, PySide6.QtGui.QPainterPath.Element]) -> PySide6.QtCore.QPointF: ...
    #     @overload
    #     def mapFromGlobal(self, arg__1: PySide6.QtCore.QPoint) -> PySide6.QtCore.QPoint: ...
    #     @overload
    #     def mapFromGlobal(self, arg__1: Union[PySide6.QtCore.QPointF, PySide6.QtCore.QPoint, PySide6.QtGui.QPainterPath.Element]) -> PySide6.QtCore.QPointF: ...
    #     @overload
    #     def mapFromParent(self, arg__1: PySide6.QtCore.QPoint) -> PySide6.QtCore.QPoint: ...
    #     @overload
    #     def mapFromParent(self, arg__1: Union[PySide6.QtCore.QPointF, PySide6.QtCore.QPoint, PySide6.QtGui.QPainterPath.Element]) -> PySide6.QtCore.QPointF: ...
    #     @overload
    #     def mapTo(self, arg__1: PySide6.QtWidgets.QWidget, arg__2: PySide6.QtCore.QPoint) -> PySide6.QtCore.QPoint: ...
    #     @overload
    #     def mapTo(self, arg__1: PySide6.QtWidgets.QWidget, arg__2: Union[PySide6.QtCore.QPointF, PySide6.QtCore.QPoint, PySide6.QtGui.QPainterPath.Element]) -> PySide6.QtCore.QPointF: ...
    #     @overload
    #     def mapToGlobal(self, arg__1: PySide6.QtCore.QPoint) -> PySide6.QtCore.QPoint: ...
    #     @overload
    #     def mapToGlobal(self, arg__1: Union[PySide6.QtCore.QPointF, PySide6.QtCore.QPoint, PySide6.QtGui.QPainterPath.Element]) -> PySide6.QtCore.QPointF: ...
    #     @overload
    #     def mapToParent(self, arg__1: PySide6.QtCore.QPoint) -> PySide6.QtCore.QPoint: ...
    #     @overload
    #     def mapToParent(self, arg__1: Union[PySide6.QtCore.QPointF, PySide6.QtCore.QPoint, PySide6.QtGui.QPainterPath.Element]) -> PySide6.QtCore.QPointF: ...
    #     def mask(self) -> PySide6.QtGui.QRegion: ...
    #     def maximumHeight(self) -> int: ...
    #     def maximumSize(self) -> PySide6.QtCore.QSize: ...
    #     def maximumWidth(self) -> int: ...
    #     def metric(self, arg__1: PySide6.QtGui.QPaintDevice.PaintDeviceMetric) -> int: ...
    #     def minimumHeight(self) -> int: ...
    #     def minimumSize(self) -> PySide6.QtCore.QSize: ...
    #     def minimumSizeHint(self) -> PySide6.QtCore.QSize: ...
    #     def minimumWidth(self) -> int: ...
    #     def mouseDoubleClickEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    #     @staticmethod
    #     def mouseGrabber() -> PySide6.QtWidgets.QWidget: ...
    #     def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    #     def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    #     def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    #     @overload
    #     def move(self, arg__1: PySide6.QtCore.QPoint) -> None: ...
    #     @overload
    #     def move(self, x: int, y: int) -> None: ...
    #     def moveEvent(self, event: PySide6.QtGui.QMoveEvent) -> None: ...
    #     def nativeEvent(self, eventType: Union[PySide6.QtCore.QByteArray, bytes], message: int) -> object: ...
    #     def nativeParentWidget(self) -> PySide6.QtWidgets.QWidget: ...
    #     def nextInFocusChain(self) -> PySide6.QtWidgets.QWidget: ...
    #     def normalGeometry(self) -> PySide6.QtCore.QRect: ...
    #     def overrideWindowFlags(self, type: PySide6.QtCore.Qt.WindowType) -> None: ...
    #     def overrideWindowState(self, state: PySide6.QtCore.Qt.WindowState) -> None: ...
    #     def paintEngine(self) -> PySide6.QtGui.QPaintEngine: ...
    #     def paintEvent(self, event: PySide6.QtGui.QPaintEvent) -> None: ...
    #     def palette(self) -> PySide6.QtGui.QPalette: ...
    #     def parentWidget(self) -> PySide6.QtWidgets.QWidget: ...
    #     def pos(self) -> PySide6.QtCore.QPoint: ...
    #     def previousInFocusChain(self) -> PySide6.QtWidgets.QWidget: ...
    #     def raise_(self) -> None: ...
    #     def rect(self) -> PySide6.QtCore.QRect: ...
    #     def redirected(self, offset: PySide6.QtCore.QPoint) -> PySide6.QtGui.QPaintDevice: ...
    #     def releaseKeyboard(self) -> None: ...
    #     def releaseMouse(self) -> None: ...
    #     def releaseShortcut(self, id: int) -> None: ...
    #     def removeAction(self, action: PySide6.QtGui.QAction) -> None: ...
    #     @overload
    #     def render(self, painter: PySide6.QtGui.QPainter, targetOffset: PySide6.QtCore.QPoint, sourceRegion: Union[PySide6.QtGui.QRegion, PySide6.QtGui.QBitmap, PySide6.QtGui.QPolygon, PySide6.QtCore.QRect] = ..., renderFlags: PySide6.QtWidgets.QWidget.RenderFlag = ...) -> None: ...
    #     @overload
    #     def render(self, target: PySide6.QtGui.QPaintDevice, targetOffset: PySide6.QtCore.QPoint = ..., sourceRegion: Union[PySide6.QtGui.QRegion, PySide6.QtGui.QBitmap, PySide6.QtGui.QPolygon, PySide6.QtCore.QRect] = ..., renderFlags: PySide6.QtWidgets.QWidget.RenderFlag = ...) -> None: ...
    #     @overload
    #     def repaint(self) -> None: ...
    #     @overload
    #     def repaint(self, arg__1: PySide6.QtCore.QRect) -> None: ...
    #     @overload
    #     def repaint(self, arg__1: Union[PySide6.QtGui.QRegion, PySide6.QtGui.QBitmap, PySide6.QtGui.QPolygon, PySide6.QtCore.QRect]) -> None: ...
    #     @overload
    #     def repaint(self, x: int, y: int, w: int, h: int) -> None: ...
    #     @overload
    #     def resize(self, arg__1: PySide6.QtCore.QSize) -> None: ...

    def resize(self, w: int, h: int) -> None:
        """
        Resizes the widget to have a width of `w` pixels and a height of `h` pixels.

        Args:
            w (int): The width of the widget in pixels.
            h (int): The height of the widget in pixels.

        <br>
        """

    #     def resizeEvent(self, event: PySide6.QtGui.QResizeEvent) -> None: ...
    #     def restoreGeometry(self, geometry: Union[PySide6.QtCore.QByteArray, bytes]) -> bool: ...
    #     def saveGeometry(self) -> PySide6.QtCore.QByteArray: ...
    #     def screen(self) -> PySide6.QtGui.QScreen: ...
    #     @overload
    #     def scroll(self, dx: int, dy: int) -> None: ...
    #     @overload
    #     def scroll(self, dx: int, dy: int, arg__3: PySide6.QtCore.QRect) -> None: ...
    #     def setAcceptDrops(self, on: bool) -> None: ...
    #     def setAccessibleDescription(self, description: str) -> None: ...
    #     def setAccessibleName(self, name: str) -> None: ...
    #     def setAttribute(self, arg__1: PySide6.QtCore.Qt.WidgetAttribute, on: bool = ...) -> None: ...
    #     def setAutoFillBackground(self, enabled: bool) -> None: ...
    #     def setBackgroundRole(self, arg__1: PySide6.QtGui.QPalette.ColorRole) -> None: ...
    #     @overload
    #     def setBaseSize(self, arg__1: PySide6.QtCore.QSize) -> None: ...
    #     @overload
    #     def setBaseSize(self, basew: int, baseh: int) -> None: ...
    #     @overload
    #     def setContentsMargins(self, left: int, top: int, right: int, bottom: int) -> None: ...
    #     @overload
    #     def setContentsMargins(self, margins: PySide6.QtCore.QMargins) -> None: ...
    #     def setContextMenuPolicy(self, policy: PySide6.QtCore.Qt.ContextMenuPolicy) -> None: ...
    #     def setCursor(self, arg__1: Union[PySide6.QtGui.QCursor, PySide6.QtCore.Qt.CursorShape, PySide6.QtGui.QPixmap]) -> None: ...
    #     def setDisabled(self, arg__1: bool) -> None: ...
    #     def setEnabled(self, arg__1: bool) -> None: ...
    #     def setFixedHeight(self, h: int) -> None: ...
    #     @overload
    #     def setFixedSize(self, arg__1: PySide6.QtCore.QSize) -> None: ...
    #     @overload
    #     def setFixedSize(self, w: int, h: int) -> None: ...
    #     def setFixedWidth(self, w: int) -> None: ...
    #     @overload
    #     def setFocus(self) -> None: ...
    #     @overload
    #     def setFocus(self, reason: PySide6.QtCore.Qt.FocusReason) -> None: ...
    #     def setFocusPolicy(self, policy: PySide6.QtCore.Qt.FocusPolicy) -> None: ...
    #     def setFocusProxy(self, arg__1: PySide6.QtWidgets.QWidget) -> None: ...
    #     def setFont(self, arg__1: Union[PySide6.QtGui.QFont, str, Sequence[str]]) -> None: ...
    #     def setForegroundRole(self, arg__1: PySide6.QtGui.QPalette.ColorRole) -> None: ...
    #     @overload
    #     def setGeometry(self, arg__1: PySide6.QtCore.QRect) -> None: ...
    #     @overload
    #     def setGeometry(self, x: int, y: int, w: int, h: int) -> None: ...
    #     def setGraphicsEffect(self, effect: PySide6.QtWidgets.QGraphicsEffect) -> None: ...
    #     def setHidden(self, hidden: bool) -> None: ...
    #     def setInputMethodHints(self, hints: PySide6.QtCore.Qt.InputMethodHint) -> None: ...
    def setLayout(self, layout: PySide6.QtWidgets.QLayout) -> None:
        """
        Sets the layout manager for this widget. An alternative to calling this function is to pass
        this widget to the layout's constructor, as shown in the last example above.

        Args:
            layout (PySide6.QtWidgets.QLayout): The layout manager to set for this widget.

        <br>
        """

    #     def setLayoutDirection(self, direction: PySide6.QtCore.Qt.LayoutDirection) -> None: ...
    #     def setLocale(self, locale: Union[PySide6.QtCore.QLocale, PySide6.QtCore.QLocale.Language]) -> None: ...
    #     @overload
    #     def setMask(self, arg__1: Union[PySide6.QtGui.QBitmap, str]) -> None: ...
    #     @overload
    #     def setMask(self, arg__1: Union[PySide6.QtGui.QRegion, PySide6.QtGui.QBitmap, PySide6.QtGui.QPolygon, PySide6.QtCore.QRect]) -> None: ...
    #     def setMaximumHeight(self, maxh: int) -> None: ...
    #     @overload
    #     def setMaximumSize(self, arg__1: PySide6.QtCore.QSize) -> None: ...
    #     @overload
    #     def setMaximumSize(self, maxw: int, maxh: int) -> None: ...
    #     def setMaximumWidth(self, maxw: int) -> None: ...
    #     def setMinimumHeight(self, minh: int) -> None: ...
    #     @overload
    #     def setMinimumSize(self, arg__1: PySide6.QtCore.QSize) -> None: ...
    #     @overload
    #     def setMinimumSize(self, minw: int, minh: int) -> None: ...
    #     def setMinimumWidth(self, minw: int) -> None: ...
    #     def setMouseTracking(self, enable: bool) -> None: ...
    #     def setPalette(self, arg__1: Union[PySide6.QtGui.QPalette, PySide6.QtCore.Qt.GlobalColor, PySide6.QtGui.QColor]) -> None: ...
    #     @overload
    #     def setParent(self, parent: Optional[PySide6.QtWidgets.QWidget]) -> None: ...
    #     @overload
    #     def setParent(self, parent: Optional[PySide6.QtWidgets.QWidget], f: PySide6.QtCore.Qt.WindowType) -> None: ...
    #     def setScreen(self, arg__1: PySide6.QtGui.QScreen) -> None: ...
    #     def setShortcutAutoRepeat(self, id: int, enable: bool = ...) -> None: ...
    #     def setShortcutEnabled(self, id: int, enable: bool = ...) -> None: ...
    #     @overload
    #     def setSizeIncrement(self, arg__1: PySide6.QtCore.QSize) -> None: ...
    #     @overload
    #     def setSizeIncrement(self, w: int, h: int) -> None: ...
    #     @overload
    #     def setSizePolicy(self, arg__1: PySide6.QtWidgets.QSizePolicy) -> None: ...
    #     @overload
    #     def setSizePolicy(self, horizontal: PySide6.QtWidgets.QSizePolicy.Policy, vertical: PySide6.QtWidgets.QSizePolicy.Policy) -> None: ...
    #     def setStatusTip(self, arg__1: str) -> None: ...
    #     def setStyle(self, arg__1: PySide6.QtWidgets.QStyle) -> None: ...
    #     def setStyleSheet(self, styleSheet: str) -> None: ...
    #     @staticmethod
    #     def setTabOrder(arg__1: PySide6.QtWidgets.QWidget, arg__2: PySide6.QtWidgets.QWidget) -> None: ...
    #     def setTabletTracking(self, enable: bool) -> None: ...
    #     def setToolTip(self, arg__1: str) -> None: ...
    #     def setToolTipDuration(self, msec: int) -> None: ...
    #     def setUpdatesEnabled(self, enable: bool) -> None: ...
    #     def setVisible(self, visible: bool) -> None: ...
    #     def setWhatsThis(self, arg__1: str) -> None: ...
    #     def setWindowFilePath(self, filePath: str) -> None: ...
    #     def setWindowFlag(self, arg__1: PySide6.QtCore.Qt.WindowType, on: bool = ...) -> None: ...
    #     def setWindowFlags(self, type: PySide6.QtCore.Qt.WindowType) -> None: ...
    #     def setWindowIcon(self, icon: Union[PySide6.QtGui.QIcon, PySide6.QtGui.QPixmap]) -> None: ...
    #     def setWindowIconText(self, arg__1: str) -> None: ...
    #     def setWindowModality(self, windowModality: PySide6.QtCore.Qt.WindowModality) -> None: ...
    #     def setWindowModified(self, arg__1: bool) -> None: ...
    #     def setWindowOpacity(self, level: float) -> None: ...
    #     def setWindowRole(self, arg__1: str) -> None: ...
    #     def setWindowState(self, state: PySide6.QtCore.Qt.WindowState) -> None: ...
    #     def setWindowTitle(self, arg__1: str) -> None: ...
    #     def sharedPainter(self) -> PySide6.QtGui.QPainter: ...
    def show(self) -> None:
        """
        Shows the widget and its child widgets.

        <br>
        <br>
        """


#     def showEvent(self, event: PySide6.QtGui.QShowEvent) -> None: ...
#     def showFullScreen(self) -> None: ...
#     def showMaximized(self) -> None: ...
#     def showMinimized(self) -> None: ...
#     def showNormal(self) -> None: ...
#     def size(self) -> PySide6.QtCore.QSize: ...
#     def sizeHint(self) -> PySide6.QtCore.QSize: ...
#     def sizeIncrement(self) -> PySide6.QtCore.QSize: ...
#     def sizePolicy(self) -> PySide6.QtWidgets.QSizePolicy: ...
#     def stackUnder(self, arg__1: PySide6.QtWidgets.QWidget) -> None: ...
#     def statusTip(self) -> str: ...
#     def style(self) -> PySide6.QtWidgets.QStyle: ...
#     def styleSheet(self) -> str: ...
#     def tabletEvent(self, event: PySide6.QtGui.QTabletEvent) -> None: ...
#     def testAttribute(self, arg__1: PySide6.QtCore.Qt.WidgetAttribute) -> bool: ...
#     def toolTip(self) -> str: ...
#     def toolTipDuration(self) -> int: ...
#     def topLevelWidget(self) -> PySide6.QtWidgets.QWidget: ...
#     def underMouse(self) -> bool: ...
#     def ungrabGesture(self, type: PySide6.QtCore.Qt.GestureType) -> None: ...
#     def unsetCursor(self) -> None: ...
#     def unsetLayoutDirection(self) -> None: ...
#     def unsetLocale(self) -> None: ...
#     @overload
#     def update(self) -> None: ...
#     @overload
#     def update(self, arg__1: PySide6.QtCore.QRect) -> None: ...
#     @overload
#     def update(self, arg__1: Union[PySide6.QtGui.QRegion, PySide6.QtGui.QBitmap, PySide6.QtGui.QPolygon, PySide6.QtCore.QRect]) -> None: ...
#     @overload
#     def update(self, x: int, y: int, w: int, h: int) -> None: ...
#     def updateGeometry(self) -> None: ...
#     def updateMicroFocus(self, query: PySide6.QtCore.Qt.InputMethodQuery = ...) -> None: ...
#     def updatesEnabled(self) -> bool: ...
#     def visibleRegion(self) -> PySide6.QtGui.QRegion: ...
#     def whatsThis(self) -> str: ...
#     def wheelEvent(self, event: PySide6.QtGui.QWheelEvent) -> None: ...
#     def width(self) -> int: ...
#     def winId(self) -> int: ...
#     def window(self) -> PySide6.QtWidgets.QWidget: ...
#     def windowFilePath(self) -> str: ...
#     def windowFlags(self) -> PySide6.QtCore.Qt.WindowType: ...
#     def windowHandle(self) -> PySide6.QtGui.QWindow: ...
#     def windowIcon(self) -> PySide6.QtGui.QIcon: ...
#     def windowIconText(self) -> str: ...
#     def windowModality(self) -> PySide6.QtCore.Qt.WindowModality: ...
#     def windowOpacity(self) -> float: ...
#     def windowRole(self) -> str: ...
#     def windowState(self) -> PySide6.QtCore.Qt.WindowState: ...
#     def windowTitle(self) -> str: ...
#     def windowType(self) -> PySide6.QtCore.Qt.WindowType: ...
#     def x(self) -> int: ...
#     def y(self) -> int: ...


class QLayout:
    """
    <hr>

    `QLayout` is the base class of all layout objects in PySide6.QtWidgets.

    Args:
        parent (PySide6.QtWidgets.QWidget): The parent widget of the layout.

    <hr>

    <h3>Methods</h3>

    <ul>
        <li><a href="#code.QtWidgets.QLayout.addWidget"><code>addWidget</code></a></li>
        <li><a href="#code.QtWidgets.QLayout.setSpacing"><code>setSpacing</code></a></li>
        <li><a href="#code.QtWidgets.QLayout.spacing"><code>spacing</code></a></li>

    </ul>

    <br>

    **Examples**
    <hr>
    ```py
    yes_button = QtWidgets.QPushButton("press me")
    no_button = QtWidgets.QPushButton("don't press me")

    # QVBoxLayout is a subclass of QLayout
    layout = QtWidgets.QVBoxLayout()
    layout.addWidget(button)
    layout.addWidget(no_button)
    ```
    In this example, we create two buttons and add them to [`QVBoxLayout`](QVBoxLayout.md) layout.
    We can use the `addWidget` method because `QVBoxLayout` is a subclass of `QLayout`.

    <hr>
    <br>
    """

    #     class SizeConstraint(enum.Enum):

    #         SetDefaultConstraint     : QLayout.SizeConstraint = ... # 0x0
    #         SetNoConstraint          : QLayout.SizeConstraint = ... # 0x1
    #         SetMinimumSize           : QLayout.SizeConstraint = ... # 0x2
    #         SetFixedSize             : QLayout.SizeConstraint = ... # 0x3
    #         SetMaximumSize           : QLayout.SizeConstraint = ... # 0x4
    #         SetMinAndMaxSize         : QLayout.SizeConstraint = ... # 0x5

    def __init__(self, parent: Optional[PySide6.QtWidgets.QWidget] = None) -> None: ...

    #     def activate(self) -> bool: ...
    #     def addChildLayout(self, l: PySide6.QtWidgets.QLayout) -> None: ...
    #     def addChildWidget(self, w: PySide6.QtWidgets.QWidget) -> None: ...
    #     def addItem(self, arg__1: PySide6.QtWidgets.QLayoutItem) -> None: ...
    def addWidget(self, w: PySide6.QtWidgets.QWidget) -> None:
        """
        Adds the widget `w` to the layout.

        Args:
            w (PySide6.QtWidgets.QWidget): The widget to add to the layout.

        <br>
        """

    #     def adoptLayout(self, layout: PySide6.QtWidgets.QLayout) -> bool: ...
    #     def alignmentRect(self, arg__1: PySide6.QtCore.QRect) -> PySide6.QtCore.QRect: ...
    #     def childEvent(self, e: PySide6.QtCore.QChildEvent) -> None: ...
    #     @staticmethod
    #     def closestAcceptableSize(w: PySide6.QtWidgets.QWidget, s: PySide6.QtCore.QSize) -> PySide6.QtCore.QSize: ...
    #     def contentsMargins(self) -> PySide6.QtCore.QMargins: ...
    #     def contentsRect(self) -> PySide6.QtCore.QRect: ...
    #     def controlTypes(self) -> PySide6.QtWidgets.QSizePolicy.ControlType: ...
    #     def count(self) -> int: ...
    #     def expandingDirections(self) -> PySide6.QtCore.Qt.Orientation: ...
    #     def geometry(self) -> PySide6.QtCore.QRect: ...
    #     def getContentsMargins(self) -> object: ...
    #     @overload
    #     def indexOf(self, arg__1: PySide6.QtWidgets.QLayoutItem) -> int: ...
    #     @overload
    #     def indexOf(self, arg__1: PySide6.QtWidgets.QWidget) -> int: ...
    #     def invalidate(self) -> None: ...
    #     def isEmpty(self) -> bool: ...
    #     def isEnabled(self) -> bool: ...
    #     def itemAt(self, index: int) -> PySide6.QtWidgets.QLayoutItem: ...
    #     def layout(self) -> PySide6.QtWidgets.QLayout: ...
    #     def maximumSize(self) -> PySide6.QtCore.QSize: ...
    #     def menuBar(self) -> PySide6.QtWidgets.QWidget: ...
    #     def minimumSize(self) -> PySide6.QtCore.QSize: ...
    #     def parentWidget(self) -> PySide6.QtWidgets.QWidget: ...
    #     def removeItem(self, arg__1: PySide6.QtWidgets.QLayoutItem) -> None: ...
    #     def removeWidget(self, w: PySide6.QtWidgets.QWidget) -> None: ...
    #     def replaceWidget(self, from_: PySide6.QtWidgets.QWidget, to: PySide6.QtWidgets.QWidget, options: PySide6.QtCore.Qt.FindChildOption = ...) -> PySide6.QtWidgets.QLayoutItem: ...
    #     @overload
    #     def setAlignment(self, arg__1: PySide6.QtCore.Qt.AlignmentFlag) -> None: ...
    #     @overload
    #     def setAlignment(self, l: PySide6.QtWidgets.QLayout, alignment: PySide6.QtCore.Qt.AlignmentFlag) -> bool: ...
    #     @overload
    #     def setAlignment(self, w: PySide6.QtWidgets.QWidget, alignment: PySide6.QtCore.Qt.AlignmentFlag) -> bool: ...
    #     @overload
    #     def setContentsMargins(self, left: int, top: int, right: int, bottom: int) -> None: ...
    #     @overload
    #     def setContentsMargins(self, margins: PySide6.QtCore.QMargins) -> None: ...
    #     def setEnabled(self, arg__1: bool) -> None: ...
    #     def setGeometry(self, arg__1: PySide6.QtCore.QRect) -> None: ...
    #     def setMenuBar(self, w: PySide6.QtWidgets.QWidget) -> None: ...
    #     def setSizeConstraint(self, arg__1: PySide6.QtWidgets.QLayout.SizeConstraint) -> None: ...
    def setSpacing(self, space: int) -> None:
        """
        Sets the spacing between the items in the layout to `space`.

        Args:
            space (int): The spacing between the items in the layout.

        <br>
        """

    #     def sizeConstraint(self) -> PySide6.QtWidgets.QLayout.SizeConstraint: ...
    def spacing(self) -> int:
        """
        Gets the spacing between the items in the layout.

        Returns:
            The spacing between the items in the layout.

        <br>
        <br>
        """


#     def takeAt(self, index: int) -> PySide6.QtWidgets.QLayoutItem: ...
#     def totalHeightForWidth(self, w: int) -> int: ...
#     def totalMaximumSize(self) -> PySide6.QtCore.QSize: ...
#     def totalMinimumHeightForWidth(self, w: int) -> int: ...
#     def totalMinimumSize(self) -> PySide6.QtCore.QSize: ...
#     def totalSizeHint(self) -> PySide6.QtCore.QSize: ...
#     def unsetContentsMargins(self) -> None: ...
#     def update(self) -> None: ...
#     def widgetEvent(self, arg__1: PySide6.QtCore.QEvent) -> None: ...


class QApplication:
    """
    <hr>

    The <code>QApplication</code> class manages the GUI application's control flow and main settings.
    It is the starting point for the GUI application. Every GUI application must have exactly one
    instance of this class.

    <hr>

    <h3>Methods</h3>

    <ul>
        <li><a href="#code.QtWidgets.QApplication.exec"><code>exec</code></a></li>
    </ul>

    <br>

    **Examples**
    <hr>
    ``` py
    app = QtWidgets.QApplication()
    window = QtWidgets.QMainWindow()
    window.show()
    app.exec()
    ```
    In the above example, an instance of the `QApplication` class is created and
    a [`QMainWindow`](QMainWindow.md) is created and shown. The `exec` method is then called to start
    the application event loop. Running the above code will display an empty window.

    <hr>
    <br>
    """

    #     focusChanged             : ClassVar[Signal] = ... # focusChanged(QWidget*,QWidget*)

    #     @overload
    #     def __init__(self) -> None: ...
    @overload
    def __init__(self, arg__1: Sequence[str] = None) -> None: ...

    #     @staticmethod
    #     def aboutQt() -> None: ...
    #     @staticmethod
    #     def activeModalWidget() -> PySide6.QtWidgets.QWidget: ...
    #     @staticmethod
    #     def activePopupWidget() -> PySide6.QtWidgets.QWidget: ...
    #     @staticmethod
    #     def activeWindow() -> PySide6.QtWidgets.QWidget: ...
    #     @staticmethod
    #     def alert(widget: PySide6.QtWidgets.QWidget, duration: int = ...) -> None: ...
    #     @staticmethod
    #     def allWidgets() -> List[PySide6.QtWidgets.QWidget]: ...
    #     def autoSipEnabled(self) -> bool: ...
    #     @staticmethod
    #     def beep() -> None: ...
    #     @staticmethod
    #     def closeAllWindows() -> None: ...
    #     @staticmethod
    #     def cursorFlashTime() -> int: ...
    #     @staticmethod
    #     def doubleClickInterval() -> int: ...
    #     def event(self, arg__1: PySide6.QtCore.QEvent) -> bool: ...

    def exec() -> int:
        """
        Enters the main event loop and waits the application to finish. The event
        loop is quit when the last window is closed.

        Returns:
            The return code of the application.
        <br>
        <br>
        """

    #     def exec_(self) -> int: ...
    #     @staticmethod
    #     def focusWidget() -> PySide6.QtWidgets.QWidget: ...
    #     @overload
    #     @staticmethod
    #     def font() -> PySide6.QtGui.QFont: ...
    #     @overload
    #     @staticmethod
    #     def font(arg__1: PySide6.QtWidgets.QWidget) -> PySide6.QtGui.QFont: ...
    #     @overload
    #     @staticmethod
    #     def font(className: bytes) -> PySide6.QtGui.QFont: ...
    #     @staticmethod
    #     def fontMetrics() -> PySide6.QtGui.QFontMetrics: ...
    #     @staticmethod
    #     def isEffectEnabled(arg__1: PySide6.QtCore.Qt.UIEffect) -> bool: ...
    #     @staticmethod
    #     def keyboardInputInterval() -> int: ...
    #     def notify(self, arg__1: PySide6.QtCore.QObject, arg__2: PySide6.QtCore.QEvent) -> bool: ...
    #     @overload
    #     @staticmethod
    #     def palette() -> PySide6.QtGui.QPalette: ...
    #     @overload
    #     @staticmethod
    #     def palette(arg__1: PySide6.QtWidgets.QWidget) -> PySide6.QtGui.QPalette: ...
    #     @overload
    #     @staticmethod
    #     def palette(className: bytes) -> PySide6.QtGui.QPalette: ...
    #     def resolveInterface(self, name: bytes, revision: int) -> int: ...
    #     @staticmethod
    #     def setActiveWindow(act: PySide6.QtWidgets.QWidget) -> None: ...
    #     def setAutoSipEnabled(self, enabled: bool) -> None: ...
    #     @staticmethod
    #     def setCursorFlashTime(arg__1: int) -> None: ...
    #     @staticmethod
    #     def setDoubleClickInterval(arg__1: int) -> None: ...
    #     @staticmethod
    #     def setEffectEnabled(arg__1: PySide6.QtCore.Qt.UIEffect, enable: bool = ...) -> None: ...
    #     @staticmethod
    #     def setFont(arg__1: Union[PySide6.QtGui.QFont, str, Sequence[str]], className: Optional[bytes] = ...) -> None: ...
    #     @staticmethod
    #     def setKeyboardInputInterval(arg__1: int) -> None: ...
    #     @staticmethod
    #     def setPalette(arg__1: Union[PySide6.QtGui.QPalette, PySide6.QtCore.Qt.GlobalColor, PySide6.QtGui.QColor], className: Optional[bytes] = ...) -> None: ...
    #     @staticmethod
    #     def setStartDragDistance(l: int) -> None: ...
    #     @staticmethod
    #     def setStartDragTime(ms: int) -> None: ...
    #     @overload
    #     @staticmethod
    #     def setStyle(arg__1: PySide6.QtWidgets.QStyle) -> None: ...
    #     @overload
    #     @staticmethod
    #     def setStyle(arg__1: str) -> PySide6.QtWidgets.QStyle: ...
    #     def setStyleSheet(self, sheet: str) -> None: ...
    #     @staticmethod
    #     def setWheelScrollLines(arg__1: int) -> None: ...
    #     @staticmethod
    #     def startDragDistance() -> int: ...
    #     @staticmethod
    #     def startDragTime() -> int: ...
    #     @staticmethod
    #     def style() -> PySide6.QtWidgets.QStyle: ...
    #     def styleSheet(self) -> str: ...
    #     @overload
    #     @staticmethod
    #     def topLevelAt(p: PySide6.QtCore.QPoint) -> PySide6.QtWidgets.QWidget: ...
    #     @overload
    #     @staticmethod
    #     def topLevelAt(x: int, y: int) -> PySide6.QtWidgets.QWidget: ...
    #     @staticmethod
    #     def topLevelWidgets() -> List[PySide6.QtWidgets.QWidget]: ...
    #     @staticmethod
    #     def wheelScrollLines() -> int: ...
    #     @overload
    #     @staticmethod
    #     def widgetAt(p: PySide6.QtCore.QPoint) -> PySide6.QtWidgets.QWidget: ...
    #     @overload
    #     @staticmethod
    #     def widgetAt(x: int, y: int) -> PySide6.QtWidgets.QWidget: ...


class QMainWindow:
    """
    <hr>

    A main window provides a framework for building an application's user interface.
    Every user interface must have a `QMainWindow` in PySide6. A `QMainWindow` must have a central widget, which is the main widget in the window. The central widget
    can be a [`QWidget`](QWidget.md) or any other widget subclass.
    To this central widget, you can add other layouts, such as [`QHBoxLayout`](QHBoxLayout.md) and [`QVBoxLayout`](QVBoxLayout.md).

    <hr>

    <h3>Methods</h3>
    <ul>
        <li><a href="#code.QtWidgets.QMainWindow.setCentralWidget"><code>setCentralWidget</code></a></li>
        <li><a href="#code.QtWidgets.QMainWindow.show"><code>show</code></a></li>
    </ul>

    <br>

    **Examples**
        <hr>
        ``` py

        class UserInterface(QtWidgets.QMainWindow):
            def __init__(self):

                # Call the QMainWindow __init__ method.
                super().__init__()

                # Set the central widget; every QMainWindow must have a central widget.
                central_widget = QtWidgets.QWidget()
                self.setCentralWidget(QWidget())

                # Add a layout to the central widget.
                layout = QtWidgets.QVBoxLayout(central_widget)

        def main():

            # Create the application object.
            app = QtWidgets.QApplication()

            # Create the main window, show it, and start the event loop.
            window = UserInterface()
            window.show()
            app.exec()
        ```
        In the above example, a simple user interface is created using the `QMainWindow` class.
        We create a class called `UserInterface` that inherits from
        `QMainWindow`. We then call the `__init__` method of the `QMainWindow` class using
        the `super()` function. We then create a central widget and set it as the central
        widget of the main window and add a layout to the central widget.
        Finally, we create an instance of the `UserInterface` class, show the main window,
        and start the application event loop.
        <br>
        Running the `main` function in the above code will display a window with a vertical layout.

    <hr>

    <br>
    """

    # iconSizeChanged          : ClassVar[Signal] = ... # iconSizeChanged(QSize)
    # tabifiedDockWidgetActivated: ClassVar[Signal] = ... # tabifiedDockWidgetActivated(QDockWidget*)
    # toolButtonStyleChanged   : ClassVar[Signal] = ... # toolButtonStyleChanged(Qt::ToolButtonStyle)

    # class DockOption(enum.Flag):

    #     AnimatedDocks            : QMainWindow.DockOption = ... # 0x1
    #     AllowNestedDocks         : QMainWindow.DockOption = ... # 0x2
    #     AllowTabbedDocks         : QMainWindow.DockOption = ... # 0x4
    #     ForceTabbedDocks         : QMainWindow.DockOption = ... # 0x8
    #     VerticalTabs             : QMainWindow.DockOption = ... # 0x10
    #     GroupedDragging          : QMainWindow.DockOption = ... # 0x20

    # def __init__(self, parent: Optional[PySide6.QtWidgets.QWidget] = ..., flags: PySide6.QtCore.Qt.WindowType = ...) -> None: ...

    # @overload
    # def addDockWidget(self, area: PySide6.QtCore.Qt.DockWidgetArea, dockwidget: PySide6.QtWidgets.QDockWidget) -> None: ...
    # @overload
    # def addDockWidget(self, area: PySide6.QtCore.Qt.DockWidgetArea, dockwidget: PySide6.QtWidgets.QDockWidget, orientation: PySide6.QtCore.Qt.Orientation) -> None: ...
    # @overload
    # def addToolBar(self, area: PySide6.QtCore.Qt.ToolBarArea, toolbar: PySide6.QtWidgets.QToolBar) -> None: ...
    # @overload
    # def addToolBar(self, title: str) -> PySide6.QtWidgets.QToolBar: ...
    # @overload
    # def addToolBar(self, toolbar: PySide6.QtWidgets.QToolBar) -> None: ...
    # def addToolBarBreak(self, area: PySide6.QtCore.Qt.ToolBarArea = ...) -> None: ...
    # def centralWidget(self) -> PySide6.QtWidgets.QWidget: ...
    # def contextMenuEvent(self, event: PySide6.QtGui.QContextMenuEvent) -> None: ...
    # def corner(self, corner: PySide6.QtCore.Qt.Corner) -> PySide6.QtCore.Qt.DockWidgetArea: ...
    # def createPopupMenu(self) -> PySide6.QtWidgets.QMenu: ...
    # def dockOptions(self) -> PySide6.QtWidgets.QMainWindow.DockOption: ...
    # def dockWidgetArea(self, dockwidget: PySide6.QtWidgets.QDockWidget) -> PySide6.QtCore.Qt.DockWidgetArea: ...
    # def documentMode(self) -> bool: ...
    # def event(self, event: PySide6.QtCore.QEvent) -> bool: ...
    # def iconSize(self) -> PySide6.QtCore.QSize: ...
    # def insertToolBar(self, before: PySide6.QtWidgets.QToolBar, toolbar: PySide6.QtWidgets.QToolBar) -> None: ...
    # def insertToolBarBreak(self, before: PySide6.QtWidgets.QToolBar) -> None: ...
    # def isAnimated(self) -> bool: ...
    # def isDockNestingEnabled(self) -> bool: ...
    # def isSeparator(self, pos: PySide6.QtCore.QPoint) -> bool: ...
    # def menuBar(self) -> PySide6.QtWidgets.QMenuBar: ...
    # def menuWidget(self) -> PySide6.QtWidgets.QWidget: ...
    # def removeDockWidget(self, dockwidget: PySide6.QtWidgets.QDockWidget) -> None: ...
    # def removeToolBar(self, toolbar: PySide6.QtWidgets.QToolBar) -> None: ...
    # def removeToolBarBreak(self, before: PySide6.QtWidgets.QToolBar) -> None: ...
    # def resizeDocks(self, docks: Sequence[PySide6.QtWidgets.QDockWidget], sizes: Sequence[int], orientation: PySide6.QtCore.Qt.Orientation) -> None: ...
    # def restoreDockWidget(self, dockwidget: PySide6.QtWidgets.QDockWidget) -> bool: ...
    # def restoreState(self, state: Union[PySide6.QtCore.QByteArray, bytes], version: int = ...) -> bool: ...
    # def saveState(self, version: int = ...) -> PySide6.QtCore.QByteArray: ...
    # def setAnimated(self, enabled: bool) -> None: ...
    def setCentralWidget(self, widget: PySide6.QtWidgets.QWidget) -> None:
        """
        Sets the given widget to be the main window's central widget.

        Args:
            widget (PySide6.QtWidgets.QWidget): The widget to set as the central widget.

        <br>
        """

    def show(self) -> None:
        """
        Shows the main window.

        <br>
        <br>
        """

    # def setCorner(self, corner: PySide6.QtCore.Qt.Corner, area: PySide6.QtCore.Qt.DockWidgetArea) -> None: ...
    # def setDockNestingEnabled(self, enabled: bool) -> None: ...
    # def setDockOptions(self, options: PySide6.QtWidgets.QMainWindow.DockOption) -> None: ...
    # def setDocumentMode(self, enabled: bool) -> None: ...
    # def setIconSize(self, iconSize: PySide6.QtCore.QSize) -> None: ...
    # def setMenuBar(self, menubar: PySide6.QtWidgets.QMenuBar) -> None: ...
    # def setMenuWidget(self, menubar: PySide6.QtWidgets.QWidget) -> None: ...
    # def setStatusBar(self, statusbar: PySide6.QtWidgets.QStatusBar) -> None: ...
    # def setTabPosition(self, areas: PySide6.QtCore.Qt.DockWidgetArea, tabPosition: PySide6.QtWidgets.QTabWidget.TabPosition) -> None: ...
    # def setTabShape(s_summary_elf, tabShape: PySide6.QtWidgets.QTabWidget.TabShape) -> None: ...
    # def setToolButtonStyle(self, toolButtonStyle: PySide6.QtCore.Qt.ToolButtonStyle) -> None: ...
    # def setUnifiedTitleAndToolBarOnMac(self, set: bool) -> None: ...
    # def splitDockWidget(self, after: PySide6.QtWidgets.QDockWidget, dockwidget: PySide6.QtWidgets.QDockWidget, orientation: PySide6.QtCore.Qt.Orientation) -> None: ...
    # def statusBar(self) -> PySide6.QtWidgets.QStatusBar: ...
    # def tabPosition(self, area: PySide6.QtCore.Qt.DockWidgetArea) -> PySide6.QtWidgets.QTabWidget.TabPosition: ...
    # def tabShape(self) -> PySide6.QtWidgets.QTabWidget.TabShape: ...
    # def tabifiedDockWidgets(self, dockwidget: PySide6.QtWidgets.QDockWidget) -> List[PySide6.QtWidgets.QDockWidget]: ...
    # def tabifyDockWidget(self, first: PySide6.QtWidgets.QDockWidget, second: PySide6.QtWidgets.QDockWidget) -> None: ...
    # def takeCentralWidget(self) -> PySide6.QtWidgets.QWidget: ...
    # def toolBarArea(self, toolbar: PySide6.QtWidgets.QToolBar) -> PySide6.QtCore.Qt.ToolBarArea: ...
    # def toolBarBreak(self, toolbar: PySide6.QtWidgets.QToolBar) -> bool: ...
    # def toolButtonStyle(self) -> PySide6.QtCore.Qt.ToolButtonStyle: ...
    # def unifiedTitleAndToolBarOnMac(self) -> bool: ...


class QHBoxLayout:
    """
    <hr>
    The <code>QHBoxLayout</code> class lines up widgets horizontally. If the widgets do not fit
    in the window, the layout will automatically wrap or resize them. For a vertical
    layout, use [`QVBoxLayout`](QVBoxLayout.md).
    <hr>

    <h3>Methods</h3>
    <ul>
        <li><a href="#code.QtWidgets.QHBoxLayout.addLayout"><code>addLayout</code></a></li>
    </ul>

    <br>

    **Examples**
    <hr>
    ``` py
    layout = QtWidgets.QHBoxLayout()
    layout.addWidget(QPushButton("Button 1"))
    layout.addWidget(QPushButton("Button 2"))
    ```
    In the above example, a horizontal layout is created, and two buttons are added to it
    using the `addWidget` method from the parent [`QLayout`](QLayout.md) parent class. The buttons will be aligned horizontally.

    <br>

    ``` py
    h_layout = QtWidgets.QHBoxLayout()
    v_layout = QtWidgets.QVBoxLayout()
    h_layout.addLayout(v_layout)
    ```
    In the above example, a horizontal layout is created, added to a central
    widget, and a vertical layout is added to it.
    <hr>

    <br>
    """

    def __init__(self, parent: Optional[PySide6.QtWidgets.QWidget] = None) -> None: ...

    def addLayout(self, layout: PySide6.QtWidgets.QLayout) -> None:
        """Adds a layout to the horizontal box layout. The layout will be added to the right of the existing layouts.

        Args:
            layout (PySide6.QtWidgets.QLayout): the layout to add.
        <br>
        <br>
        """

    # @overload
    # def __init__(self) -> None: ...
    # @overload
    # def __init__(self, parent: PySide6.QtWidgets.QWidget) -> None: ...


class QVBoxLayout:
    """
    <hr>
    The <code>QVBoxLayout</code> class lines up widgets vertically. If the widgets do not fit
    in the window, the layout will automatically wrap or resize them. For a horizontal
    layout, see [`QHBoxLayout`](QHBoxLayout.md).

    <hr>


    <h3>Methods</h3>
    <ul>
        <li><a href="#code.QtWidgets.QVBoxLayout.addLayout"><code>addLayout</code></a></li>
    </ul>

    <br>

    **Examples**
    <hr>
    ``` py
    vbox = QtWidgets.QVBoxLayout()
    textedit = QtWidgets.QTextEdit()
    vbox.addWidget(textedit)
    ```
    In the above example, a vertical layout is created and a [`QTextEdit`](QTextEdit.md) widget is added to it using the `addWidget` method from the parent class [`QLayout`](QLayout.md).

    <br>

    ``` py
    vbox = QtWidgets.QVBoxLayout()
    hbox = QtWidgets.QHBoxLayout()
    vbox.addLayout(hbox)
    ```
    In the above example, a vertical layout is created and a horizontal layout is added to it.
    <hr>

    <br>
    """

    def __init__(self, parent: Optional[PySide6.QtWidgets.QWidget] = None) -> None: ...

    def addLayout(self, layout: PySide6.QtWidgets.QLayout) -> None:
        """Adds a layout to the vertical box layout. The layout will be added below the existing layouts.

        Args:
            layout (PySide6.QtWidgets.QLayout): the layout to add
        <br>
        <br>
        """

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, parent: PySide6.QtWidgets.QWidget) -> None: ...


class QFormLayout:
    """
    <hr>

    ![](layouts/form_layout.png)

    `QFormLayout` is a layout manager that arranges widgets in a two-column layout. The left column
    contains labels, and the right column contains widgets. This layout can also be achieved using
    [`QGridLayout`](QGridLayout.md) but `QFormLayout` provides a more convenient way to create
    form-like layouts.

    <hr>

    <h3>Methods</h3>
    <ul>
        <li><a href="#code.QtWidgets.QFormLayout.addRow"><code>addRow</code></a></li>
        <li><a href="#code.QtWidgets.QFormLayout.horizontalSpacing"><code>horizontalSpacing</code></a></li>
        <li><a href="#code.QtWidgets.QFormLayout.sethorizontalSpacing"><code>setHorizontalSpacing</code></a></li>
        <li><a href="#code.QtWidgets.QFormLayout.verticalSpacing"><code>verticalSpacing</code></a></li>
        <li><a href="#code.QtWidgets.QFormLayout.setVerticalSpacing"><code>setVerticalSpacing</code></a></li>
        <li><a href="#code.QtWidgets.QFormLayout.removeRow"><code>removeRow</code></a></li>
        <li><a href="#code.QtWidgets.QFormLayout.rowCount"><code>rowCount</code></a></li>
    </ul>

    <br>

    **Examples**
    <hr>
    ``` py
    layout = QtWidgets.QFormLayout()
    label = QtWidgets.QLabel("Name:")
    line_edit = QtWidgets.QLineEdit()
    layout.addRow(label, line_edit)

    print(layout.rowCount())
    ```
    `1`
    ```py
    spin_box = QtWidgets.QSpinBox()
    layout.addRow("age", spinbox)

    layout.removeRow(0)
    print(layout.rowCount())
    ```
    `1`
    <hr>
    <br>

    """

    # class FieldGrowthPolicy(enum.Enum):

    #     FieldsStayAtSizeHint: QFormLayout.FieldGrowthPolicy = ...  # 0x0
    #     ExpandingFieldsGrow: QFormLayout.FieldGrowthPolicy = ...  # 0x1
    #     AllNonFixedFieldsGrow: QFormLayout.FieldGrowthPolicy = ...  # 0x2

    # class ItemRole(enum.Enum):

    #     LabelRole: QFormLayout.ItemRole = ...  # 0x0
    #     FieldRole: QFormLayout.ItemRole = ...  # 0x1
    #     SpanningRole: QFormLayout.ItemRole = ...  # 0x2

    # class RowWrapPolicy(enum.Enum):

    #     DontWrapRows: QFormLayout.RowWrapPolicy = ...  # 0x0
    #     WrapLongRows: QFormLayout.RowWrapPolicy = ...  # 0x1
    #     WrapAllRows: QFormLayout.RowWrapPolicy = ...  # 0x2

    # class TakeRowResult(Shiboken.Object):
    #     @overload
    #     def __init__(self) -> None: ...
    #     @overload
    #     def __init__(
    #         self, TakeRowResult: PySide6.QtWidgets.QFormLayout.TakeRowResult
    #     ) -> None: ...
    #     @staticmethod
    #     def __copy__() -> None: ...

    def __init__(self, parent: Optional[PySide6.QtWidgets.QWidget] = None) -> None: ...

    # def addItem(self, item: PySide6.QtWidgets.QLayoutItem) -> None: ...
    def addRow(
        self,
        label: PySide6.QtWidgets.QWidget | str,
        field: PySide6.QtWidgets.QLayout | PySide6.QtWidgets.QWidget,
    ) -> None:
        """
        Add a row to the form layout with a label and a field. The label can be a string or a widget.
        The field can be a widget or a layout.

        Args:
            label (PySide6.QtWidgets.QWidget | str): The label for the field.
            field (PySide6.QtWidgets.QLayout | PySide6.QtWidgets.QWidget): The field to add.

        <br>
        """

    # def count(self) -> int: ...
    # def expandingDirections(self) -> PySide6.QtCore.Qt.Orientation: ...
    # def fieldGrowthPolicy(self) -> PySide6.QtWidgets.QFormLayout.FieldGrowthPolicy: ...
    # def formAlignment(self) -> PySide6.QtCore.Qt.AlignmentFlag: ...
    # def getItemPosition(self, index: int) -> object: ...
    # def getLayoutPosition(self, layout: PySide6.QtWidgets.QLayout) -> object: ...
    # def getWidgetPosition(self, widget: PySide6.QtWidgets.QWidget) -> object: ...
    # def hasHeightForWidth(self) -> bool: ...
    # def heightForWidth(self, width: int) -> int: ...
    def horizontalSpacing(self) -> int:
        """
        Get the horizontal spacing between the items in the layout.

        Returns:
            The horizontal spacing between the items in the layout.

        <br>
        """

    # @overload
    # def insertRow(self, row: int, label: PySide6.QtWidgets.QWidget, field: PySide6.QtWidgets.QLayout) -> None: ...
    # @overload
    # def insertRow(self, row: int, label: PySide6.QtWidgets.QWidget, field: PySide6.QtWidgets.QWidget) -> None: ...
    # @overload
    # def insertRow(self, row: int, labelText: str, field: PySide6.QtWidgets.QLayout) -> None: ...
    # @overload
    # def insertRow(self, row: int, labelText: str, field: PySide6.QtWidgets.QWidget) -> None: ...
    # @overload
    # def insertRow(self, row: int, layout: PySide6.QtWidgets.QLayout) -> None: ...
    # @overload
    # def insertRow(self, row: int, widget: PySide6.QtWidgets.QWidget) -> None: ...
    # def invalidate(self) -> None: ...
    # @overload
    # def isRowVisible(self, layout: PySide6.QtWidgets.QLayout) -> bool: ...
    # @overload
    # def isRowVisible(self, row: int) -> bool: ...
    # @overload
    # def isRowVisible(self, widget: PySide6.QtWidgets.QWidget) -> bool: ...
    # @overload
    # def itemAt(self, index: int) -> PySide6.QtWidgets.QLayoutItem: ...
    # @overload
    # def itemAt(self, row: int, role: PySide6.QtWidgets.QFormLayout.ItemRole) -> PySide6.QtWidgets.QLayoutItem: ...
    # def labelAlignment(self) -> PySide6.QtCore.Qt.AlignmentFlag: ...
    # @overload
    # def labelForField(self, field: PySide6.QtWidgets.QLayout) -> PySide6.QtWidgets.QWidget: ...
    # @overload
    # def labelForField(self, field: PySide6.QtWidgets.QWidget) -> PySide6.QtWidgets.QWidget: ...
    # def minimumSize(self) -> PySide6.QtCore.QSize: ...
    # @overload
    def removeRow(
        self, row: int | PySide6.QtWidgets.QWidget | PySide6.QtWidgets.QLayout
    ) -> None:
        """
        Remove the row from the layout. The row can be specified by the row number, the widget, or the layout.

        Args:
            row (int | PySide6.QtWidgets.QWidget | PySide6.QtWidgets.QLayout): The row to remove.

        <br>
        """

    # @overload
    # def removeRow(self, row: int) -> None: ...
    # @overload
    # def removeRow(self, widget: PySide6.QtWidgets.QWidget) -> None: ...

    def rowCount(self) -> int:
        """
        Get the number of rows in the layout.

        Returns:
            The number of rows in the layout.

        <br>
        """

    # def rowWrapPolicy(self) -> PySide6.QtWidgets.QFormLayout.RowWrapPolicy: ...
    # def setFieldGrowthPolicy(self, policy: PySide6.QtWidgets.QFormLayout.FieldGrowthPolicy) -> None: ...
    # def setFormAlignment(self, alignment: PySide6.QtCore.Qt.AlignmentFlag) -> None: ...
    # def setGeometry(self, rect: PySide6.QtCore.QRect) -> None: ...
    def setHorizontalSpacing(self, spacing: int) -> None:
        """
        Set the horizontal spacing between the items in the layout.

        Args:
            spacing (int): The horizontal spacing between the items in the layout.

        <br>
        """

    # def setItem(self, row: int, role: PySide6.QtWidgets.QFormLayout.ItemRole, item: PySide6.QtWidgets.QLayoutItem) -> None: ...
    # def setLabelAlignment(self, alignment: PySide6.QtCore.Qt.AlignmentFlag) -> None: ...
    # def setLayout(self, row: int, role: PySide6.QtWidgets.QFormLayout.ItemRole, layout: PySide6.QtWidgets.QLayout) -> None: ...
    # @overload
    # def setRowVisible(self, layout: PySide6.QtWidgets.QLayout, on: bool) -> None: ...
    # @overload
    # def setRowVisible(self, row: int, on: bool) -> None: ...
    # @overload
    # def setRowVisible(self, widget: PySide6.QtWidgets.QWidget, on: bool) -> None: ...
    # def setRowWrapPolicy(self, policy: PySide6.QtWidgets.QFormLayout.RowWrapPolicy) -> None: ...
    # def setSpacing(self, arg__1: int) -> None: ...
    def setVerticalSpacing(self, spacing: int) -> None:
        """
        Set the vertical spacing between the items in the layout.

        Args:
            spacing (int): The vertical spacing between the items in the layout.

        <br>
        """

    # def setWidget(self, row: int, role: PySide6.QtWidgets.QFormLayout.ItemRole, widget: PySide6.QtWidgets.QWidget) -> None: ...
    # def sizeHint(self) -> PySide6.QtCore.QSize: ...
    # def spacing(self) -> int: ...
    # def takeAt(self, index: int) -> PySide6.QtWidgets.QLayoutItem: ...
    # @overload
    # def takeRow(self, layout: PySide6.QtWidgets.QLayout) -> PySide6.QtWidgets.QFormLayout.TakeRowResult: ...
    # @overload
    # def takeRow(self, row: int) -> PySide6.QtWidgets.QFormLayout.TakeRowResult: ...
    # @overload
    # def takeRow(self, widget: PySide6.QtWidgets.QWidget) -> PySide6.QtWidgets.QFormLayout.TakeRowResult: ...
    def verticalSpacing(self) -> int:
        """
        Get the vertical spacing between the items in the layout.

        Returns:
            The vertical spacing between the items in the layout.

        <br>
        <br>
        """


class QGridLayout:
    """
    <hr>

    ![](layouts/grid_layout.png)

    The `QGridLayout` class lays out widgets in a grid, which has a variable number of rows and columns. The grid layout is used
    to create a more complex layout than the [`QHBoxLayout`](QHBoxLayout.md) and [`QVBoxLayout`](QVBoxLayout.md) classes,
    which only allow for horizontal and vertical layouts, respectively.

    <hr>

    <h3>Methods</h3>
    <ul>
        <li><a href="#code.QtWidgets.QGridLayout.addLayout"><code>addLayout</code></a></li>
        <li><a href="#code.QtWidgets.QGridLayout.addWidget"><code>addWidget</code></a></li>
        <li><a href="#code.QtWidgets.QGridLayout.columnCount"><code>columnCount</code></a></li>
        <li><a href="#code.QtWidgets.QGridLayout.rowCount"><code>rowCount</code></a></li>
        <li><a href="#code.QtWidgets.QGridLayout.setHorizontalSpacing"><code>setHorizontalSpacing</code></a></li>
        <li><a href="#code.QtWidgets.QGridLayout.setVerticalSpacing"><code>setVerticalSpacing</code></a></li>
        <li><a href="#code.QtWidgets.QGridLayout.setColumnMinimumWidth"><code>setColumnMinimumWidth</code></a></li>
        <li><a href="#code.QtWidgets.QGridLayout.setRowMinimumHeight"><code>setRowMinimumHeight</code></a></li>
        <li><a href="#code.QtWidgets.QGridLayout.setColumnStretch"><code>setColumnStretch</code></a></li>
        <li><a href="#code.QtWidgets.QGridLayout.setRowStretch"><code>setRowStretch</code></a></li>
        <li><a href="#code.QtWidgets.QGridLayout.horizontalSpacing"><code>horizontalSpacing</code></a></li>
        <li><a href="#code.QtWidgets.QGridLayout.verticalSpacing"><code>verticalSpacing</code></a></li>
        <li><a href="#code.QtWidgets.QGridLayout.columnMinimumWidth"><code>columnMinimumWidth</code></a></li>
        <li><a href="#code.QtWidgets.QGridLayout.rowMinimumHeight"><code>rowMinimumHeight</code></a></li>
        <li><a href="#code.QtWidgets.QGridLayout.columnStretch"><code>columnStretch</code></a></li>
        <li><a href="#code.QtWidgets.QGridLayout.rowStretch"><code>rowStretch</code></a></li>

    </ul>

    <br>

    **Examples**
    <hr>
    ```py
    layout = QtWidgets.QGridLayout()
    layout.setHorizontalSpacing(10)
    layout.setVerticalSpacing(10)

    print(layout.horizontalSpacing(), layout.verticalSpacing())
    ```
    `10 10`
    ```py
    layout.addWidget(QPushButton("Button 1"), 0, 0)
    layout.addWidget(QPushButton("Button 2"), 0, 1)
    layout.addWidget(QPushButton("Button 3"), 1, 0)
    layout.addWidget(QPushButton("Button 4"), 1, 1)

    print(layout.columnCount(), layout.rowCount())
    ```
    `2 2`

    <hr>

    <br>
    """

    def __init__(self, parent: Optional[PySide6.QtWidgets.QWidget] = None) -> None: ...

    #     @overload
    #     def addItem(self, arg__1: PySide6.QtWidgets.QLayoutItem) -> None: ...
    #     @overload
    #     def addItem(self, item: PySide6.QtWidgets.QLayoutItem, row: int, column: int, rowSpan: int = ..., columnSpan: int = ..., alignment: PySide6.QtCore.Qt.AlignmentFlag = ...) -> None: ...

    def addLayout(
        self, layout: PySide6.QtWidgets.QLayout, row: int, column: int
    ) -> None:
        """
        Add a layout to the grid layout at the specified row and column.

        Args:
            layout (PySide6.QtWidgets.QLayout): The layout to add.
            row (int): The row to add the layout to.
            column (int): The column to add the layout to.

        <br>
        """

    def addWidget(
        self,
        widget: PySide6.QtWidgets.QWidget,
        row: int,
        column: int,
    ) -> None:
        """
        Add a widget to the grid layout at the specified row and column.

        Args:
            widget (PySide6.QtWidgets.QWidget): The widget to add.
            row (int): The row to add the widget to.
            column (int): The column to add the widget to.

        <br>
        """

    #     @overload
    #     def addWidget(self, w: PySide6.QtWidgets.QWidget) -> None: ...
    #     def cellRect(self, row: int, column: int) -> PySide6.QtCore.QRect: ...
    def columnCount(self) -> int:
        """
        Get the number of columns in the grid layout.

        Returns:
            int: The number of columns in the grid layout.

        <br>
        """

    def columnMinimumWidth(self, column: int) -> int:
        """
        Get the minimum width of the specified column in the grid layout.

        Args:
            column (int): The column to get the minimum width of.

        Returns:
            The minimum width of the specified column in the grid layout.

        <br>
        """

    def columnStretch(self, column: int) -> int:
        """
        Get the stretch factor of the specified column in the grid layout.

        Args:
            column (int): The column to get the stretch factor of.

        Returns:
            int: The stretch factor of the specified column in the grid layout.
        <br>
        """

    #     def count(self) -> int: ...
    #     def expandingDirections(self) -> PySide6.QtCore.Qt.Orientation: ...
    #     def getItemPosition(self, idx: int) -> object: ...
    #     def hasHeightForWidth(self) -> bool: ...
    #     def heightForWidth(self, arg__1: int) -> int: ...
    def horizontalSpacing(self) -> int:
        """
        Get the horizontal spacing between items in the grid layout.

        Returns:
            int: The horizontal spacing between items in the grid layout.

        <br>
        """

    #     def invalidate(self) -> None: ...
    #     def itemAt(self, index: int) -> PySide6.QtWidgets.QLayoutItem: ...
    #     def itemAtPosition(self, row: int, column: int) -> PySide6.QtWidgets.QLayoutItem: ...
    #     def maximumSize(self) -> PySide6.QtCore.QSize: ...
    #     def minimumHeightForWidth(self, arg__1: int) -> int: ...
    #     def minimumSize(self) -> PySide6.QtCore.QSize: ...
    #     def originCorner(self) -> PySide6.QtCore.Qt.Corner: ...
    def rowCount(self) -> int:
        """
        Get the number of rows in the grid layout.

        Returns:
            int: The number of rows in the grid layout.

        <br>
        """

    def rowMinimumHeight(self, row: int) -> int:
        """
        Get the minimum height of the specified row in the grid layout.

        Args:
            row (int): The row to get the minimum height of.

        Returns:
            int: The minimum height of the specified row in the grid layout.

        <br>
        """

    def rowStretch(self, row: int) -> int:
        """
        Get the stretch factor of the specified row in the grid layout.

        Args:
            row (int): The row to get the stretch factor of.

        Returns:
            int: The stretch factor of the specified row in the grid layout.

        <br>
        """

    def setColumnMinimumWidth(self, column: int, minSize: int) -> None:
        """
        Set the minimum width of the specified column in the grid layout.

        Args:
            column (int): The column to set the minimum width of.
            minSize (int): The minimum width of the specified column.

        <br>
        """

    def setColumnStretch(self, column: int, stretch: int) -> None:
        """
        Set the stretch factor of the specified column in the grid layout.

        Args:
            column (int): The column to set the stretch factor of.
            stretch (int): The stretch factor of the specified column.

        <br>
        """

    #     def setDefaultPositioning(self, n: int, orient: PySide6.QtCore.Qt.Orientation) -> None: ...
    #     def setGeometry(self, arg__1: PySide6.QtCore.QRect) -> None: ...
    def setHorizontalSpacing(self, spacing: int) -> None:
        """
        Set the horizontal spacing between items in the grid layout.

        Args:
            spacing (int): The horizontal spacing between items in the grid layout.

        <br>
        """

    #     def setOriginCorner(self, arg__1: PySide6.QtCore.Qt.Corner) -> None: ...
    def setRowMinimumHeight(self, row: int, minSize: int) -> None:
        """
        Set the minimum height of the specified row in the grid layout.

        Args:
            row (int): The row to set the minimum height of.
            minSize (int): The minimum height of the specified row.

        <br>
        """

    def setRowStretch(self, row: int, stretch: int) -> None:
        """
        Set the stretch factor of the specified row in the grid layout.

        Args:
            row (int): The row to set the stretch factor of.
            stretch (int): The stretch factor of the specified row.

        <br>
        """

    #     def setSpacing(self, spacing: int) -> None:

    def setVerticalSpacing(self, spacing: int) -> None:
        """
        Set the vertical spacing between items in the grid layout.

        Args:
            spacing (int): The vertical spacing between items in the grid layout.

        <br>
        """

    #     def sizeHint(self) -> PySide6.QtCore.QSize: ...
    #     def takeAt(self, index: int) -> PySide6.QtWidgets.QLayoutItem: ...
    def verticalSpacing(self) -> int:
        """
        Get the vertical spacing between items in the grid layout.

        Returns:
            int: The vertical spacing between items in the grid layout.

        <br>
        <br>
        """


class QGroupBox:
    """
    <hr>

    ![](layouts/group_box.png)

    `QGroupBox` is a widget that groups other widgets together. It provides a title and a frame around the widgets it contains.

    Args:
        title (str): The title of the group box.

    <hr>

    <h3>Signals</h3>
    <ul>
        <li><code>clicked</code>: Emitted when the group box is clicked.</li>
    </ul>


    <h3>Methods</h3>
    <ul>
        <li><a href="#code.QtWidgets.QGroupBox.setTitle"><code>setTitle</code></a></li>
        <li><a href="#code.QtWidgets.QGroupBox.title"><code>title</code></a></li>
    </ul>

    <br>

    **Examples**
        <hr>
        ``` py
        group_box = QtWidgets.QGroupBox("Group Box")
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(QPushButton("Button 1"))
        layout.addWidget(QPushButton("Button 2"))

        group_box.setLayout(layout)
        ```
        Running the above code will create a group box with the title "Group Box" and two buttons aligned vertically inside it.
        Note that the layout is set using the `setLayout` method from the parent [`QWidget`](QWidget.md) class.
        <hr>

    <br>
    """

    ...
    # clicked                  : ClassVar[Signal] = ... # clicked()
    # toggled                  : ClassVar[Signal] = ... # toggled(bool)

    # @overload
    # def __init__(self, parent: Optional[PySide6.QtWidgets.QWidget] = ...) -> None: ...

    def __init__(self, title: str = None) -> None: ...

    # def alignment(self) -> PySide6.QtCore.Qt.AlignmentFlag: ...
    # def changeEvent(self, event: PySide6.QtCore.QEvent) -> None: ...
    # def childEvent(self, event: PySide6.QtCore.QChildEvent) -> None: ...
    # def event(self, event: PySide6.QtCore.QEvent) -> bool: ...
    # def focusInEvent(self, event: PySide6.QtGui.QFocusEvent) -> None: ...
    # def initStyleOption(self, option: PySide6.QtWidgets.QStyleOptionGroupBox) -> None: ...
    # def isCheckable(self) -> bool: ...
    # def isChecked(self) -> bool: ...
    # def isFlat(self) -> bool: ...
    # def minimumSizeHint(self) -> PySide6.QtCore.QSize: ...
    # def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    # def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    # def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    # def paintEvent(self, event: PySide6.QtGui.QPaintEvent) -> None: ...
    # def resizeEvent(self, event: PySide6.QtGui.QResizeEvent) -> None: ...
    # def setAlignment(self, alignment: int) -> None: ...
    # def setCheckable(self, checkable: bool) -> None: ...
    # def setChecked(self, checked: bool) -> None: ...
    # def setFlat(self, flat: bool) -> None: ...
    def setTitle(self, title: str) -> None:
        """
        Set the title of the group box.

        Args:
            title (str): The title of the group box.

        <br>
        """

    def title(self) -> str:
        """
        Get the title of the group box.

        Returns:
            str: The title of the group box.

        <br>
        <br>
        """


class QTextEdit:
    """
    <hr>
    ![QTextEdit](buttons/text_edit.png)

    `QTextEdit` is an advanced text editor that provides a rich text display and editing features.
    It can be used to display and edit formatted text, such as HTML and Markdown.
    <hr>

    <h3>Signals</h3>
    <ul>
        <li><code>cursorPositionChanged</code>: Emitted when the cursor position changes.</li>
        <li><code>textChanged</code>: Emitted when the text changes.</li>
    </ul>

    <h3>Methods</h3>
    <ul>
        <li><a href="#code.QtWidgets.QTextEdit.clear"><code>clear</code></a></li>
        <li><a href="#code.QtWidgets.QTextEdit.copy"><code>copy</code></a></li>
        <li><a href="#code.QtWidgets.QTextEdit.paste"><code>paste</code></a></li>
        <li><a href="#code.QtWidgets.QTextEdit.redo"><code>redo</code></a></li>
        <li><a href="#code.QtWidgets.QTextEdit.undo"><code>undo</code></a></li>
        <li><a href="#code.QtWidgets.QTextEdit.cut"><code>cut</code></a></li>
        <li><a href="#code.QtWidgets.QTextEdit.append"><code>append</code></a></li>
        <li><a href="#code.QtWidgets.QTextEdit.setPlaceholderText"><code>setPlaceholderText</code></a></li>
        <li><a href="#code.QtWidgets.QTextEdit.placeholderText"><code>placeholderText</code></a></li>
        <li><a href="#code.QtWidgets.QTextEdit.setReadOnly"><code>setReadOnly</code></a></li>
        <li><a href="#code.QtWidgets.QTextEdit.isReadOnly"><code>isReadOnly</code></a></li>
        <li><a href="#code.QtWidgets.QTextEdit.setFontItalic"><code>setFontItalic</code></a></li>
        <li><a href="#code.QtWidgets.QTextEdit.setFontUnderline"><code>setFontUnderline</code></a></li>
        <li><a href="#code.QtWidgets.QTextEdit.setFontWeight"><code>setFontWeight</code></a></li>
        <li><a href="#code.QtWidgets.QTextEdit.setFontPointSize"><code>setFontPointSize</code></a></li>
        <li><a href="#code.QtWidgets.QTextEdit.setText"><code>setText</code></a></li>
        <li><a href="#code.QtWidgets.QTextEdit.setHtml"><code>toHtml</code></a></li>
        <li><a href="#code.QtWidgets.QTextEdit.setMarkdown"><code>setMarkdown</code></a></li>
        <li><a href="#code.QtWidgets.QTextEdit.toPlainText"><code>toPlainText</code></a></li>
        <li><a href="#code.QtWidgets.QTextEdit.toHtml"><code>toHtml</code></a></li>
        <li><a href="#code.QtWidgets.QTextEdit.toMarkdown"><code>toMarkdown</code></a></li>
        <li><a href="#code.QtWidgets.QTextEdit.zoomIn"><code>zoomIn</code></a></li>
        <li><a href="#code.QtWidgets.QTextEdit.zoomOut"><code>zoomOut</code></a></li>
    </ul>

    <br>

    **Examples**
    <hr>
    ``` py
    text_edit = QtWidgets.QTextEdit()
    text_edit.setHtml("<b>Hello, World!</b>")

    print(text_edit.toPlainText())
    print(text_edit.toHtml())
    ```
    `Hello, World!` <br>
    `<b>Hello, World!</b>`
    ``` py
    text_edit.setMarkdown("**Hello, World!**")

    print(text_edit.toPlainText())
    print(text_edit.Markdown())
    ```
    `Hello, World!` <br>
    `**Hello, World!**` <br> <br>
    The above code shows how to set the text of a `QTextEdit` widget using HTML and Markdown and how to get the text in plain text, HTML, and Markdown formats.

    <hr>
    <br>
    """

    # copyAvailable: ClassVar[Signal] = ...  # copyAvailable(bool)
    # currentCharFormatChanged: ClassVar[Signal] = (
    #    ...
    # )  currentCharFormatChanged(QTextCharFormat)
    cursorPositionChanged: ClassVar[Signal] = ...  # cursorPositionChanged()
    # redoAvailable: ClassVar[Signal] = ...  # redoAvailable(bool)
    # selectionChanged: ClassVar[Signal] = ...  # selectionChanged()
    textChanged: ClassVar[Signal] = ...  # textChanged()
    # undoAvailable: ClassVar[Signal] = ...  # undoAvailable(bool)

    # class AutoFormattingFlag(enum.Flag):

    #     AutoAll: QTextEdit.AutoFormattingFlag = ...  # -0x1
    #     AutoNone: QTextEdit.AutoFormattingFlag = ...  # 0x0
    #     AutoBulletList: QTextEdit.AutoFormattingFlag = ...  # 0x1

    # class ExtraSelection(Shiboken.Object):
    #     @overload
    #     def __init__(self) -> None: ...
    #     @overload
    #     def __init__(
    #         self, ExtraSelection: PySide6.QtWidgets.QTextEdit.ExtraSelection
    #     ) -> None: ...
    #     @staticmethod
    #     def __copy__() -> None: ...

    # class LineWrapMode(enum.Enum):

    #     NoWrap: QTextEdit.LineWrapMode = ...  # 0x0
    #     WidgetWidth: QTextEdit.LineWrapMode = ...  # 0x1
    #     FixedPixelWidth: QTextEdit.LineWrapMode = ...  # 0x2
    #     FixedColumnWidth: QTextEdit.LineWrapMode = ...  # 0x3

    # @overload
    # def __init__(self, parent: Optional[PySide6.QtWidgets.QWidget] = ...) -> None: ...
    # @overload
    # def __init__(
    #     self, text: str, parent: Optional[PySide6.QtWidgets.QWidget] = ...
    # ) -> None: ...
    # def acceptRichText(self) -> bool: ...
    # def alignment(self) -> PySide6.QtCore.Qt.AlignmentFlag: ...
    # def anchorAt(self, pos: PySide6.QtCore.QPoint) -> str: ...
    def append(self, text: str) -> None:
        """
        Append text to the end of the text edit.

        Args:
            text (str): The text to append.

        <br>
        """

    # def autoFormatting(self) -> PySide6.QtWidgets.QTextEdit.AutoFormattingFlag: ...
    # def canInsertFromMimeData(self, source: PySide6.QtCore.QMimeData) -> bool: ...
    # def canPaste(self) -> bool: ...
    # def changeEvent(self, e: PySide6.QtCore.QEvent) -> None: ...
    def clear(self) -> None:
        """
        Clear the text in the text edit.

        <br>
        """

    # def contextMenuEvent(self, e: PySide6.QtGui.QContextMenuEvent) -> None: ...
    def copy(self) -> None:
        """
        Copiy any selected text to the clipboard.

        <br>
        """

    # def createMimeDataFromSelection(self) -> PySide6.QtCore.QMimeData: ...
    # @overload
    # def createStandardContextMenu(self) -> PySide6.QtWidgets.QMenu: ...
    # @overload
    # def createStandardContextMenu(
    #     self, position: PySide6.QtCore.QPoint
    # ) -> PySide6.QtWidgets.QMenu: ...
    # def currentCharFormat(self) -> PySide6.QtGui.QTextCharFormat: ...
    # def currentFont(self) -> PySide6.QtGui.QFont: ...
    # def cursorForPosition(
    #     self, pos: PySide6.QtCore.QPoint
    # ) -> PySide6.QtGui.QTextCursor: ...
    # @overload
    # def cursorRect(self) -> PySide6.QtCore.QRect: ...
    # @overload
    # def cursorRect(self, cursor: PySide6.QtGui.QTextCursor) -> PySide6.QtCore.QRect: ...
    # def cursorWidth(self) -> int: ...
    def cut(self) -> None:
        """
        Cut any selected text to the clipboard.

        <br>
        """

    # def doSetTextCursor(self, cursor: PySide6.QtGui.QTextCursor) -> None: ...
    # def document(self) -> PySide6.QtGui.QTextDocument: ...
    # def documentTitle(self) -> str: ...
    # def dragEnterEvent(self, e: PySide6.QtGui.QDragEnterEvent) -> None: ...
    # def dragLeaveEvent(self, e: PySide6.QtGui.QDragLeaveEvent) -> None: ...
    # def dragMoveEvent(self, e: PySide6.QtGui.QDragMoveEvent) -> None: ...
    # def dropEvent(self, e: PySide6.QtGui.QDropEvent) -> None: ...
    # def ensureCursorVisible(self) -> None: ...
    # def event(self, e: PySide6.QtCore.QEvent) -> bool: ...
    # def extraSelections(self) -> List[PySide6.QtWidgets.QTextEdit.ExtraSelection]: ...
    # @overload
    # def find(
    #     self, exp: str, options: PySide6.QtGui.QTextDocument.FindFlag = ...
    # ) -> bool: ...
    # @overload
    # def find(
    #     self,
    #     exp: Union[PySide6.QtCore.QRegularExpression, str],
    #     options: PySide6.QtGui.QTextDocument.FindFlag = ...,
    # ) -> bool: ...
    # def focusInEvent(self, e: PySide6.QtGui.QFocusEvent) -> None: ...
    # def focusNextPrevChild(self, next: bool) -> bool: ...
    # def focusOutEvent(self, e: PySide6.QtGui.QFocusEvent) -> None: ...
    # def fontFamily(self) -> str: ...
    # def fontItalic(self) -> bool: ...
    # def fontPointSize(self) -> float: ...
    # def fontUnderline(self) -> bool: ...
    # def fontWeight(self) -> int: ...
    # def inputMethodEvent(self, arg__1: PySide6.QtGui.QInputMethodEvent) -> None: ...
    # @overload
    # def inputMethodQuery(self, property: PySide6.QtCore.Qt.InputMethodQuery) -> Any: ...
    # @overload
    # def inputMethodQuery(
    #     self, query: PySide6.QtCore.Qt.InputMethodQuery, argument: Any
    # ) -> Any: ...
    # def insertFromMimeData(self, source: PySide6.QtCore.QMimeData) -> None: ...
    # def insertHtml(self, text: str) -> None: ...
    # def insertPlainText(self, text: str) -> None: ...
    def isReadOnly(self) -> bool:
        """
        Check if the text edit is read-only.

        Returns:
            bool: True if the text edit is read-only, False otherwise.

        <br>
        """

    # def isUndoRedoEnabled(self) -> bool: ...
    # def keyPressEvent(self, e: PySide6.QtGui.QKeyEvent) -> None: ...
    # def keyReleaseEvent(self, e: PySide6.QtGui.QKeyEvent) -> None: ...
    # def lineWrapColumnOrWidth(self) -> int: ...
    # def lineWrapMode(self) -> PySide6.QtWidgets.QTextEdit.LineWrapMode: ...
    # def loadResource(self, type: int, name: Union[PySide6.QtCore.QUrl, str]) -> Any: ...
    # def mergeCurrentCharFormat(
    #     self, modifier: PySide6.QtGui.QTextCharFormat
    # ) -> None: ...
    # def mouseDoubleClickEvent(self, e: PySide6.QtGui.QMouseEvent) -> None: ...
    # def mouseMoveEvent(self, e: PySide6.QtGui.QMouseEvent) -> None: ...
    # def mousePressEvent(self, e: PySide6.QtGui.QMouseEvent) -> None: ...
    # def mouseReleaseEvent(self, e: PySide6.QtGui.QMouseEvent) -> None: ...
    # def moveCursor(
    #     self,
    #     operation: PySide6.QtGui.QTextCursor.MoveOperation,
    #     mode: PySide6.QtGui.QTextCursor.MoveMode = ...,
    # ) -> None: ...
    # def overwriteMode(self) -> bool: ...
    # def paintEvent(self, e: PySide6.QtGui.QPaintEvent) -> None: ...
    def paste(self) -> None:
        """
        Paste text from the clipboard into the text edit.

        <br>
        """

    def placeholderText(self) -> str:
        """
        Get the placeholder text of the text edit.

        Returns:
            str: The placeholder text of the text edit.

        <br>
        """

    # def print_(self, printer: PySide6.QtGui.QPagedPaintDevice) -> None: ...
    def redo(self) -> None:
        """
        Redo the last operation.

        <br>
        """

    # def resizeEvent(self, e: PySide6.QtGui.QResizeEvent) -> None: ...
    # def scrollContentsBy(self, dx: int, dy: int) -> None: ...
    # def scrollToAnchor(self, name: str) -> None: ...
    # def selectAll(self) -> None: ...
    # def setAcceptRichText(self, accept: bool) -> None: ...
    # def setAlignment(self, a: PySide6.QtCore.Qt.AlignmentFlag) -> None: ...
    # def setAutoFormatting(
    #     self, features: PySide6.QtWidgets.QTextEdit.AutoFormattingFlag
    # ) -> None: ...
    # def setCurrentCharFormat(self, format: PySide6.QtGui.QTextCharFormat) -> None: ...
    # def setCurrentFont(
    #     self, f: Union[PySide6.QtGui.QFont, str, Sequence[str]]
    # ) -> None: ...
    # def setCursorWidth(self, width: int) -> None: ...
    # def setDocument(self, document: PySide6.QtGui.QTextDocument) -> None: ...
    # def setDocumentTitle(self, title: str) -> None: ...
    # def setExtraSelections(
    #     self, selections: Sequence[PySide6.QtWidgets.QTextEdit.ExtraSelection]
    # ) -> None: ...
    # def setFontFamily(self, fontFamily: str) -> None: ...
    def setFontItalic(self, b: bool) -> None:
        """
        Set the italic font style of the text edit. All text added to the text edit after a call with `True` will be displayed in italic.

        Args:
            b (bool): True to set the font style to italic, False otherwise.

        <br>
        """

    def setFontPointSize(self, s: float) -> None:
        """
        Set the font size of the text edit. All text added to the text edit after a call with a specific size will be displayed with that size.

        Args:
            s (float): The font size to set.

        <br>
        """

    def setFontUnderline(self, b: bool) -> None:
        """
        Set the underline font style of the text edit. All text added to the text edit after a call with `True` will be displayed with an underline.

        Args:
            b (bool): True to set the font style to underline, False otherwise.

        <br>
        """

    def setFontWeight(self, w: int) -> None:
        """
        Set the font weight of the text edit. Font weight is a numerical value that determines the thickness of the characters in the text edit.
        All text added to the text edit after a call with a specific weight will be displayed with that weight.

        Args:
            w (int): The font weight to set.

        <br>
        """

    def setHtml(self, text: str) -> None:
        """
        Set the text edit contents to the specified HTML text.

        Args:
            text (str): The HTML text to set.

        <br>
        """

    # def setLineWrapColumnOrWidth(self, w: int) -> None: ...
    # def setLineWrapMode(
    #     self, mode: PySide6.QtWidgets.QTextEdit.LineWrapMode
    # ) -> None: ...
    def setMarkdown(self, markdown: str) -> None:
        """
        Set the text edit contents to the specified Markdown text.

        Args:
            markdown (str): The Markdown text to set.

        <br>
        """

    # def setOverwriteMode(self, overwrite: bool) -> None: ...
    def setPlaceholderText(self, placeholderText: str) -> None:
        """
        Set the placeholder text of the text edit. Placeholder text is grayed out and displayed when the text edit is empty.

        Args:
            placeholderText (str): The placeholder text to set.

        <br>
        """

    # def setPlainText(self, text: str) -> None: ...
    def setReadOnly(self, ro: bool) -> None:
        """
        Set whether the text edit is read-only. If the text edit is read-only, the user cannot edit the text.

        Args:
            ro (bool): True to set the text edit to read-only, False otherwise.

        <br>
        """

    # def setTabChangesFocus(self, b: bool) -> None: ...
    # def setTabStopDistance(self, distance: float) -> None: ...
    def setText(self, text: str) -> None:
        """
        Set the contents of the text edit to the specified text. The text is displayed as plain text.

        Args:
            text (str): The text to set.

        <br>
        """

    # def setTextBackgroundColor(
    #     self,
    #     c: Union[
    #         PySide6.QtGui.QColor,
    #         PySide6.QtGui.QRgba64,
    #         Any,
    #         PySide6.QtCore.Qt.GlobalColor,
    #         str,
    #         int,
    #     ],
    # ) -> None: ...
    # def setTextColor(
    #     self,
    #     c: Union[
    #         PySide6.QtGui.QColor,
    #         PySide6.QtGui.QRgba64,
    #         Any,
    #         PySide6.QtCore.Qt.GlobalColor,
    #         str,
    #         int,
    #     ],
    # ) -> None: ...
    # def setTextCursor(self, cursor: PySide6.QtGui.QTextCursor) -> None: ...
    # def setTextInteractionFlags(
    #     self, flags: PySide6.QtCore.Qt.TextInteractionFlag
    # ) -> None: ...
    # def setUndoRedoEnabled(self, enable: bool) -> None: ...
    # def setWordWrapMode(self, policy: PySide6.QtGui.QTextOption.WrapMode) -> None: ...
    # def showEvent(self, arg__1: PySide6.QtGui.QShowEvent) -> None: ...
    # def tabChangesFocus(self) -> bool: ...
    # def tabStopDistance(self) -> float: ...
    # def textBackgroundColor(self) -> PySide6.QtGui.QColor: ...
    # def textColor(self) -> PySide6.QtGui.QColor: ...
    # def textCursor(self) -> PySide6.QtGui.QTextCursor: ...
    # def textInteractionFlags(self) -> PySide6.QtCore.Qt.TextInteractionFlag: ...
    # def timerEvent(self, e: PySide6.QtCore.QTimerEvent) -> None: ...
    def toHtml(self) -> str:
        """
        Get the text edit contents as HTML text.

        Returns:
            str: The text edit contents as HTML text.

        <br>
        """

    def toMarkdown(self) -> str:
        """
        Get the text edit contents as Markdown text.

        Returns:
            str: The text edit contents as Markdown text.

        <br>
        """

    def toPlainText(self) -> str:
        """
        Get the text edit contents as plain text. For example if the text edit contains the HTML text `<b>bold</b>`, the returned text will be `bold`.

        Returns:
            str: The text edit contents as plain text.

        <br>
        """

    def undo(self) -> None:
        """
        Undo the last operation in the text edit.

        <br>
        """

    # def wheelEvent(self, e: PySide6.QtGui.QWheelEvent) -> None: ...
    # def wordWrapMode(self) -> PySide6.QtGui.QTextOption.WrapMode: ...
    def zoomIn(self, r: int) -> None:
        """
        Zoom in the text edit by the specified range.

        Args:
            r (int): The range to zoom in by.

        <br>
        """

    # def zoomInF(self, range: float) -> None: ...
    def zoomOut(self, r: int) -> None:
        """
        Zoom out the text edit by the specified range.

        Args:
            r (int): The range to zoom out by.

        <br>
        <br>
        """


class QCheckBox:
    """
    <hr>
    ![](buttons/checkbox.png)

    A <code>QCheckBox</code> widget is a toggle button that can be checked or unchecked.
    Checkboxes are typically used to represent features in an application that
    can be enabled or disabled without affecting others. By default, a checkbox
    is unchecked.

    Args:
        text (str): The text to display next to the checkbox.

    <hr>

    <h3>Signals</h3>
    <ul>
        <li><code>stateChanged</code>: Emitted whenever the checkbox's state changes.</li>
    </ul>

    <h3>Methods</h3>
    <ul>
        <li><a href="#code.QtWidgets.QCheckBox.IsChecked"><code>IsChecked</code></a></li>
        <li><a href="#code.QtWidgets.QCheckBox.setChecked"><code>setChecked</code></a></li>
        <li><a href="#code.QtWidgets.QCheckBox.setText"><code>setText</code></a></li>
        <li><a href="#code.QtWidgets.QCheckBox.text"><code>text</code></a></li>
    </ul>

    <br>


    **Examples**
        <hr>
        ``` py
        checkbox = QtWidgets.QCheckBox()
        print(checkbox.IsChecked())
        ```
        ```False```
        ``` py
        checkbox.setChecked(True)
        print(checkbox.IsChecked())
        ```
        ```True```
        <hr>

    <br>
    """

    def __init__(self, text: str = None) -> None: ...

    def IsChecked() -> bool:
        """
        Returns True if the checkbox is checked; otherwise returns False.

        Returns:
            True if the checkbox is checked; otherwise False.
        <br>
        """
        ...

    def setChecked(checked: bool):
        """
        Sets the checkbox to be checked if checked is True; otherwise sets it
        to be unchecked.

        Args:
            checked (bool): True to check the checkbox; otherwise False.
        <br>
        """

    # stateChanged             : ClassVar[Signal] = ... # stateChanged(int)

    # @overload
    # def __init__(self, parent: Optional[PySide6.QtWidgets.QWidget] = ...) -> None: ...

    def setText(self, text: str) -> None:
        """
        Set the text to display next to the checkbox.

        Args:
            text (str): The text to display next to the checkbox.
        <br>
        """

    def text(self) -> str:
        """
        Get the text displayed next to the checkbox.

        Returns:
            str: The text displayed next to the checkbox.
        <br>
        <br>
        """

    # def checkState(self) -> PySide6.QtCore.Qt.CheckState: ...
    # def checkStateSet(self) -> None: ...
    # def event(self, e: PySide6.QtCore.QEvent) -> bool: ...
    # def hitButton(self, pos: PySide6.QtCore.QPoint) -> bool: ...
    # def initStyleOption(self, option: PySide6.QtWidgets.QStyleOptionButton) -> None: ...
    # def isTristate(self) -> bool: ...
    # def minimumSizeHint(self) -> PySide6.QtCore.QSize: ...
    # def mouseMoveEvent(self, arg__1: PySide6.QtGui.QMouseEvent) -> None: ...
    # def nextCheckState(self) -> None: ...
    # def paintEvent(self, arg__1: PySide6.QtGui.QPaintEvent) -> None: ...
    # def setCheckState(self, state: PySide6.QtCore.Qt.CheckState) -> None: ...
    # def setTristate(self, y: bool = ...) -> None: ...
    # def sizeHint(self) -> PySide6.QtCore.QSize: ...


class QLabel:
    """
    <hr>
    ![](buttons/label.png)

    <code>QLabel</code> is used for displaying text or an image. No user interaction
    functionality is provided.

    Args:
        text (str): The text to display.

    <hr>


    <h3>Methods</h3>
    <ul>
        <li><a href="#code.QtWidgets.QLabel.setText"><code>setText</code></a></li>
        <li><a href="#code.QtWidgets.QLabel.text"><code>text</code></a></li>
    </ul>

    <br>



    **Examples**
        <hr>
        ``` py
        label = QtWidgets.QLabel("Hello World!")
        print(label.text())
        ```
        ```'Hello World!'```
        ``` py
        label.setText("Goodbye World!")
        print(label.text())
        ```
        ```'Goodbye World!'```
        <hr>

    <br>
    """

    # linkActivated            : ClassVar[Signal] = ... # linkActivated(QString)
    # linkHovered              : ClassVar[Signal] = ... # linkHovered(QString)

    # @overload
    # def __init__(self, parent: Optional[PySide6.QtWidgets.QWidget] = ..., f: PySide6.QtCore.Qt.WindowType = ...) -> None: ...

    def __init__(self, text: str = None) -> None: ...

    # def alignment(self) -> PySide6.QtCore.Qt.AlignmentFlag: ...
    # def buddy(self) -> PySide6.QtWidgets.QWidget: ...
    # def changeEvent(self, arg__1: PySide6.QtCore.QEvent) -> None: ...
    # def clear(self) -> None: ...
    # def contextMenuEvent(self, ev: PySide6.QtGui.QContextMenuEvent) -> None: ...
    # def event(self, e: PySide6.QtCore.QEvent) -> bool: ...
    # def focusInEvent(self, ev: PySide6.QtGui.QFocusEvent) -> None: ...
    # def focusNextPrevChild(self, next: bool) -> bool: ...
    # def focusOutEvent(self, ev: PySide6.QtGui.QFocusEvent) -> None: ...
    # def hasScaledContents(self) -> bool: ...
    # def hasSelectedText(self) -> bool: ...
    # def heightForWidth(self, arg__1: int) -> int: ...
    # def indent(self) -> int: ...
    # def keyPressEvent(self, ev: PySide6.QtGui.QKeyEvent) -> None: ...
    # def margin(self) -> int: ...
    # def minimumSizeHint(self) -> PySide6.QtCore.QSize: ...
    # def mouseMoveEvent(self, ev: PySide6.QtGui.QMouseEvent) -> None: ...
    # def mousePressEvent(self, ev: PySide6.QtGui.QMouseEvent) -> None: ...
    # def mouseReleaseEvent(self, ev: PySide6.QtGui.QMouseEvent) -> None: ...
    # def movie(self) -> PySide6.QtGui.QMovie: ...
    # def openExternalLinks(self) -> bool: ...
    # def paintEvent(self, arg__1: PySide6.QtGui.QPaintEvent) -> None: ...
    # def picture(self) -> PySide6.QtGui.QPicture: ...
    # def pixmap(self) -> PySide6.QtGui.QPixmap: ...
    # def selectedText(self) -> str: ...
    # def selectionStart(self) -> int: ...
    # def setAlignment(self, arg__1: PySide6.QtCore.Qt.AlignmentFlag) -> None: ...
    # def setBuddy(self, arg__1: PySide6.QtWidgets.QWidget) -> None: ...
    # def setIndent(self, arg__1: int) -> None: ...
    # def setMargin(self, arg__1: int) -> None: ...
    # def setMovie(self, movie: PySide6.QtGui.QMovie) -> None: ...
    # @overload
    # def setNum(self, arg__1: float) -> None: ...
    # @overload
    # def setNum(self, arg__1: int) -> None: ...
    # def setOpenExternalLinks(self, open: bool) -> None: ...
    # def setPicture(self, arg__1: Union[PySide6.QtGui.QPicture, int]) -> None: ...
    # def setPixmap(self, arg__1: Union[PySide6.QtGui.QPixmap, PySide6.QtGui.QImage, str]) -> None: ...
    # def setScaledContents(self, arg__1: bool) -> None: ...
    # def setSelection(self, arg__1: int, arg__2: int) -> None: ...
    def setText(self, text: str) -> None:
        """
        Sets the label's text to the given text.

        Args:
            text (str): The text to set.
        <br>
        """

    # def setTextFormat(self, arg__1: PySide6.QtCore.Qt.TextFormat) -> None: ...
    # def setTextInteractionFlags(self, flags: PySide6.QtCore.Qt.TextInteractionFlag) -> None: ...
    # def setWordWrap(self, on: bool) -> None: ...
    # def sizeHint(self) -> PySide6.QtCore.QSize: ...
    def text(self) -> str:
        """
        Returns the label's text.

        Returns:
            The label's text.
        <br>
        <br>
        """

    # def textFormat(self) -> PySide6.QtCore.Qt.TextFormat: ...
    # def textInteractionFlags(self) -> PySide6.QtCore.Qt.TextInteractionFlag: ...
    # def wordWrap(self) -> bool: ...


class QComboBox:
    """
    <hr>
    ![](buttons/combobox.png)

    A <code>QComboBox</code> is a button that provides a list of options to the user when clicked.
    The user can select an option from the list. The selected option is displayed
    in the combo box.

    <hr>

    <h3>Signals</h3>
    <ul>
        <li><code>currentIndexChanged</code>: Emitted when the current index changes.</li>
    </ul>

    <h3>Methods</h3>
    <ul>
        <li><a href="#code.QtWidgets.QComboBox.addItem"><code>addItem</code></a></li>
        <li><a href="#code.QtWidgets.QComboBox.addItems"><code>addItems</code></a></li>
        <li><a href="#code.QtWidgets.QComboBox.clear"><code>clear</code></a></li>
        <li><a href="#code.QtWidgets.QComboBox.currentIndex"><code>currentIndex</code></a></li>
        <li><a href="#code.QtWidgets.QComboBox.currentText"><code>currentText</code></a></li>
        <li><a href="#code.QtWidgets.QComboBox.removeItem"><code>removeItem</code></a></li>
        <li><a href="#code.QtWidgets.QComboBox.setCurrentIndex"><code>setCurrentIndex</code></a></li>
        <li><a href="#code.QtWidgets.QComboBox.setCurrentText"><code>setCurrentText</code></a></li>
    </ul>

    <br>


    **Examples**
        <hr>
        ``` py
        combo = QtWidgets.QComboBox()
        combo.addItem("Option 1")
        combo.addItems(["Option 2", "Option 3"])
        print(combo.currentText())
        ```
        ```'Option 1'```
        ``` py
        print(combo.currentIndex())
        ```
        ```'0'```
        ``` py
        combo.setCurrentIndex(2)
        print(combo.currentText())
        ```
        ```'Option 3'```
        ``` py
        combo.clear()
        print(combo.currentText())
        ```
        ```''```
        ``` py
        print(combo.currentIndex())
        ```
        ```'-1'```
        <hr>
    <br>
    """

    # activated                : ClassVar[Signal] = ... # activated(int)
    currentIndexChanged: ClassVar[Signal] = ...  # currentIndexChanged(int)
    # currentTextChanged       : ClassVar[Signal] = ... # currentTextChanged(QString)
    # editTextChanged          : ClassVar[Signal] = ... # editTextChanged(QString)
    # highlighted              : ClassVar[Signal] = ... # highlighted(int)
    # textActivated            : ClassVar[Signal] = ... # textActivated(QString)
    # textHighlighted          : ClassVar[Signal] = ... # textHighlighted(QString)

    # class InsertPolicy(enum.Enum):

    #     NoInsert: QComboBox.InsertPolicy = ...  # 0x0
    #     InsertAtTop: QComboBox.InsertPolicy = ...  # 0x1
    #     InsertAtCurrent: QComboBox.InsertPolicy = ...  # 0x2
    #     InsertAtBottom: QComboBox.InsertPolicy = ...  # 0x3
    #     InsertAfterCurrent: QComboBox.InsertPolicy = ...  # 0x4
    #     InsertBeforeCurrent: QComboBox.InsertPolicy = ...  # 0x5
    #     InsertAlphabetically: QComboBox.InsertPolicy = ...  # 0x6

    # class SizeAdjustPolicy(enum.Enum):

    #     AdjustToContents: QComboBox.SizeAdjustPolicy = ...  # 0x0
    #     AdjustToContentsOnFirstShow: QComboBox.SizeAdjustPolicy = ...  # 0x1
    #     AdjustToMinimumContentsLengthWithIcon: QComboBox.SizeAdjustPolicy = ...  # 0x2

    # def __init__(self, parent: Optional[PySide6.QtWidgets.QWidget] = ...) -> None: ...

    # @overload
    # def addItem(self,icon: Union[PySide6.QtGui.QIcon, PySide6.QtGui.QPixmap], text: str, userData: Any = ...,) -> None: ...
    # @overload
    def addItem(self, text: str) -> None:
        """
        Adds an item to the combo box with the given text.

        Args:
            text (str): The text to display in the combo box.
        <br>
        """

    def addItems(self, texts: Sequence[str]) -> None:
        """
        Adds the items in the list texts to the combo box.

        Args:
            texts (Sequence[str]): The list of strings to add to the combo box.
        <br>
        """

    # def changeEvent(self, e: PySide6.QtCore.QEvent) -> None: ...
    def clear(self) -> None:
        """
        Clears the contents of the combo box, removing all items.

        <br>
        """

    # def clearEditText(self) -> None: ...
    # def completer(self) -> PySide6.QtWidgets.QCompleter: ...
    # def contextMenuEvent(self, e: PySide6.QtGui.QContextMenuEvent) -> None: ...
    # def count(self) -> int: ...
    # def currentData(self, role: int = ...) -> Any: ...
    def currentIndex(self) -> int:
        """
        Gets the index of the currently selected item in the combo box. For
        an empty combo box, returns -1. The current index can change when inserting
        or removing items.

        Returns:
            The index of the currently selected item.
        <br>
        """

    def currentText(self) -> str:
        """
        Gets the text of the currently selected item in the combo box. For an
        empty combo box, returns an empty string.

        Returns:
            The text of the currently selected item.
        <br>
        """

    # def duplicatesEnabled(self) -> bool: ...
    # def event(self, event: PySide6.QtCore.QEvent) -> bool: ...
    # def findData(self, data: Any, role: int = ..., flags: PySide6.QtCore.Qt.MatchFlag = ...) -> int: ...
    # def findText(self, text: str, flags: PySide6.QtCore.Qt.MatchFlag = ...) -> int: ...
    # def focusInEvent(self, e: PySide6.QtGui.QFocusEvent) -> None: ...
    # def focusOutEvent(self, e: PySide6.QtGui.QFocusEvent) -> None: ...
    # def hasFrame(self) -> bool: ...
    # def hideEvent(self, e: PySide6.QtGui.QHideEvent) -> None: ...
    # def hidePopup(self) -> None: ...
    # def iconSize(self) -> PySide6.QtCore.QSize: ...
    # def initStyleOption(self, option: PySide6.QtWidgets.QStyleOptionComboBox) -> None: ...
    # def inputMethodEvent(self, arg__1: PySide6.QtGui.QInputMethodEvent) -> None: ...
    # @overload
    # def inputMethodQuery(self, arg__1: PySide6.QtCore.Qt.InputMethodQuery) -> Any: ...
    # @overload
    # def inputMethodQuery(self, query: PySide6.QtCore.Qt.InputMethodQuery, argument: Any) -> Any: ...
    # @overload
    # def insertItem(self, index: int, icon: Union[PySide6.QtGui.QIcon, PySide6.QtGui.QPixmap], text: str, userData: Any = ...) -> None: ...
    # @overload
    # def insertItem(self, index: int, text: str, userData: Any = ...) -> None: ...
    # def insertItems(self, index: int, texts: Sequence[str]) -> None: ...
    # def insertPolicy(self) -> PySide6.QtWidgets.QComboBox.InsertPolicy: ...
    # def insertSeparator(self, index: int) -> None: ...
    # def isEditable(self) -> bool: ...
    # def itemData(self, index: int, role: int = ...) -> Any: ...
    # def itemDelegate(self) -> PySide6.QtWidgets.QAbstractItemDelegate: ...
    # def itemIcon(self, index: int) -> PySide6.QtGui.QIcon: ...
    # def itemText(self, index: int) -> str: ...
    # def keyPressEvent(self, e: PySide6.QtGui.QKeyEvent) -> None: ...
    # def keyReleaseEvent(self, e: PySide6.QtGui.QKeyEvent) -> None: ...
    # def lineEdit(self) -> PySide6.QtWidgets.QLineEdit: ...
    # def maxCount(self) -> int: ...
    # def maxVisibleItems(self) -> int: ...
    # def minimumContentsLength(self) -> int: ...
    # def minimumSizeHint(self) -> PySide6.QtCore.QSize: ...
    # def model(self) -> PySide6.QtCore.QAbstractItemModel: ...
    # def modelColumn(self) -> int: ...
    # def mousePressEvent(self, e: PySide6.QtGui.QMouseEvent) -> None: ...
    # def mouseReleaseEvent(self, e: PySide6.QtGui.QMouseEvent) -> None: ...
    # def paintEvent(self, e: PySide6.QtGui.QPaintEvent) -> None: ...
    # def placeholderText(self) -> str: ...
    def removeItem(self, index: int) -> None:
        """
        Removes the item at the given index from the combo box.

        Args:
            index (int): The index of the item to remove.
        <br>
        """

    # def resizeEvent(self, e: PySide6.QtGui.QResizeEvent) -> None: ...
    # def rootModelIndex(self) -> PySide6.QtCore.QModelIndex: ...
    # def setCompleter(self, c: PySide6.QtWidgets.QCompleter) -> None: ...
    def setCurrentIndex(self, index: int) -> None:
        """
        Sets the current index of the combo box to the given index.

        Args:
            index (int): The index of the item to set as the current item.
        <br>
        """

    def setCurrentText(self, text: str) -> None:
        """
        Sets the current text of the combo box to the given text.

        Args:
            text (str): The text to set as the current text.
        <br>
        <br>
        """

    # def setText(): ...

    # def setDuplicatesEnabled(self, enable: bool) -> None: ...
    # def setEditText(self, text: str) -> None: ...
    # def setEditable(self, editable: bool) -> None: ...
    # def setFrame(self, arg__1: bool) -> None: ...
    # def setIconSize(self, size: PySide6.QtCore.QSize) -> None: ...
    # def setInsertPolicy(self, policy: PySide6.QtWidgets.QComboBox.InsertPolicy) -> None: ...
    # def setItemData(self, index: int, value: Any, role: int = ...) -> None: ...
    # def setItemDelegate(self, delegate: PySide6.QtWidgets.QAbstractItemDelegate) -> None: ...
    # def setItemIcon(self, index: int, icon: Union[PySide6.QtGui.QIcon, PySide6.QtGui.QPixmap]) -> None: ...
    # def setItemText(self, index: int, text: str) -> None: ...
    # def setLineEdit(self, edit: PySide6.QtWidgets.QLineEdit) -> None: ...
    # def setMaxCount(self, max: int) -> None: ...
    # def setMaxVisibleItems(self, maxItems: int) -> None: ...
    # def setMinimumContentsLength(self, characters: int) -> None: ...
    # def setModel(self, model: PySide6.QtCore.QAbstractItemModel) -> None: ...
    # def setModelColumn(self, visibleColumn: int) -> None: ...
    # def setPlaceholderText(self, placeholderText: str) -> None: ...
    # def setRootModelIndex(self, index: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex]) -> None: ...
    # def setSizeAdjustPolicy(self, policy: PySide6.QtWidgets.QComboBox.SizeAdjustPolicy) -> None: ...
    # def setValidator(self, v: PySide6.QtGui.QValidator) -> None: ...
    # def setView(self, itemView: PySide6.QtWidgets.QAbstractItemView) -> None: ...
    # def showEvent(self, e: PySide6.QtGui.QShowEvent) -> None: ...
    # def showPopup(self) -> None: ...
    # def sizeAdjustPolicy(self) -> PySide6.QtWidgets.QComboBox.SizeAdjustPolicy: ...
    # def sizeHint(self) -> PySide6.QtCore.QSize: ...
    # def validator(self) -> PySide6.QtGui.QValidator: ...
    # def view(self) -> PySide6.QtWidgets.QAbstractItemView: ...
    # def wheelEvent(self, e: PySide6.QtGui.QWheelEvent) -> None: ...


class QSpinBox:
    """
    <hr>
    ![](buttons/spinbox.png)

    `QSpinBox` is designed to handle integers and discrete sets of values. Use
    [`QDoubleSpinBox`](QDoubleSpinBox.md) for floating point values.
    `QSpinBox` allows the user to choose a value by clicking the up and down buttons
    to increment or decrement the value displayed. The value can also be changed by typing
    in a value. The range of valid values and the number of decimal places shown is configurable.

    <hr>

    <h3>Signals</h3>
    <ul>
        <li><code>valueChanged</code>: Emitted when the value in the spin box changes.</li>
    </ul>

    <h3>Methods</h3>
    <ul>
        <li><a href="#code.QtWidgets.QSpinBox.setMaximum"><code>setMaximum</code></a></li>
        <li><a href="#code.QtWidgets.QSpinBox.setMinimum"><code>setMinimum</code></a></li>
        <li><a href="#code.QtWidgets.QSpinBox.setSingleStep"><code>setSingleStep</code></a></li>
        <li><a href="#code.QtWidgets.QSpinBox.setValue"><code>setValue</code></a></li>
        <li><a href="#code.QtWidgets.QSpinBox.value"><code>value</code></a></li>
        <li><a href="#code.QtWidgets.QSpinBox.setRange"><code>setRange</code></a></li>
        <li><a href="#code.QtWidgets.QSpinBox.setPrefix"><code>setPrefix</code></a></li>
        <li><a href="#code.QtWidgets.QSpinBox.setSuffix"><code>setSuffix</code></a></li>
    </ul>

    <br>

    **Examples**
        <hr>
        ``` py
        spin_box = QtWidgets.QSpinBox()
        spin_box.setMaximum(100)
        spin_box.setMinimum(0)
        spin_box.setSingleStep(5)
        spin_box.setValue(50)
        print(spin_box.value())
        ```
        ```50```
        ``` py
        spin_box.setValue(200)
        print(spin_box.value())
        ```
        ```100```
        <hr>

    <br>
    """

    textChanged: ClassVar[Signal] = ...  # textChanged(QString)
    valueChanged: ClassVar[Signal] = ...  # valueChanged(int)

    # def __init__(self, parent: Optional[PySide6.QtWidgets.QWidget] = ...) -> None: ...

    # def cleanText(self) -> str: ...
    # def displayIntegerBase(self) -> int: ...
    # def event(self, event: PySide6.QtCore.QEvent) -> bool: ...
    # def fixup(self, str: str) -> str: ...
    # def maximum(self) -> int: ...
    # def minimum(self) -> int: ...
    # def prefix(self) -> str: ...
    # def setDisplayIntegerBase(self, base: int) -> None: ...

    def setMaximum(self, max: int) -> None:
        """
        Set the maximum value of the spin box. The default maximum value is 99.

        Args:
            max (int): The maximum value of the spin box.
        <br>
        """

    def setMinimum(self, min: int) -> None:
        """
        Set the minimum value of the spin box. The default minimum value
        is 0.

        Args:
            min (int): The minimum value of the spin box.
        <br>
        """

    def setPrefix(self, prefix: str) -> None:
        """
        Set the prefix of the spin box. The prefix is displayed before the
        value in the spin box and is not editable by the user.

        Args:
            prefix (str): The prefix to set.
        <br>
        """

    def setRange(self, min: int, max: int) -> None:
        """
        Set the minimum and maximum values of the spin box.
        If the current value is outside the new range, the value is adjusted
        to the nearest limit.

        Args:
            min (int): The new minimum value.
            max (int): The new maximum value.
        <br>
        """

    def setSingleStep(self, val: int) -> None:
        """
        Set the value that the spin box will increment or decrement by when the
        up or down buttons are clicked. The default step value is 1. Setting a
        value less than 0 does nothing.

        Args:
            val (int): The value to increment or decrement by.
        <br>
        """

    # def setStepType(self, stepType: PySide6.QtWidgets.QAbstractSpinBox.StepType) -> None: ...
    def setSuffix(self, suffix: str) -> None:
        """
        Set the suffix of the spin box. The suffix is displayed after the value
        in the spin box and is not editable by the user.

        Args:
            suffix (str): The suffix to set.
        <br>
        """

    def setValue(self, val: int) -> None:
        """
        Set the value of the spin box. If the value is outside the range of
        the spin box, the value is adjusted to the nearest limit.

        Args:
            val (int): The value to set the spin box to.
        <br>
        """

    # def singleStep(self) -> int: ...
    # def stepType(self) -> PySide6.QtWidgets.QAbstractSpinBox.StepType: ...
    # def suffix(self) -> str: ...
    # def textFromValue(self, val: int) -> str: ...
    # def validate(self, input: str, pos: int) -> object: ...
    def value(self) -> int:
        """
        Returns the current value of the spin box.

        Returns:
            The current value of the spin box.
        <br>
        <br>
        """

    # def valueFromText(self, text: str) -> int: ...


class QDoubleSpinBox:
    """
    <hr>
    ![](buttons/double_spinbox.png)

    `QDoubleSpinBox` is designed to handle double values. For integers, use
    [`QSpinBox`](QSpinBox.md) instead. `QDoubleSpinBox`
    allows the user to choose a value by clicking the up and down buttons to
    increment or decrement the value displayed. The value can also be changed
    by typing in a value. The range of valid values and the number of decimal
    places shown is configurable.

    <hr>

    <h3>Signals</h3>
    <ul>
        <li><code>valueChanged</code>: Emitted when the value in the spin box changes.</li>
    </ul>


    <h3>Methods</h3>
    <ul>
        <li><a href="#code.QtWidgets.QDoubleSpinBox.setMaximum"><code>setMaximum</code></a></li>
        <li><a href="#code.QtWidgets.QDoubleSpinBox.setMinimum"><code>setMinimum</code></a></li>
        <li><a href="#code.QtWidgets.QDoubleSpinBox.setSingleStep"><code>setSingleStep</code></a></li>
        <li><a href="#code.QtWidgets.QDoubleSpinBox.setValue"><code>setValue</code></a></li>
        <li><a href="#code.QtWidgets.QDoubleSpinBox.value"><code>value</code></a></li>
        <li><a href="#code.QtWidgets.QDoubleSpinBox.setRange"><code>setRange</code></a></li>
        <li><a href="#code.QtWidgets.QDoubleSpinBox.setPrefix"><code>setPrefix</code></a></li>
        <li><a href="#code.QtWidgets.QDoubleSpinBox.setSuffix"><code>setSuffix</code></a></li>
    </ul>

    <br>

    **Examples**
        <hr>
        ``` py
        spin_box = QtWidgets.QDoubleSpinBox()
        spin_box.setMaximum(100)
        spin_box.setMinimum(0)
        spin_box.setSingleStep(0.1)
        spin_box.setValue(50)
        print(spin_box.value())
        ```
        ```50.0```
        ``` py
        spin_box.setValue(200)
        print(spin_box.value())
        ```
        ```100.0```
        <hr>

    <br>
    """

    textChanged: ClassVar[Signal] = ...  # textChanged(QString)
    valueChanged: ClassVar[Signal] = ...  # valueChanged(double)

    # def __init__(self, parent: Optional[PySide6.QtWidgets.QWidget] = ...) -> None: ...

    # def cleanText(self) -> str: ...
    # def decimals(self) -> int: ...
    # def fixup(self, str: str) -> str: ...
    # def maximum(self) -> float: ...
    # def minimum(self) -> float: ...
    # def prefix(self) -> str: ...
    # def setDecimals(self, prec: int) -> None: ...
    def setMaximum(self, max: float) -> None:
        """
        Set the maximum value of the spin box. The default maximum value
        is 99.99.

        Args:
            max: The new maximum value.
        <br>
        """

    def setMinimum(self, min: float) -> None:
        """
        Set the minimum value of the spin box. The default minimum value
        is 0.0.

        Args:
            min: The new minimum value.
        <br>
        """

    def setPrefix(self, prefix: str) -> None:
        """
        Set the prefix of the spin box. The prefix is displayed before the
        value in the spin box and is not editable by the user.

        Args:
            prefix: The new prefix.
        <br>
        """

    def setRange(self, min: float, max: float) -> None:
        """
        Set the minimum and maximum values of the spin box. If the current
        value is outside the new range, the value is adjusted to the nearest limit.

        Args:
            min: The new minimum value.
            max: The new maximum value.
        <br>
        """

    def setSingleStep(self, val: float) -> None:
        """
        Set the value that the spin box will increment or decrement by when the
        up or down buttons are clicked. The default step value is 1.0. Setting a
        singleStep value of less than 0 does nothing.

        Args:
            val: The new step value.
        <br>
        """

    # def setStepType(self, stepType: PySide6.QtWidgets.QAbstractSpinBox.StepType) -> None: ...
    def setSuffix(self, suffix: str) -> None:
        """
        Set the suffix of the spin box. The suffix is displayed after the value
        in the spin box and is not editable by the user.

        Args:
            suffix: The new suffix.
        <br>
        """

    def setValue(self, val: float) -> None:
        """
        Set the value of the spin box. If the value is outside the range of the
        spin box, the value is adjusted to the nearest limit.

        Args:
            val: The new value.
        <br>
        """

    # def singleStep(self) -> float: ...
    # def stepType(self) -> PySide6.QtWidgets.QAbstractSpinBox.StepType: ...
    # def suffix(self) -> str: ...
    # def textFromValue(self, val: float) -> str: ...
    # def validate(self, input: str, pos: int) -> object: ...
    def value(self) -> float:
        """
        Returns the value of the spin box.

        Returns:
            The value of the spin box.
        <br>
        <br>
        """

    # def valueFromText(self, text: str) -> float: ...


class QPushButton:
    """
    <hr>
    ![](buttons/pushbutton.png)

    The push button, or command button, is perhaps the most commonly used widget
    in any graphical user interface. Push (click) a button to command the computer
    to perform some action, or to answer a question. Typical buttons are OK, Apply,
    Cancel, Close, Yes, No and Help.

    args:
        text (str): The text to display on the button.

    <hr>

    <h3>Signals</h3>
    <ul>
        <li><code>clicked</code>: Emitted when the button is clicked.</li>
    </ul>

    <h3>Methods</h3>
    <ul>
        <li><a href="#code.QtWidgets.QPushButton.text"><code>text</code></a></li>
        <li><a href="#code.QtWidgets.QPushButton.setText"><code>setText</code></a></li>
    </ul>

    <br>

    **Examples**
        <hr>
        ``` py
        button = QtWidgets.QPushButton("Click me!")
        print(button.text())
        ```
        ```'Click me!'```
        ``` py
        button.setText("Don't click me!")
        print(button.text())
        ```
        ```'Don't click me!'```
        <hr>

    <br>
    """

    clicked: ClassVar[Signal] = ...  # clicked()

    def text(self) -> str:
        """
        Returns the text displayed in the button.

        Returns:
            The text displayed in the button.
        <br>
        """

    def setText(text: str) -> None:
        """
        Sets the text to be displayed in the button.

        Args:
            text (str): The text to display in the button.
        <br>
        <br>
        """

    # @overload
    # def __init__(self, icon: Union[PySide6.QtGui.QIcon, PySide6.QtGui.QPixmap], text: str, parent: Optional[PySide6.QtWidgets.QWidget] = ...) -> None: ...
    # @overload
    # def __init__(self, parent: Optional[PySide6.QtWidgets.QWidget] = ...) -> None: ...

    def __init__(self, text: str = None) -> None: ...

    # def autoDefault(self) -> bool: ...
    # def event(self, e: PySide6.QtCore.QEvent) -> bool: ...
    # def focusInEvent(self, arg__1: PySide6.QtGui.QFocusEvent) -> None: ...
    # def focusOutEvent(self, arg__1: PySide6.QtGui.QFocusEvent) -> None: ...
    # def hitButton(self, pos: PySide6.QtCore.QPoint) -> bool: ...
    # def initStyleOption(self, option: PySide6.QtWidgets.QStyleOptionButton) -> None: ...
    # def isDefault(self) -> bool: ...
    # def isFlat(self) -> bool: ...
    # def keyPressEvent(self, arg__1: PySide6.QtGui.QKeyEvent) -> None: ...
    # def menu(self) -> PySide6.QtWidgets.QMenu: ...
    # def minimumSizeHint(self) -> PySide6.QtCore.QSize: ...
    # def mouseMoveEvent(self, arg__1: PySide6.QtGui.QMouseEvent) -> None: ...
    # def paintEvent(self, arg__1: PySide6.QtGui.QPaintEvent) -> None: ...
    # def setAutoDefault(self, arg__1: bool) -> None: ...
    # def setDefault(self, arg__1: bool) -> None: ...
    # def setFlat(self, arg__1: bool) -> None: ...
    # def setMenu(self, menu: PySide6.QtWidgets.QMenu) -> None: ...
    # def showMenu(self) -> None: ...
    # def sizeHint(self) -> PySide6.QtCore.QSize: ...


class QLineEdit:
    """
    <hr>
    ![](buttons/line_edit.png)

    `QLineEdit` is a widget that allows the user to enter and edit text. It provides
    a single line for the user to type in text.

    Args:
        text (str): The initial text to display in the line edit.

    <hr>

    <h3>Signals</h3>
    <ul>
        <li> <code>cursorPositionChanged</code>: Emitted when the cursor position changes.</li>
        <li> <code>editingFinished</code>: Emitted when the editing is finished.</li>
        <li> <code>returnPressed</code>: Emitted when the return key is pressed.</li>
        <li> <code>textChanged</code>: Emitted when the text changes.</li>
        <li> <code>textEdited</code>: Emitted when the text is edited.</li>
    </ul>

    <h3>Methods</h3>
    <ul>
        <li><a href="#code.QtWidgets.QLineEdit.text"><code>text</code></a></li>
        <li><a href="#code.QtWidgets.QLineEdit.setText"><code>setText</code></a></li>
        <li><a href="#code.QtWidgets.QLineEdit.clear"><code>clear</code></a></li>
        <li><a href="#code.QtWidgets.QLineEdit.copy"><code>copy</code></a></li>
        <li><a href="#code.QtWidgets.QLineEdit.cut"><code>cut</code></a></li>
        <li><a href="#code.QtWidgets.QLineEdit.paste"><code>paste</code></a></li>
        <li><a href="#code.QtWidgets.QLineEdit.redo"><code>redo</code></a></li>
        <li><a href="#code.QtWidgets.QLineEdit.undo"><code>undo</code></a></li>
        <li><a href="#code.QtWidgets.QLineEdit.isModified"><code>isModified</code></a></li>
        <li><a href="#code.QtWidgets.QLineEdit.isReadOnly"><code>isReadOnly</code></a></li>
        <li><a href="#code.QtWidgets.QLineEdit.setReadOnly"><code>setReadOnly</code></a></li>
        <li><a href="#code.QtWidgets.QLineEdit.PlaceholderText"><code>PlaceholderText</code></a></li>
        <li><a href="#code.QtWidgets.QLineEdit.setPlaceholderText"><code>setPlaceholderText</code></a></li>
        <li><a href="#code.QtWidgets.QLineEdit.maxLength"><code>maxLength</code></a></li>
        <li><a href="#code.QtWidgets.QLineEdit.setMaxLength"><code>setMaxLength</code></a></li>
    </ul>


    <br>

    **Examples**
    <hr>
    ``` py
    line_edit = QtWidgets.QLineEdit("Enter text here")
    print(line_edit.text())
    print(line_edit.isModified())
    ```
    ```'Enter text here'``` <br>
    ```False``` <br> <br>
    Now the user modifies the text in the line edit to `'New text'`.
    ``` py
    print(line_edit.modified())
    print(line_edit.text())
    ```
    ```True``` <br>
    ```'New text'```

    <hr>

    <br>
    """

    cursorPositionChanged: ClassVar[Signal] = ...  # cursorPositionChanged(int,int)
    editingFinished: ClassVar[Signal] = ...  # editingFinished()
    #     inputRejected            : ClassVar[Signal] = ... # inputRejected()
    returnPressed: ClassVar[Signal] = ...  # returnPressed()
    #     selectionChanged: ClassVar[Signal] = ...  # selectionChanged()
    textChanged: ClassVar[Signal] = ...  # textChanged(QString)
    textEdited: ClassVar[Signal] = ...  # textEdited(QString)

    #     class ActionPosition(enum.Enum):

    #         LeadingPosition          : QLineEdit.ActionPosition = ... # 0x0
    #         TrailingPosition         : QLineEdit.ActionPosition = ... # 0x1

    #     class EchoMode(enum.Enum):

    #         Normal                   : QLineEdit.EchoMode = ... # 0x0
    #         NoEcho                   : QLineEdit.EchoMode = ... # 0x1
    #         Password                 : QLineEdit.EchoMode = ... # 0x2
    #         PasswordEchoOnEdit       : QLineEdit.EchoMode = ... # 0x3

    #     @overload
    def __init__(self, text: str = None) -> None: ...

    #     @overload
    #     def __init__(self, parent: Optional[PySide6.QtWidgets.QWidget] = ...) -> None: ...

    #     @overload
    #     def addAction(self, action: PySide6.QtGui.QAction) -> None: ...
    #     @overload
    #     def addAction(self, action: PySide6.QtGui.QAction, position: PySide6.QtWidgets.QLineEdit.ActionPosition) -> None: ...
    #     @overload
    #     def addAction(self, arg__1: PySide6.QtGui.QAction) -> None: ...
    #     @overload
    #     def addAction(self, icon: Union[PySide6.QtGui.QIcon, PySide6.QtGui.QPixmap], position: PySide6.QtWidgets.QLineEdit.ActionPosition) -> PySide6.QtGui.QAction: ...
    #     @overload
    #     def addAction(self, icon: Union[PySide6.QtGui.QIcon, PySide6.QtGui.QPixmap], text: str) -> PySide6.QtGui.QAction: ...
    #     @overload
    #     def addAction(self, icon: Union[PySide6.QtGui.QIcon, PySide6.QtGui.QPixmap], text: str, callable: object) -> PySide6.QtGui.QAction: ...
    #     @overload
    #     def addAction(self, icon: Union[PySide6.QtGui.QIcon, PySide6.QtGui.QPixmap], text: str, receiver: PySide6.QtCore.QObject, member: bytes, type: PySide6.QtCore.Qt.ConnectionType = ...) -> PySide6.QtGui.QAction: ...
    #     @overload
    #     def addAction(self, icon: Union[PySide6.QtGui.QIcon, PySide6.QtGui.QPixmap], text: str, shortcut: Union[PySide6.QtGui.QKeySequence, PySide6.QtCore.QKeyCombination, PySide6.QtGui.QKeySequence.StandardKey, str, int]) -> PySide6.QtGui.QAction: ...
    #     @overload
    #     def addAction(self, icon: Union[PySide6.QtGui.QIcon, PySide6.QtGui.QPixmap], text: str, shortcut: Union[PySide6.QtGui.QKeySequence, PySide6.QtCore.QKeyCombination, PySide6.QtGui.QKeySequence.StandardKey, str, int], callable: object) -> PySide6.QtGui.QAction: ...
    #     @overload
    #     def addAction(self, icon: Union[PySide6.QtGui.QIcon, PySide6.QtGui.QPixmap], text: str, shortcut: Union[PySide6.QtGui.QKeySequence, PySide6.QtCore.QKeyCombination, PySide6.QtGui.QKeySequence.StandardKey, str, int], receiver: PySide6.QtCore.QObject, member: bytes, type: PySide6.QtCore.Qt.ConnectionType = ...) -> PySide6.QtGui.QAction: ...
    #     @overload
    #     def addAction(self, text: str) -> PySide6.QtGui.QAction: ...
    #     @overload
    #     def addAction(self, text: str, callable: object) -> PySide6.QtGui.QAction: ...
    #     @overload
    #     def addAction(self, text: str, receiver: PySide6.QtCore.QObject, member: bytes, type: PySide6.QtCore.Qt.ConnectionType = ...) -> PySide6.QtGui.QAction: ...
    #     @overload
    #     def addAction(self, text: str, shortcut: Union[PySide6.QtGui.QKeySequence, PySide6.QtCore.QKeyCombination, PySide6.QtGui.QKeySequence.StandardKey, str, int]) -> PySide6.QtGui.QAction: ...
    #     @overload
    #     def addAction(self, text: str, shortcut: Union[PySide6.QtGui.QKeySequence, PySide6.QtCore.QKeyCombination, PySide6.QtGui.QKeySequence.StandardKey, str, int], callable: object) -> PySide6.QtGui.QAction: ...
    #     @overload
    #     def addAction(self, text: str, shortcut: Union[PySide6.QtGui.QKeySequence, PySide6.QtCore.QKeyCombination, PySide6.QtGui.QKeySequence.StandardKey, str, int], receiver: PySide6.QtCore.QObject, member: bytes, type: PySide6.QtCore.Qt.ConnectionType = ...) -> PySide6.QtGui.QAction: ...
    #     def alignment(self) -> PySide6.QtCore.Qt.AlignmentFlag: ...
    #     def backspace(self) -> None: ...
    #     def changeEvent(self, arg__1: PySide6.QtCore.QEvent) -> None: ...
    def clear(self) -> None:
        """
        Clear the text in the line edit.

        <br>
        """

    #     def completer(self) -> PySide6.QtWidgets.QCompleter: ...
    #     def contextMenuEvent(self, arg__1: PySide6.QtGui.QContextMenuEvent) -> None: ...
    def copy(self) -> None:
        """
        Copy the selected text in the line edit to the clipboard.

        <br>
        """

    #     def createStandardContextMenu(self) -> PySide6.QtWidgets.QMenu: ...
    #     def cursorBackward(self, mark: bool, steps: int = ...) -> None: ...
    #     def cursorForward(self, mark: bool, steps: int = ...) -> None: ...
    #     def cursorMoveStyle(self) -> PySide6.QtCore.Qt.CursorMoveStyle: ...
    #     def cursorPosition(self) -> int: ...
    #     def cursorPositionAt(self, pos: PySide6.QtCore.QPoint) -> int: ...
    #     def cursorRect(self) -> PySide6.QtCore.QRect: ...
    #     def cursorWordBackward(self, mark: bool) -> None: ...
    #     def cursorWordForward(self, mark: bool) -> None: ...
    def cut(self) -> None:
        """
        Cut the selected text in the line edit to the clipboard.

        <br>
        """

    #     def del_(self) -> None: ...
    #     def deselect(self) -> None: ...
    #     def displayText(self) -> str: ...
    #     def dragEnabled(self) -> bool: ...
    #     def dragEnterEvent(self, arg__1: PySide6.QtGui.QDragEnterEvent) -> None: ...
    #     def dragLeaveEvent(self, e: PySide6.QtGui.QDragLeaveEvent) -> None: ...
    #     def dragMoveEvent(self, e: PySide6.QtGui.QDragMoveEvent) -> None: ...
    #     def dropEvent(self, arg__1: PySide6.QtGui.QDropEvent) -> None: ...
    #     def echoMode(self) -> PySide6.QtWidgets.QLineEdit.EchoMode: ...
    #     def end(self, mark: bool) -> None: ...
    #     def event(self, arg__1: PySide6.QtCore.QEvent) -> bool: ...
    #     def focusInEvent(self, arg__1: PySide6.QtGui.QFocusEvent) -> None: ...
    #     def focusOutEvent(self, arg__1: PySide6.QtGui.QFocusEvent) -> None: ...
    #     def hasAcceptableInput(self) -> bool: ...
    #     def hasFrame(self) -> bool: ...
    #     def hasSelectedText(self) -> bool: ...
    #     def home(self, mark: bool) -> None: ...
    #     def initStyleOption(self, option: PySide6.QtWidgets.QStyleOptionFrame) -> None: ...
    #     def inputMask(self) -> str: ...
    #     def inputMethodEvent(self, arg__1: PySide6.QtGui.QInputMethodEvent) -> None: ...
    #     @overload
    #     def inputMethodQuery(self, arg__1: PySide6.QtCore.Qt.InputMethodQuery) -> Any: ...
    #     @overload
    #     def inputMethodQuery(self, property: PySide6.QtCore.Qt.InputMethodQuery, argument: Any) -> Any: ...
    #     def insert(self, arg__1: str) -> None: ...
    #     def isClearButtonEnabled(self) -> bool: ...
    def isModified(self) -> bool:
        """
        Check if the text in the line edit has been modified by the user.
        `setText` resets the modified flag.

        Returns:
            True if the text has been modified, False otherwise.
        <br>
        """

    def isReadOnly(self) -> bool:
        """
        Check if the line edit is read-only.

        Returns:
            True if the line edit is read-only, False otherwise.
        <br>
        """

    #     def isRedoAvailable(self) -> bool: ...
    #     def isUndoAvailable(self) -> bool: ...
    #     def keyPressEvent(self, arg__1: PySide6.QtGui.QKeyEvent) -> None: ...
    #     def keyReleaseEvent(self, arg__1: PySide6.QtGui.QKeyEvent) -> None: ...
    def maxLength(self) -> int:
        """
        Get the maximum length of the text in the line edit.

        Returns:
            The maximum length of the text in the line edit.
        <br>
        """

    #     def minimumSizeHint(self) -> PySide6.QtCore.QSize: ...
    #     def mouseDoubleClickEvent(self, arg__1: PySide6.QtGui.QMouseEvent) -> None: ...
    #     def mouseMoveEvent(self, arg__1: PySide6.QtGui.QMouseEvent) -> None: ...
    #     def mousePressEvent(self, arg__1: PySide6.QtGui.QMouseEvent) -> None: ...
    #     def mouseReleaseEvent(self, arg__1: PySide6.QtGui.QMouseEvent) -> None: ...
    #     def paintEvent(self, arg__1: PySide6.QtGui.QPaintEvent) -> None: ...
    def paste(self) -> None:
        """
        Paste the text from the clipboard to the line edit.

        <br>
        """

    def placeholderText(self) -> str:
        """
        Get the placeholder text displayed in the line edit when it is empty.

        Returns:
            The placeholder text.
        <br>
        """

    def redo(self) -> None:
        """
        Redo the last operation in the line edit.

        <br>
        """

    #     def selectAll(self) -> None: ...
    #     def selectedText(self) -> str: ...
    #     def selectionEnd(self) -> int: ...
    #     def selectionLength(self) -> int: ...
    #     def selectionStart(self) -> int: ...
    #     def setAlignment(self, flag: PySide6.QtCore.Qt.AlignmentFlag) -> None: ...
    #     def setClearButtonEnabled(self, enable: bool) -> None: ...
    #     def setCompleter(self, completer: PySide6.QtWidgets.QCompleter) -> None: ...
    #     def setCursorMoveStyle(self, style: PySide6.QtCore.Qt.CursorMoveStyle) -> None: ...
    #     def setCursorPosition(self, arg__1: int) -> None: ...
    #     def setDragEnabled(self, b: bool) -> None: ...
    #     def setEchoMode(self, arg__1: PySide6.QtWidgets.QLineEdit.EchoMode) -> None: ...
    #     def setFrame(self, arg__1: bool) -> None: ...
    #     def setInputMask(self, inputMask: str) -> None: ...
    def setMaxLength(self, length: int) -> None:
        """
        Set the maximum length of the text in the line edit.

        Args:
            length: The maximum length of the text in the line edit.
        <br>
        """

    #     def setModified(self, arg__1: bool) -> None: ...
    def setPlaceholderText(self, text: str) -> None:
        """
        Set the placeholder text displayed in the line edit when it is empty. The placeholder text is displayed in gray.

        Args:
            text (str): The placeholder text.
        <br>
        """

    def setReadOnly(self, read_only: bool) -> None:
        """
        Set the line edit to read-only. If the line edit is read-only, the user cannot edit the text.

        Args:
            read_only: True to set the line edit to read-only, False otherwise.
        <br>
        """

    #     def setSelection(self, arg__1: int, arg__2: int) -> None: ...
    def setText(self, text: str) -> None:
        """
        Set the content of the line edit to the specified text.

        Args:
            text (str): The text to set in the line edit.
        <br>
        """

    #     @overload
    #     def setTextMargins(self, left: int, top: int, right: int, bottom: int) -> None: ...
    #     @overload
    #     def setTextMargins(self, margins: PySide6.QtCore.QMargins) -> None: ...
    #     def setValidator(self, arg__1: PySide6.QtGui.QValidator) -> None: ...
    #     def sizeHint(self) -> PySide6.QtCore.QSize: ...
    def text(self) -> str:
        """
        Get the text in the line edit.

        Returns:
            The text in the line edit.
        <br>
        """

    #     def textMargins(self) -> PySide6.QtCore.QMargins: ...
    #     def timerEvent(self, arg__1: PySide6.QtCore.QTimerEvent) -> None: ...
    def undo(self) -> None:
        """
        Undo the last operation in the line edit.

        <br>
        <br>
        """


#     def validator(self) -> PySide6.QtGui.QValidator: ...


class QFileDialog:
    """

    <hr>

    `QFileDialog` provides a dialog that allows users to select files or directories.
    <hr>

    <h3>Methods</h3>
    <ul>
        <li><a href="#code.QtWidgets.QFileDialog.getSaveFileName"><code>getSaveFileName</code></a></li>
    </ul>

    <br>

    **Examples**
    <hr>

    ```py
    from PySide6 import QtWidgets
    from PySide6.QtCore import Slot


    app = QtWidgets.QApplication()
    window = QtWidgets.QMainWindow()

    @Slot()
    def save_file():
        # Get the filename selected by the user
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(filter="CSV files (*.csv)")

        # Save the data to this file
        with open(file_name, "w") as file:
            file.write(data)

    data = "1,2,3,4,5"
    button = QtWidgets.QPushButton("Save File")
    # A main window always requires a central widget
    window.setCentralWidget(button)
    button.clicked.connect(save_file)

    window.show()
    app.exec()
    ```
    The above example shows the shortest working code to save data to a CSV file.
    Running the code above will display a window with a [QPushButton](QPushButton.md) that allows the user to save the data (`"1,2,3,4,5"`) to a CSV file.
    <hr>
    <br>
    """

    #     currentChanged           : ClassVar[Signal] = ... # currentChanged(QString)
    #     currentUrlChanged        : ClassVar[Signal] = ... # currentUrlChanged(QUrl)
    #     directoryEntered         : ClassVar[Signal] = ... # directoryEntered(QString)
    #     directoryUrlEntered      : ClassVar[Signal] = ... # directoryUrlEntered(QUrl)
    #     fileSelected             : ClassVar[Signal] = ... # fileSelected(QString)
    #     filesSelected            : ClassVar[Signal] = ... # filesSelected(QStringList)
    #     filterSelected           : ClassVar[Signal] = ... # filterSelected(QString)
    #     urlSelected              : ClassVar[Signal] = ... # urlSelected(QUrl)
    #     urlsSelected             : ClassVar[Signal] = ... # urlsSelected(QList<QUrl>)

    #     class AcceptMode(enum.Enum):

    #         AcceptOpen               : QFileDialog.AcceptMode = ... # 0x0
    #         AcceptSave               : QFileDialog.AcceptMode = ... # 0x1

    #     class DialogLabel(enum.Enum):

    #         LookIn                   : QFileDialog.DialogLabel = ... # 0x0
    #         FileName                 : QFileDialog.DialogLabel = ... # 0x1
    #         FileType                 : QFileDialog.DialogLabel = ... # 0x2
    #         Accept                   : QFileDialog.DialogLabel = ... # 0x3
    #         Reject                   : QFileDialog.DialogLabel = ... # 0x4

    #     class FileMode(enum.Enum):

    #         AnyFile                  : QFileDialog.FileMode = ... # 0x0
    #         ExistingFile             : QFileDialog.FileMode = ... # 0x1
    #         Directory                : QFileDialog.FileMode = ... # 0x2
    #         ExistingFiles            : QFileDialog.FileMode = ... # 0x3

    #     class Option(enum.Flag):

    #         ShowDirsOnly             : QFileDialog.Option = ... # 0x1
    #         DontResolveSymlinks      : QFileDialog.Option = ... # 0x2
    #         DontConfirmOverwrite     : QFileDialog.Option = ... # 0x4
    #         DontUseNativeDialog      : QFileDialog.Option = ... # 0x8
    #         ReadOnly                 : QFileDialog.Option = ... # 0x10
    #         HideNameFilterDetails    : QFileDialog.Option = ... # 0x20
    #         DontUseCustomDirectoryIcons: QFileDialog.Option = ... # 0x40

    #     class ViewMode(enum.Enum):

    #         Detail                   : QFileDialog.ViewMode = ... # 0x0
    #         List                     : QFileDialog.ViewMode = ... # 0x1

    #     @overload
    #     def __init__(self, parent: PySide6.QtWidgets.QWidget, f: PySide6.QtCore.Qt.WindowType) -> None: ...
    #     @overload
    #     def __init__(self, parent: Optional[PySide6.QtWidgets.QWidget] = ..., caption: str = ..., directory: str = ..., filter: str = ...) -> None: ...

    #     def accept(self) -> None: ...
    #     def acceptMode(self) -> PySide6.QtWidgets.QFileDialog.AcceptMode: ...
    #     def changeEvent(self, e: PySide6.QtCore.QEvent) -> None: ...
    #     def defaultSuffix(self) -> str: ...
    #     def directory(self) -> PySide6.QtCore.QDir: ...
    #     def directoryUrl(self) -> PySide6.QtCore.QUrl: ...
    #     def done(self, result: int) -> None: ...
    #     def fileMode(self) -> PySide6.QtWidgets.QFileDialog.FileMode: ...
    #     def filter(self) -> PySide6.QtCore.QDir.Filter: ...
    #     @staticmethod
    #     def getExistingDirectory(parent: Optional[PySide6.QtWidgets.QWidget] = ..., caption: str = ..., dir: str = ..., options: PySide6.QtWidgets.QFileDialog.Option = ...) -> str: ...
    #     @staticmethod
    #     def getExistingDirectoryUrl(parent: Optional[PySide6.QtWidgets.QWidget] = ..., caption: str = ..., dir: Union[PySide6.QtCore.QUrl, str] = ..., options: PySide6.QtWidgets.QFileDialog.Option = ..., supportedSchemes: Sequence[str] = ...) -> PySide6.QtCore.QUrl: ...
    #     @staticmethod
    #     def getOpenFileName(parent: PySide6.QtWidgets.QWidget, caption: Optional[str] = ..., dir: str = ..., filter: str = ..., selectedFilter: str = ..., options: PySide6.QtWidgets.QFileDialog.Option = ...) -> Tuple[str, str]: ...
    #     @staticmethod
    #     def getOpenFileNames(parent: PySide6.QtWidgets.QWidget, caption: Optional[str] = ..., dir: str = ..., filter: str = ..., selectedFilter: str = ..., options: PySide6.QtWidgets.QFileDialog.Option = ...) -> Tuple[List[str], str]: ...
    #     @staticmethod
    #     def getOpenFileUrl(parent: PySide6.QtWidgets.QWidget, caption: Optional[str] = ..., dir: Union[PySide6.QtCore.QUrl, str] = ..., filter: str = ..., selectedFilter: str = ..., options: PySide6.QtWidgets.QFileDialog.Option = ..., supportedSchemes: Sequence[str] = ...) -> Tuple[PySide6.QtCore.QUrl, str]: ...
    #     @staticmethod
    #     def getOpenFileUrls(parent: PySide6.QtWidgets.QWidget, caption: Optional[str] = ..., dir: Union[PySide6.QtCore.QUrl, str] = ..., filter: str = ..., selectedFilter: str = ..., options: PySide6.QtWidgets.QFileDialog.Option = ..., supportedSchemes: Sequence[str] = ...) -> Tuple[List[PySide6.QtCore.QUrl], str]: ...
    @staticmethod
    def getSaveFileName(
        caption: Optional[str] = None, dir: str = None, filter: str = None
    ) -> Tuple[str, str]:
        """
        Opens a dialog for saving a file. The dialog is displayed as a modal
        dialog and returns the selected file name and filter.

        Args:
            caption (str): The dialog caption.
            dir (str): The initial directory.
            filter (str): The file filter. Generally, this is a string like
                "Image files (*.png *.jpg)" or "Text files (*.txt);;CSV files (*.csv)",
                where multiple filters are separated by two semicolons.

        Returns:
            A tuple containing the selected file name and filter.
        <br>
        <br>
        """


#     @staticmethod
#     def getSaveFileUrl(parent: PySide6.QtWidgets.QWidget, caption: Optional[str] = ..., dir: Union[PySide6.QtCore.QUrl, str] = ..., filter: str = ..., selectedFilter: str = ..., options: PySide6.QtWidgets.QFileDialog.Option = ..., supportedSchemes: Sequence[str] = ...) -> Tuple[PySide6.QtCore.QUrl, str]: ...
#     def history(self) -> List[str]: ...
#     def iconProvider(self) -> PySide6.QtGui.QAbstractFileIconProvider: ...
#     def itemDelegate(self) -> PySide6.QtWidgets.QAbstractItemDelegate: ...
#     def labelText(self, label: PySide6.QtWidgets.QFileDialog.DialogLabel) -> str: ...
#     def mimeTypeFilters(self) -> List[str]: ...
#     def nameFilters(self) -> List[str]: ...
#     @overload
#     def open(self) -> None: ...
#     @overload
#     def open(self, receiver: PySide6.QtCore.QObject, member: bytes) -> None: ...
#     def options(self) -> PySide6.QtWidgets.QFileDialog.Option: ...
#     def proxyModel(self) -> PySide6.QtCore.QAbstractProxyModel: ...
#     def restoreState(self, state: Union[PySide6.QtCore.QByteArray, bytes]) -> bool: ...
#     @staticmethod
#     def saveFileContent(fileContent: Union[PySide6.QtCore.QByteArray, bytes], fileNameHint: str = ...) -> None: ...
#     def saveState(self) -> PySide6.QtCore.QByteArray: ...
#     def selectFile(self, filename: str) -> None: ...
#     def selectMimeTypeFilter(self, filter: str) -> None: ...
#     def selectNameFilter(self, filter: str) -> None: ...
#     def selectUrl(self, url: Union[PySide6.QtCore.QUrl, str]) -> None: ...
#     def selectedFiles(self) -> List[str]: ...
#     def selectedMimeTypeFilter(self) -> str: ...
#     def selectedNameFilter(self) -> str: ...
#     def selectedUrls(self) -> List[PySide6.QtCore.QUrl]: ...
#     def setAcceptMode(self, mode: PySide6.QtWidgets.QFileDialog.AcceptMode) -> None: ...
#     def setDefaultSuffix(self, suffix: str) -> None: ...
#     @overload
#     def setDirectory(self, directory: str) -> None: ...
#     @overload
#     def setDirectory(self, directory: Union[PySide6.QtCore.QDir, str]) -> None: ...
#     def setDirectoryUrl(self, directory: Union[PySide6.QtCore.QUrl, str]) -> None: ...
#     def setFileMode(self, mode: PySide6.QtWidgets.QFileDialog.FileMode) -> None: ...
#     def setFilter(self, filters: PySide6.QtCore.QDir.Filter) -> None: ...
#     def setHistory(self, paths: Sequence[str]) -> None: ...
#     def setIconProvider(self, provider: PySide6.QtGui.QAbstractFileIconProvider) -> None: ...
#     def setItemDelegate(self, delegate: PySide6.QtWidgets.QAbstractItemDelegate) -> None: ...
#     def setLabelText(self, label: PySide6.QtWidgets.QFileDialog.DialogLabel, text: str) -> None: ...
#     def setMimeTypeFilters(self, filters: Sequence[str]) -> None: ...
#     def setNameFilter(self, filter: str) -> None: ...
#     def setNameFilters(self, filters: Sequence[str]) -> None: ...
#     def setOption(self, option: PySide6.QtWidgets.QFileDialog.Option, on: bool = ...) -> None: ...
#     def setOptions(self, options: PySide6.QtWidgets.QFileDialog.Option) -> None: ...
#     def setProxyModel(self, model: PySide6.QtCore.QAbstractProxyModel) -> None: ...
#     def setSidebarUrls(self, urls: Sequence[PySide6.QtCore.QUrl]) -> None: ...
#     def setSupportedSchemes(self, schemes: Sequence[str]) -> None: ...
#     def setViewMode(self, mode: PySide6.QtWidgets.QFileDialog.ViewMode) -> None: ...
#     def setVisible(self, visible: bool) -> None: ...
#     def sidebarUrls(self) -> List[PySide6.QtCore.QUrl]: ...
#     def supportedSchemes(self) -> List[str]: ...
#     def testOption(self, option: PySide6.QtWidgets.QFileDialog.Option) -> bool: ...
#     def viewMode(self) -> PySide6.QtWidgets.QFileDialog.ViewMode: ...
