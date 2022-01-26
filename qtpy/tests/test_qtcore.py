"""Test QtCore."""

from datetime import datetime
import os
import sys

import pytest

from qtpy import PYQT5, PYQT6, PYSIDE2, PYSIDE6, PYQT_VERSION, PYSIDE_VERSION, QtCore


def test_qtmsghandler():
    """Test qtpy.QtMsgHandler"""
    assert QtCore.qInstallMessageHandler is not None


def test_qdatetime_toPython():
    """Test QDateTime.toPython"""
    q_date = QtCore.QDateTime.currentDateTime()
    assert QtCore.QDateTime.toPython is not None
    py_date = q_date.toPython()
    assert isinstance(py_date, datetime)


@pytest.mark.skipif(sys.platform.startswith('linux') and os.environ.get('USE_CONDA', 'No') == 'No',
                    reason="Fatal Python error: Aborted on Linux CI when not using conda")
def test_qeventloop_exec_(qtbot):
    """Test QEventLoop.exec_"""
    assert QtCore.QEventLoop.exec_ is not None
    event_loop = QtCore.QEventLoop(None)
    QtCore.QTimer.singleShot(100, event_loop.quit)
    event_loop.exec_()


def test_qthread_exec_():
    """Test QThread.exec_"""
    assert QtCore.QThread.exec_ is not None


def test_qlibraryinfo_location():
    """Test QLibraryInfo.location"""
    assert QtCore.QLibraryInfo.location is not None
    assert QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.PrefixPath) is not None


def test_qtextstreammanipulator_exec_():
    """Test QTextStreamManipulator.exec_"""
    QtCore.QTextStreamManipulator.exec_ is not None


@pytest.mark.skipif(PYSIDE2 or PYQT6,
                    reason="Doesn't seem to be present on PySide2 and PyQt6")
def test_QtCore_SignalInstance():
    class ClassWithSignal(QtCore.QObject):
        signal = QtCore.Signal()

    instance = ClassWithSignal()

    assert isinstance(instance.signal, QtCore.SignalInstance)


@pytest.mark.skipif(PYQT5 and PYQT_VERSION.startswith('5.9'),
                    reason="A specific setup with at least sip 4.9.9 is needed for PyQt5 5.9.*"
                           "to work with scoped enum access")
def test_enum_access():
    """Test scoped and unscoped enum access for qtpy.QtCore.*."""
    assert QtCore.QAbstractAnimation.Stopped == QtCore.QAbstractAnimation.State.Stopped
    assert QtCore.QEvent.ActionAdded == QtCore.QEvent.Type.ActionAdded
    assert QtCore.Qt.AlignLeft == QtCore.Qt.AlignmentFlag.AlignLeft
    assert QtCore.Qt.Key_Return == QtCore.Qt.Key.Key_Return
    assert QtCore.Qt.transparent == QtCore.Qt.GlobalColor.transparent
    assert QtCore.Qt.Widget == QtCore.Qt.WindowType.Widget
    assert QtCore.Qt.BackButton == QtCore.Qt.MouseButton.XButton1
    assert QtCore.Qt.XButton1 == QtCore.Qt.MouseButton.XButton1
    assert QtCore.Qt.BackgroundColorRole == QtCore.Qt.ItemDataRole.BackgroundColorRole
    assert QtCore.Qt.TextColorRole == QtCore.Qt.ItemDataRole.TextColorRole
    if PYSIDE2 or PYSIDE6:
        assert QtCore.Qt.MidButton == QtCore.Qt.MouseButton.MiddleButton


@pytest.mark.skipif(PYSIDE2 and PYSIDE_VERSION.startswith('5.12.0'),
                    reason="Utility functions unavailable for PySide2 5.12.0")
def test_qtgui_namespace_mightBeRichText():
    """
    Test included elements (mightBeRichText) from module QtGui.

    See: https://doc.qt.io/qt-5/qt-sub-qtgui.html
    """
    assert QtCore.Qt.mightBeRichText is not None
