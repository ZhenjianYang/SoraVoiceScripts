from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1123   ._SN',
        MapName             = 'Bose',
        Location            = 'T1123.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
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
        'Scherazard',                           # 9
        'Olivier',                              # 10
        'Kloe',                                 # 11
        'Tita',                                 # 12
        'Zin',                                  # 13
        'Mayor Maybelle',                       # 14
        'Lila',                                 # 15
        'Buck',                                 # 16
        'Trayton',                              # 17
        'Citizen',                              # 18
        'Citizen',                              # 19
        'Citizen',                              # 20
        'Citizen',                              # 21
        'Citizen',                              # 22
        'Citizen',                              # 23
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
        'ED6_DT07/CH00020 ._CH',             # 00
        'ED6_DT07/CH00030 ._CH',             # 01
        'ED6_DT07/CH00040 ._CH',             # 02
        'ED6_DT07/CH00060 ._CH',             # 03
        'ED6_DT07/CH00070 ._CH',             # 04
        'ED6_DT07/CH02360 ._CH',             # 05
        'ED6_DT26/CH20360 ._CH',             # 06
        'ED6_DT07/CH01140 ._CH',             # 07
        'ED6_DT07/CH01040 ._CH',             # 08
        'ED6_DT26/CH20342 ._CH',             # 09
        'ED6_DT07/CH01220 ._CH',             # 0A
        'ED6_DT07/CH01460 ._CH',             # 0B
        'ED6_DT07/CH01130 ._CH',             # 0C
        'ED6_DT07/CH01680 ._CH',             # 0D
        'ED6_DT07/CH01690 ._CH',             # 0E
        'ED6_DT06/CH20118 ._CH',             # 0F
        'ED6_DT07/CH00021 ._CH',             # 10
        'ED6_DT07/CH00031 ._CH',             # 11
        'ED6_DT07/CH00041 ._CH',             # 12
        'ED6_DT07/CH00061 ._CH',             # 13
        'ED6_DT07/CH00071 ._CH',             # 14
    )

    AddCharChipPat(
        'ED6_DT07/CH00020P._CP',             # 00
        'ED6_DT07/CH00030P._CP',             # 01
        'ED6_DT07/CH00040P._CP',             # 02
        'ED6_DT07/CH00060P._CP',             # 03
        'ED6_DT07/CH00070P._CP',             # 04
        'ED6_DT07/CH02360P._CP',             # 05
        'ED6_DT26/CH20360P._CP',             # 06
        'ED6_DT07/CH01140P._CP',             # 07
        'ED6_DT07/CH01040P._CP',             # 08
        'ED6_DT26/CH20342P._CP',             # 09
        'ED6_DT07/CH01220P._CP',             # 0A
        'ED6_DT07/CH01460P._CP',             # 0B
        'ED6_DT07/CH01130P._CP',             # 0C
        'ED6_DT07/CH01680P._CP',             # 0D
        'ED6_DT07/CH01690P._CP',             # 0E
        'ED6_DT06/CH20118P._CP',             # 0F
        'ED6_DT07/CH00021P._CP',             # 10
        'ED6_DT07/CH00031P._CP',             # 11
        'ED6_DT07/CH00041P._CP',             # 12
        'ED6_DT07/CH00061P._CP',             # 13
        'ED6_DT07/CH00071P._CP',             # 14
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_332",          # 00, 0
        "Function_1_34F",          # 01, 1
        "Function_2_374",          # 02, 2
        "Function_3_1490",         # 03, 3
        "Function_4_14A5",         # 04, 4
        "Function_5_14C9",         # 05, 5
        "Function_6_14ED",         # 06, 6
        "Function_7_152A",         # 07, 7
        "Function_8_1567",         # 08, 8
        "Function_9_15A4",         # 09, 9
        "Function_10_15D9",        # 0A, 10
        "Function_11_1602",        # 0B, 11
        "Function_12_1627",        # 0C, 12
        "Function_13_165C",        # 0D, 13
        "Function_14_16A5",        # 0E, 14
    )


    def Function_0_332(): pass

    label("Function_0_332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_34E")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_34E")

    Return()

    # Function_0_332 end

    def Function_1_34F(): pass

    label("Function_1_34F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_373")
    OP_72(0x0, 0x10)
    OP_72(0x1, 0x10)
    OP_6F(0x0, 29)
    OP_6F(0x1, 29)

    label("loc_373")

    Return()

    # Function_1_34F end

    def Function_2_374(): pass

    label("Function_2_374")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x4)
    SetChrPos(0xD, -1910, -1000, -5900, 90)
    SetChrPos(0xE, 160, -1400, -5250, 90)
    SetChrPos(0xF, -720, -1000, -3310, 135)
    SetChrPos(0x10, -1340, -1000, -4540, 90)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 6)
    SetChrSubChip(0xE, 10)
    SetChrPos(0x11, -20430, 0, 440, 270)
    SetChrPos(0x12, -20190, 0, 1910, 270)
    SetChrPos(0x13, -18990, 0, 1800, 270)
    SetChrPos(0x14, -17990, 0, 1380, 270)
    SetChrPos(0x15, -17170, 0, -470, 270)
    SetChrPos(0x16, -17100, 0, 200, 270)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    OP_43(0x11, 0x1, 0x0, 0x9)
    OP_43(0x13, 0x1, 0x0, 0xA)
    OP_43(0x15, 0x1, 0x0, 0xB)
    OP_6D(-13970, 0, 14660, 0)
    OP_67(0, 11740, -10000, 0)
    OP_6B(1780, 0)
    OP_6C(56000, 0)
    OP_6E(367, 0)
    FadeToBright(1500, 0)

    def lambda_4F9():
        OP_6D(-17870, 0, 1730, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4F9)

    def lambda_511():
        OP_67(0, 9280, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_511)

    def lambda_529():
        OP_6B(1940, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_529)

    def lambda_539():
        OP_6C(68000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_539)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(100)
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(100)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(100)
    OP_62(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(100)
    OP_62(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(9600, 0, 14190, 0)
    OP_67(0, 10090, -10000, 0)
    OP_6B(1940, 0)
    OP_6C(30000, 0)
    OP_6E(367, 0)

    def lambda_603():
        OP_6D(-400, 0, -5770, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_603)

    def lambda_61B():
        OP_6C(33000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_61B)
    Sleep(2500)
    OP_62(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(50)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(50)
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)
    OP_63(0xF)
    OP_63(0x10)
    OP_63(0xD)
    SetChrPos(0x101, -3100, 0, 12790, 180)
    SetChrPos(0x8, -4530, 0, 12880, 180)
    SetChrPos(0xA, -4370, 0, 14000, 180)
    SetChrPos(0xB, -5270, 0, 13810, 180)
    SetChrPos(0x9, -3500, 0, 14100, 180)
    SetChrPos(0xC, -2550, 0, 14100, 180)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Fade(500)
    OP_6D(-3240, 0, 14240, 0)
    OP_67(0, 8200, -10000, 0)
    OP_6B(1940, 0)
    OP_6C(33000, 0)
    OP_6E(367, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x101,
        "#1020F#5PThis is awful...!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "Start Rescuing People Immediately\x01",      # 0
            "Organize First\x01",                         # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7E1"),
        (1, "loc_B92"),
        (SWITCH_DEFAULT, "loc_E93"),
    )


    label("loc_7E1")


    ChrTalk(    #1
        0x101,
        (
            "#1005F#5PW-We've got to do something!\x01",
            "C'mon!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 600)

    def lambda_820():
        OP_8E(0xFE, 0xFFFFF3E4, 0x0, 0x2E18, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_820)
    Sleep(100)

    ChrTalk(    #2
        0x9,
        (
            "#530F#6PWait, Estelle!\x02\x03",

            "We must not rush in blindly!\x01",
            "We must organize our efforts first!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x9, 500)

    ChrTalk(    #3
        0x101,
        "#1026F#2PWh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x9,
        (
            "#030F#6PFrom the looks of it,\x01",
            "two areas need the most focus.\x02\x03",

            "It would be best for us to split\x01",
            "into two groups.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        "#1002F#2PR-Right.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 500)
    Sleep(400)

    ChrTalk(    #6
        0x8,
        (
            "#022F#2PKloe, Tita, with me!\x02\x03",

            "We'll guide the people who didn't get out\x01",
            "in time over by the west exit.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9C2():
        OP_8C(0xC, 225, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_9C2)

    def lambda_9D0():
        OP_8C(0x9, 225, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9D0)
    OP_8C(0x101, 270, 400)

    ChrTalk(    #7
        0xA,
        "#042F#6PYes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xB,
        "#062F#5PC-Coming!\x02",
    )

    CloseMessageWindow()

    def lambda_A0E():
        OP_6D(-4420, 0, 13210, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A0E)
    OP_43(0x8, 0x1, 0x0, 0x6)
    Sleep(500)
    OP_43(0xB, 0x1, 0x0, 0x7)
    Sleep(300)
    OP_43(0xA, 0x1, 0x0, 0x8)
    OP_44(0x101, 0x2)
    OP_44(0x9, 0x2)
    OP_44(0xC, 0x2)
    WaitChrThread(0x101, 0x0)
    Sleep(1500)

    def lambda_A5B():
        OP_6D(-2290, 0, 14010, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A5B)
    Sleep(500)
    OP_8C(0xC, 180, 500)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #9
        0xC,
        (
            "#076F#6PAll right!\x01",
            "The rest of us will clear the rubble over there!\x02\x03",

            "It looks like some people are still trapped\x01",
            "beneath it!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B06():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B06)
    Sleep(50)

    def lambda_B19():
        OP_8C(0xFE, 180, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B19)
    Sleep(300)

    ChrTalk(    #10
        0x101,
        "#1005F#2PLet's go!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x9,
        "#035F#6PHeh. Let us get lifting!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 600)
    OP_43(0x101, 0x1, 0x0, 0x3)
    Sleep(500)
    OP_43(0x9, 0x1, 0x0, 0x4)
    Sleep(300)
    OP_43(0xC, 0x1, 0x0, 0x5)
    Sleep(1000)
    Jump("loc_E93")

    label("loc_B92")

    OP_2B(0x94, 0x3)

    ChrTalk(    #12
        0x101,
        (
            "#1002F#5PWait, wait... We've gotta figure out\x01",
            "how we're gonna do this. QUICKLY,\x01",
            "but we've gotta.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(300)

    ChrTalk(    #13
        0x101,
        (
            "#1005F#2POkay! Schera, take Kloe and Tita\x01",
            "and help evacuate any civilians who\x01",
            "are still in the area!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C79():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C79)

    def lambda_C87():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C87)
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(    #14
        0x8,
        "#022F#5PUnderstood!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 500)

    ChrTalk(    #15
        0x8,
        "#024F#2PKloe, Tita, let's get to the west exit!\x02",
    )

    CloseMessageWindow()

    def lambda_CF1():
        OP_8C(0xFE, 180, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_CF1)
    Sleep(50)

    def lambda_D04():
        OP_8C(0xFE, 180, 500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_D04)
    Sleep(300)

    ChrTalk(    #16
        0xA,
        "#042F#6PYes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xB,
        "#062F#5PC-Coming!\x02",
    )

    CloseMessageWindow()

    def lambda_D40():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_D40)
    Sleep(100)
    OP_8C(0x9, 225, 400)

    def lambda_D5A():
        OP_6D(-4420, 0, 13210, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D5A)
    OP_43(0x8, 0x1, 0x0, 0x6)
    Sleep(500)
    OP_43(0xB, 0x1, 0x0, 0x7)
    Sleep(300)
    OP_43(0xA, 0x1, 0x0, 0x8)
    WaitChrThread(0x101, 0x0)
    Sleep(1500)
    OP_44(0x101, 0x2)
    OP_44(0x9, 0x2)
    OP_44(0xC, 0x2)

    def lambda_DA7():
        OP_6D(-2290, 0, 14010, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_DA7)
    Sleep(500)
    OP_8C(0x101, 0, 500)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #18
        0x101,
        (
            "#1005F#2PZin, Olivier!\x02\x03",

            "We'll help clear that rubble!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E0B():
        OP_8C(0xFE, 180, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_E0B)
    Sleep(50)

    def lambda_E1E():
        OP_8C(0xFE, 180, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_E1E)
    Sleep(400)

    ChrTalk(    #19
        0xC,
        "#076F#6PRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x9,
        "#035F#6PHeh. Let us get lifting!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 600)
    OP_43(0x101, 0x1, 0x0, 0x3)
    Sleep(500)
    OP_43(0x9, 0x1, 0x0, 0x4)
    Sleep(300)
    OP_43(0xC, 0x1, 0x0, 0x5)
    Sleep(1000)
    Jump("loc_E93")

    label("loc_E93")

    Fade(500)
    OP_6D(110, -1000, -4550, 0)
    OP_67(0, 7830, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #21
        0xD,
        (
            "#616F#5PLila! LIIILAAAA!\x01",
            "Say something! ANYTHING!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(100)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #22
        0xF,
        "#6PErgh... No good!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        "#6PCan't...move it with just us!\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x1, 0x0, 0xC)

    def lambda_F8C():
        OP_6D(910, -1000, -2920, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F8C)
    Sleep(300)
    OP_43(0x9, 0x1, 0x0, 0xD)
    Sleep(300)
    OP_43(0xC, 0x1, 0x0, 0xE)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #24
        0x101,
        "#1005F#6PMayor Maybelle!\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1033():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1033)

    def lambda_1041():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1041)

    def lambda_104F():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_104F)
    Sleep(400)

    ChrTalk(    #25
        0x10,
        "#5PYou guys...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xD,
        "#619F#5PE-Estelle! Oh, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#1005F#6PWe're here to help!\x01",
            "Is someone under there?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xD,
        (
            "#618F#5PL-Li-Lila... Lila's...\x02\x03",

            "#616FLila pushed me out of the way\x01",
            "and was, was...!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1130():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1130)
    Sleep(50)

    def lambda_1143():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1143)
    Sleep(50)
    OP_8C(0xC, 180, 400)

    ChrTalk(    #29
        0x101,
        "#1002F#6POh, no!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xC,
        (
            "#072F#6P...I think I can move this on my own.\x02\x03",

            "You there! Step back a bit!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xF,
        "#3PS-Sure...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x10,
        "#5PIt's, uh, in your hands!\x02",
    )

    CloseMessageWindow()

    def lambda_11F6():

        label("loc_11F6")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_11F6")

    QueueWorkItem2(0xF, 2, lambda_11F6)

    def lambda_1207():

        label("loc_1207")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_1207")

    QueueWorkItem2(0x10, 2, lambda_1207)

    def lambda_1218():

        label("loc_1218")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_1218")

    QueueWorkItem2(0xD, 1, lambda_1218)
    SetChrFlags(0xC, 0x4)

    def lambda_122E():
        OP_8E(0xFE, 0x60E, 0xFFFFFC18, 0xFFFFEFFC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_122E)

    def lambda_1249():
        OP_6D(870, -1000, -3760, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1249)
    Sleep(300)

    def lambda_1266():
        OP_8F(0xFE, 0xFFFFFAA6, 0xFFFFFC18, 0xFFFFF3D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1266)
    Sleep(100)

    def lambda_1286():
        OP_8F(0xFE, 0xFFFFF880, 0xFFFFFC18, 0xFFFFEF7A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1286)
    WaitChrThread(0xC, 0x1)
    OP_8C(0xC, 225, 400)
    Sleep(500)
    Fade(500)

    def lambda_12B7():
        OP_6B(2700, 0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_12B7)
    SetChrFlags(0xC, 0x2)
    SetChrChipByIndex(0xC, 9)
    SetChrSubChip(0xC, 0)
    OP_0D()

    def lambda_12D7():
        OP_99(0xFE, 0x0, 0x2, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_12D7)
    Sleep(500)

    ChrTalk(    #33
        0xC,
        "#077F#6PHiii...YAH!\x02",
    )

    CloseMessageWindow()
    Fade(500)

    def lambda_130A():
        OP_6B(2900, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_130A)
    OP_B0(0x2, 0xFA)
    OP_6F(0x2, 0)
    OP_70(0x2, 0xAA)
    Sleep(150)

    def lambda_1331():
        OP_99(0xFE, 0x4, 0x9, 0x578)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1331)
    OP_22(0x123, 0x0, 0x64)
    SetChrSubChip(0xE, 2)
    OP_44(0xD, 0x1)

    def lambda_134F():
        OP_8C(0xD, 90, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_134F)
    OP_73(0x2)
    WaitChrThread(0xC, 0x2)
    Sleep(1000)

    ChrTalk(    #34
        0xD,
        "#619F#5PLila?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xE,
        (
            "#5P#625F#80WNn...ah...\x02\x03",

            "#626F#80WMiss...May...be...aaah...\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x10, 0x2)
    OP_44(0xF, 0x2)
    OP_8C(0xF, 135, 400)
    OP_8C(0x10, 135, 400)

    ChrTalk(    #36
        0xF,
        "#6PShe's alive!\x02",
    )

    CloseMessageWindow()
    OP_44(0xD, 0x1)

    ChrTalk(    #37
        0xD,
        "#616F#5POh, Lila! LILA!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 500)
    Sleep(300)

    ChrTalk(    #38
        0x101,
        "#1005F#4POlivier! Help me carry Lila!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        "#035F#6PLeave the fair maiden to me.\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21()
    Sleep(1000)
    OP_A2(0x1A13)
    ClearMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1111   ._SN", 109, 0, 0)
    IdleLoop()
    Return()

    # Function_2_374 end

    def Function_3_1490(): pass

    label("Function_3_1490")

    OP_8E(0xFE, 0xFFFFF24A, 0xFFFFFC18, 0x1766, 0x1388, 0x0)
    Return()

    # Function_3_1490 end

    def Function_4_14A5(): pass

    label("Function_4_14A5")

    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 17)
    OP_8E(0xFE, 0xFFFFF24A, 0xFFFFFC18, 0x1766, 0x1388, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_4_14A5 end

    def Function_5_14C9(): pass

    label("Function_5_14C9")

    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 20)
    OP_8E(0xFE, 0xFFFFF24A, 0xFFFFFC18, 0x1766, 0x1194, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_5_14C9 end

    def Function_6_14ED(): pass

    label("Function_6_14ED")

    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 16)
    OP_8E(0xFE, 0xFFFFE049, 0x0, 0x2634, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFCA22, 0x0, 0x221A, 0x1388, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_6_14ED end

    def Function_7_152A(): pass

    label("Function_7_152A")

    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 19)
    OP_8E(0xFE, 0xFFFFE2AA, 0x0, 0x272E, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFCC34, 0x0, 0x21CA, 0x1388, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_7_152A end

    def Function_8_1567(): pass

    label("Function_8_1567")

    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 18)
    OP_8E(0xFE, 0xFFFFE2AA, 0x0, 0x272E, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFCC34, 0x0, 0x21CA, 0x1388, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_8_1567 end

    def Function_9_15A4(): pass

    label("Function_9_15A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_15D8")
    OP_90(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x9C4, 0x0)
    OP_90(0xFE, 0x0, 0x0, 0x3E8, 0x9C4, 0x0)
    Jump("Function_9_15A4")

    label("loc_15D8")

    Return()

    # Function_9_15A4 end

    def Function_10_15D9(): pass

    label("Function_10_15D9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1601")
    OP_8C(0xFE, 90, 200)
    OP_8C(0xFE, 0, 200)
    OP_8C(0xFE, 270, 200)
    OP_8C(0xFE, 180, 200)
    Jump("Function_10_15D9")

    label("loc_1601")

    Return()

    # Function_10_15D9 end

    def Function_11_1602(): pass

    label("Function_11_1602")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1626")
    OP_8C(0xFE, 45, 300)
    Sleep(1000)
    OP_8C(0xFE, 315, 300)
    Sleep(1000)
    Jump("Function_11_1602")

    label("loc_1626")

    Return()

    # Function_11_1602 end

    def Function_12_1627(): pass

    label("Function_12_1627")

    OP_8E(0xFE, 0x2C6, 0xFFFFFC18, 0xA14, 0x1388, 0x0)
    OP_8E(0xFE, 0x28A, 0xFFFFFC18, 0xFFFFF902, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_12_1627 end

    def Function_13_165C(): pass

    label("Function_13_165C")

    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 17)
    OP_8E(0xFE, 0x2C6, 0xFFFFFC18, 0xA14, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFFF60, 0xFFFFFC18, 0xFFFFFC68, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 1)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x1000)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_13_165C end

    def Function_14_16A5(): pass

    label("Function_14_16A5")

    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 20)
    OP_8E(0xFE, 0x2C6, 0xFFFFFC18, 0xA14, 0x1194, 0x0)
    OP_8E(0xFE, 0x7B2, 0xFFFFFC18, 0xFFFFFB8C, 0x1194, 0x0)
    SetChrChipByIndex(0xFE, 4)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x1000)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_14_16A5 end

    SaveToFile()

Try(main)
