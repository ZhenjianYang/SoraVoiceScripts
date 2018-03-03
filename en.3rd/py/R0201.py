from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R0201   ._SN',
        MapName             = 'Rolent',
        Location            = 'R0201.x',
        MapIndex            = 22,
        MapDefaultBGM       = "ed60029",
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
        'Joshua',                               # 9
        'Target Camera',                        # 10
        'Fog Adjustment',                       # 11
        'Rolent',                               # 12
        'Verte Bridge - Checkpoint',            # 13
        'Perzel Farm',                          # 14
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02750 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH02750P._CP',             # 00
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -131580,
        Z                   = 0,
        Y                   = -18130,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -224350,
        Z                   = 20,
        Y                   = -16180,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -184980,
        Z                   = 0,
        Y                   = -81290,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -179550,
        TriggerZ            = 0,
        TriggerY            = -15360,
        TriggerRange        = 1500,
        ActorX              = -179550,
        ActorZ              = 1500,
        ActorY              = -15360,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_196",          # 00, 0
        "Function_1_1B5",          # 01, 1
        "Function_2_1C8",          # 02, 2
        "Function_3_1DE",          # 03, 3
        "Function_4_A10",          # 04, 4
        "Function_5_A71",          # 05, 5
    )


    def Function_0_196(): pass

    label("Function_0_196")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B4")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)

    label("loc_1B4")

    Return()

    # Function_0_196 end

    def Function_1_1B5(): pass

    label("Function_1_1B5")

    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    Return()

    # Function_1_1B5 end

    def Function_2_1C8(): pass

    label("Function_2_1C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1DD")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_1C8")

    label("loc_1DD")

    Return()

    # Function_2_1C8 end

    def Function_3_1DE(): pass

    label("Function_3_1DE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0 op#A op#5
        "\x18\x07\x00#35A#40WSeveral weeks later...\x05\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1500)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x00Several peaceful weeks passed.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x00Joshua's injuries continued to heal, and it wasn't\x01",
            "long before he was able to walk with ease again.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "\x07\x00Estelle was jumping for joy at this fact, using it as\x01",
            "an excuse to drag him out to play with her at every\x01",
            "possible opportunity.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x00For him, however, it meant more than deciding what\x01",
            "game to play next--he had to decide what course of\x01",
            "action he was to take.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x00The time for him to make his choice was drawing\x01",
            "near...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_C4(0x1, 0x800)
    Sleep(1000)
    OP_1D(0x58)
    OP_6D(-152800, 0, -17910, 0)
    OP_67(0, 8980, -10000, 0)
    OP_6B(3810, 0)
    OP_6C(237000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x101, -148950, 0, -17700, 270)
    SetChrPos(0x10, -147000, 0, -17700, 270)
    OP_43(0x101, 0x3, 0x0, 0x4)
    OP_43(0x10, 0x3, 0x0, 0x4)

    def lambda_4A9():
        OP_6D(-179410, 0, -15260, 10000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_4A9)

    def lambda_4C1():
        OP_67(0, 5500, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4C1)

    def lambda_4D9():
        OP_6B(2900, 10000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_4D9)
    FadeToBright(3000, 0)
    OP_0D()
    WaitChrThread(0x11, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x10, 0xFF)
    SetChrPos(0x101, -171150, 0, -10350, 240)
    SetChrPos(0x10, -170520, 0, -9030, 240)

    def lambda_522():
        OP_8E(0xFE, 0xFFFD4A86, 0xFFFFFFF6, 0xFFFFC752, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_522)
    Sleep(100)

    def lambda_542():
        OP_8E(0xFE, 0xFFFD4B76, 0xFFFFFFF6, 0xFFFFCB8A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_542)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x10, 0x1)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #6
        "\x07\x05South: Perzel Farm\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #7
        0x10,
        (
            "#1678F#6PPerzel?\x02\x03",

            "#1676FThat's the short-haired girl's last name,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(    #8
        0x101,
        (
            "#290F#5PUh-huh! This is where Tio lives.\x02\x03",

            "Guess what, though?\x02\x03",

            "#291FHer mom had twins!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)
    Sleep(300)

    ChrTalk(    #9
        0x10,
        (
            "#1677F#12P...As if I needed to guess anything. You wouldn't\x01",
            "shut up about it when you first heard the news.\x02\x03",

            "#1671FYou've also been to see them over and over as it\x01",
            "is... Are they still exciting enough to want to keep\x01",
            "visiting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#291F#5POh, we're not here to visit them today.\x01",
            "We're here to help at the farm!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #11
        0x101,
        (
            "#290F#5PRight now, it's harvesting time.\x02\x03",

            "But Miss Hannah's kind of stuck with the babies,\x01",
            "so they need some help.\x02\x03",

            "#291FAnd when Elissa told me about it, I wanted that\x01",
            "help to be ME.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        (
            "#1677F#12P...Well, it's nice of you to offer...\x02\x03",

            "#1675F...but why do I have to come, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#292F#5PBecause I said so. No complaining!\x02\x03",

            "Let's gooo!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_91C():
        OP_8E(0xFE, 0xFFFD4AEA, 0xFFFFFFF6, 0xFFFFC93C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_91C)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 180, 500)

    def lambda_943():
        OP_8E(0xFE, 0xFFFD4AEA, 0xFFFFFFF6, 0xFFFFA22C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_943)

    def lambda_95E():
        OP_8E(0xFE, 0xFFFD4B76, 0xFFFFFFF6, 0xFFFFA47A, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_95E)
    Sleep(400)

    ChrTalk(    #14 op#A
        0x101,
        "#294F#2P#15AThis is part of your rear-hillbilly process!\x02",
    )

    Sleep(1800)

    ChrTalk(    #15 op#A
        0x10,
        "#1677F#4P#20A...I told you, it's 'rehabilitation.'\x02",
    )

    Sleep(1800)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    NewScene("ED6_DT21/T0400   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_1DE end

    def Function_4_A10(): pass

    label("Function_4_A10")


    def lambda_A16():
        OP_8E(0xFE, 0xFFFDA0BC, 0x0, 0xFFFFBADC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A16)
    WaitChrThread(0xFE, 0x1)

    def lambda_A36():
        OP_8E(0xFE, 0xFFFD93E2, 0xA, 0xFFFFCBBC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A36)
    WaitChrThread(0xFE, 0x1)

    def lambda_A56():
        OP_8E(0xFE, 0xFFFD6A0C, 0x0, 0xFFFFCBBC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A56)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_4_A10 end

    def Function_5_A71(): pass

    label("Function_5_A71")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #16
        "\x07\x05South: Perzel Farm\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_5_A71 end

    SaveToFile()

Try(main)
