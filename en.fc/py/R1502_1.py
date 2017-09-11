from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R1502_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'R1502.x',
        MapIndex            = 59,
        MapDefaultBGM       = "ed60022",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
    )

    ScpFunction(
        "Function_0_66",           # 00, 0
        "Function_1_5F5",          # 01, 1
    )


    def Function_0_66(): pass

    label("Function_0_66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F4")
    EventBegin(0x0)
    OP_22(0x85, 0x1, 0x55)
    SetChrPos(0x8, -75050, -2009, -3930, 106)
    TurnDirection(0x0, 0x8, 0)
    TurnDirection(0x1, 0x8, 0)
    TurnDirection(0x2, 0x8, 0)
    Sleep(300)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(1000)
    LoadEffect(0x0, "map\\\\mp023_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -75080, -50, -3790, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x101, -71140, -60, -3530, 290)
    SetChrPos(0x103, -70970, -20, -4830, 290)
    SetChrPos(0x102, -69490, -80, -4330, 290)
    SetChrChipByIndex(0x103, 5)
    SetChrChipByIndex(0x102, 4)
    SetChrChipByIndex(0x101, 3)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1A0():
        OP_6C(250000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1A0)

    def lambda_1B0():
        OP_6D(-75050, 10, -3930, 5000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_1B0)
    Sleep(3000)

    def lambda_1CD():
        OP_6B(2800, 6000)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_1CD)

    def lambda_1DD():
        OP_67(0, 6510, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x2, 3, lambda_1DD)
    OP_24(0x85, 0x64)
    PlayEffect(0x0, 0x1, 0xFF, -75080, -50, -3790, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)

    def lambda_22E():
        OP_8F(0x8, 0xFFFEDAD6, 0xA, 0xFFFFF0A6, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_22E)

    def lambda_249():
        OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_249)
    OP_43(0x8, 0x0, 0x0, 0x2)
    WaitChrThread(0x8, 0x3)
    OP_82(0x1, 0x2)
    OP_82(0x0, 0x2)
    OP_24(0x85, 0x50)
    Sleep(1000)
    OP_6A(0x8)
    OP_43(0x8, 0x0, 0x1, 0x1)
    Sleep(200)
    Sleep(800)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x8, 0x2)
    WaitChrThread(0x8, 0x3)
    OP_44(0x8, 0xFF)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    OP_6A(0x0)
    ClearMapFlags(0x1)
    OP_23(0x85)
    OP_82(0x0, 0x2)
    OP_84(0x0)
    Battle(0x3EE, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_2CC"),
        (SWITCH_DEFAULT, "loc_2CF"),
    )


    label("loc_2CC")

    OP_B4(0x0)
    Return()

    label("loc_2CF")

    EventBegin(0x0)
    OP_66(0x1)
    OP_6D(-71660, -90, -2720, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -72450, -70, -2130, 315)
    SetChrPos(0x103, -71630, -90, -4019, 315)
    SetChrPos(0x102, -70980, 10, -2250, 315)
    SetChrFlags(0x8, 0x80)
    OP_0D()
    Sleep(400)
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #0
        0x101,
        (
            "#004FYikes! That scared the heck\x01",
            "out of me.\x02\x03",

            "I wasn't expecting a monster to\x01",
            "pop out like that...\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x102, 65535)

    def lambda_3D2():
        TurnDirection(0x102, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3D2)
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #1
        0x103,
        (
            "#022FIt looks like it followed the sound of\x01",
            "our footsteps and then attacked us.\x02\x03",

            "It almost caught us completely\x01",
            "off guard too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(    #2
        0x102,
        (
            "#012FIf it had attacked one of the villagers,\x01",
            "who knows what might have happened.\x02\x03",

            "It's a good thing we took care of it\x01",
            "before anyone else ran into it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 400)

    ChrTalk(    #3
        0x103,
        (
            "#020FAgreed...\x02\x03",

            "Anyway, we should get back and\x01",
            "report to the village elder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x102,
        "#010FRight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        "#000FOkay, let's go.\x02",
    )

    CloseMessageWindow()
    OP_28(0xE, 0x4, 0x10)
    OP_28(0xE, 0x1, 0x8)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00Quest \x07\x02[Ravennue Monster] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)

    label("loc_5F4")

    Return()

    # Function_0_66 end

    def Function_1_5F5(): pass

    label("Function_1_5F5")

    SetChrChipByIndex(0x8, 2)
    OP_22(0x23B, 0x0, 0x64)
    OP_24(0x85, 0x46)

    def lambda_609():
        OP_96(0x8, 0xFFFECDF2, 0xFFFFFFB0, 0xFFFFF2B8, 0x3E8, 0x9C4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_609)

    def lambda_627():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_627)
    OP_99(0x8, 0x0, 0x0, 0x0)
    Sleep(20)
    OP_99(0x8, 0x1, 0x1, 0x0)
    Sleep(20)
    OP_99(0x8, 0x2, 0x2, 0x0)
    Sleep(20)
    OP_99(0x8, 0x3, 0x3, 0x0)
    WaitChrThread(0x8, 0x3)
    OP_99(0x8, 0x0, 0x0, 0x0)
    OP_22(0x23B, 0x0, 0x64)
    OP_24(0x85, 0x46)

    def lambda_681():
        OP_96(0x8, 0xFFFED09A, 0x7D0, 0xFFFFFCCC, 0x898, 0x36B0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_681)
    OP_99(0x8, 0x0, 0x0, 0x0)
    Sleep(20)
    OP_99(0x8, 0x1, 0x1, 0x0)
    Sleep(20)
    OP_99(0x8, 0x2, 0x2, 0x0)
    Sleep(20)
    OP_99(0x8, 0x3, 0x3, 0x0)
    WaitChrThread(0x8, 0x3)
    OP_99(0x8, 0x0, 0x0, 0x0)
    OP_22(0x23B, 0x0, 0x64)
    OP_24(0x85, 0x3C)

    def lambda_6E9():
        OP_96(0x8, 0xFFFEE814, 0x1388, 0xFFFFF448, 0x1450, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_6E9)
    OP_99(0x8, 0x0, 0x0, 0x0)
    Sleep(20)
    OP_99(0x8, 0x1, 0x1, 0x0)
    Sleep(20)
    OP_99(0x8, 0x2, 0x2, 0x0)
    Sleep(20)
    OP_99(0x8, 0x3, 0x3, 0x0)
    Return()

    # Function_1_5F5 end

    SaveToFile()

Try(main)
