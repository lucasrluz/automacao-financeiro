import QtQuick.Controls
import QtQuick.Controls.Material
import QtQuick

ApplicationWindow {
    visible: true
    width: 500
    height: 700
    font.pixelSize: 16
    Material.theme: Material.Dark

    Rectangle {
        color: '#000000ff'
        width: parent.width - 20
        height: parent.height - 20
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter

        Label {
            id: 'novo_saque_label'
            text: 'Novo Saque'
            anchors.horizontalCenter: parent.horizontalCenter 
        }

        Label {
            id: 'init_date_label'
            text: 'Data Inicial'
            anchors.top: novo_saque_label.bottom
            anchors.left: parent.left
            anchors.topMargin: 20
        }

        TextField {
            id: 'init_date_text_field'
            placeholderText: 'dd/mm/yyyy'
            width: parent.width
            height: 50
            anchors.top: init_date_label.bottom
            anchors.horizontalCenter: parent.horizontalCenter
        }

        Label {
            id: 'end_date_label'
            text: 'Data Final'
            anchors.top: init_date_text_field.bottom
            anchors.left: parent.left
            anchors.topMargin: 20
        }

        TextField {
            id: 'end_date_text_field'
            placeholderText: 'dd/mm/yyyy'
            width: parent.width
            height: 50
            anchors.top: end_date_label.bottom
            anchors.horizontalCenter: parent.horizontalCenter
        }

		    Label {
            id: 'email_for_report_label'
            text: 'E-mail'
            anchors.top: end_date_text_field.bottom
            anchors.left: parent.left
            anchors.topMargin: 20
        }

        TextField {
            id: 'email_for_report_text_field'
            placeholderText: 'E-mail'
            width: parent.width
            height: 50
            anchors.top: email_for_report_label.bottom
            anchors.horizontalCenter: parent.horizontalCenter
        }

        Button {
            id: 'submit_button'
            text: 'Solicitar'
            width: parent.width
            height: 50
            anchors.top: email_for_report_text_field.bottom
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.topMargin: 20
        }
    }
}