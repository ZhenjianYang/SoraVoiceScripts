from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4312   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4312.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        'Special Ops Soldier',                  # 9
        'Special Ops Soldier',                  # 10
        'Special Ops Soldier',                  # 11
        'Special Ops Soldier',                  # 12
        'Sergeant',                             # 13
        'Rianne',                               # 14
        'Sieg',                                 # 15
        'Nial',                                 # 16
        'Princess Klaudia',                     # 17
        '1st Lieutenant Schwarz',               # 18
        'Scherazard',                           # 19
        'Olivier',                              # 20
        'Carna',                                # 21
        'Anelace',                              # 22
        'Grant',                                # 23
        'Kurt',                                 # 24
        'Royal Guardsman',                      # 25
        'Royal Guardsman',                      # 26
        'Royal Guardsman',                      # 27
        'Royal Guardsman',                      # 28
        'Royal Guardsman',                      # 29
        'Royal Guardsman',                      # 30
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
        'ED6_DT07/CH00100 ._CH',             # 00
        'ED6_DT07/CH00101 ._CH',             # 01
        'ED6_DT07/CH00110 ._CH',             # 02
        'ED6_DT07/CH00111 ._CH',             # 03
        'ED6_DT07/CH00170 ._CH',             # 04
        'ED6_DT07/CH00171 ._CH',             # 05
        'ED6_DT07/CH00340 ._CH',             # 06
        'ED6_DT07/CH00341 ._CH',             # 07
        'ED6_DT07/CH00440 ._CH',             # 08
        'ED6_DT07/CH01480 ._CH',             # 09
        'ED6_DT07/CH02320 ._CH',             # 0A
        'ED6_DT07/CH02060 ._CH',             # 0B
        'ED6_DT07/CH02340 ._CH',             # 0C
        'ED6_DT07/CH02090 ._CH',             # 0D
        'ED6_DT07/CH00020 ._CH',             # 0E
        'ED6_DT07/CH00030 ._CH',             # 0F
        'ED6_DT07/CH00122 ._CH',             # 10
        'ED6_DT07/CH00444 ._CH',             # 11
        'ED6_DT07/CH00443 ._CH',             # 12
        'ED6_DT07/CH01240 ._CH',             # 13
        'ED6_DT07/CH01630 ._CH',             # 14
        'ED6_DT07/CH01260 ._CH',             # 15
        'ED6_DT07/CH01620 ._CH',             # 16
        'ED6_DT07/CH01320 ._CH',             # 17
        'ED6_DT07/CH00040 ._CH',             # 18
    )

    AddCharChipPat(
        'ED6_DT07/CH00100P._CP',             # 00
        'ED6_DT07/CH00101P._CP',             # 01
        'ED6_DT07/CH00110P._CP',             # 02
        'ED6_DT07/CH00111P._CP',             # 03
        'ED6_DT07/CH00170P._CP',             # 04
        'ED6_DT07/CH00171P._CP',             # 05
        'ED6_DT07/CH00340P._CP',             # 06
        'ED6_DT07/CH00341P._CP',             # 07
        'ED6_DT07/CH00440P._CP',             # 08
        'ED6_DT07/CH01480P._CP',             # 09
        'ED6_DT07/CH02320P._CP',             # 0A
        'ED6_DT07/CH02060P._CP',             # 0B
        'ED6_DT07/CH02340P._CP',             # 0C
        'ED6_DT07/CH02090P._CP',             # 0D
        'ED6_DT07/CH00020P._CP',             # 0E
        'ED6_DT07/CH00030P._CP',             # 0F
        'ED6_DT07/CH00122P._CP',             # 10
        'ED6_DT07/CH00444P._CP',             # 11
        'ED6_DT07/CH00443P._CP',             # 12
        'ED6_DT07/CH01240P._CP',             # 13
        'ED6_DT07/CH01630P._CP',             # 14
        'ED6_DT07/CH01260P._CP',             # 15
        'ED6_DT07/CH01620P._CP',             # 16
        'ED6_DT07/CH01320P._CP',             # 17
        'ED6_DT07/CH00040P._CP',             # 18
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
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
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -57400,
        Y                   = 1000,
        Z                   = 2550,
        Range               = -43640,
        Unknown_10          = 0xFFFFFC18,
        Unknown_14          = 0xFFFFFCCC,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )


    ScpFunction(
        "Function_0_452",          # 00, 0
        "Function_1_4AB",          # 01, 1
        "Function_2_4CB",          # 02, 2
        "Function_3_998",          # 03, 3
        "Function_4_DF9",          # 04, 4
        "Function_5_1021",         # 05, 5
        "Function_6_39D1",         # 06, 6
        "Function_7_427C",         # 07, 7
    )


    def Function_0_452(): pass

    label("Function_0_452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_460")
    OP_A3(0x3FA)
    Event(0, 2)

    label("loc_460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_477")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FB)
    Event(0, 6)

    label("loc_477")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_483"),
        (SWITCH_DEFAULT, "loc_499"),
    )


    label("loc_483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_496")
    OP_A2(0x659)
    Event(0, 5)

    label("loc_496")

    Jump("loc_499")

    label("loc_499")

    OP_51(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_452 end

    def Function_1_4AB(): pass

    label("Function_1_4AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BD")
    OP_1C(0x1, 0x0, 0x4)
    OP_72(0x1, 0x10)

    label("loc_4BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CA")
    OP_1B(0x0, 0x0, 0x7)

    label("loc_4CA")

    Return()

    # Function_1_4AB end

    def Function_2_4CB(): pass

    label("Function_2_4CB")

    EventBegin(0x0)
    OP_6D(640, 0, -4630, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x108, 190, 0, -7530, 0)
    SetChrPos(0x101, -1330, 0, -8480, 0)
    SetChrPos(0x102, 570, 0, -8760, 0)

    ChrTalk(    #0
        0x101,
        (
            "#000FSo, this is the Erbe Royal Villa...\x02\x03",

            "It's gorgeous... Certainly gives\x01",
            "the castle a run for its mira...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        "#010FWell, it IS a royal family residence.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x8, 11320, 0, -6220, 257)
    SetChrPos(0x9, 12050, 0, -5100, 264)
    SetChrPos(0xA, 12230, 0, -6940, 276)
    SetChrPos(0xB, 13520, 0, -5780, 285)
    TurnDirection(0x108, 0x8, 400)

    ChrTalk(    #2
        0x108,
        (
            "#070FOops... Looks like the welcoming\x01",
            "committee's here.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_68F():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_68F)

    def lambda_69D():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_69D)

    def lambda_6AB():
        OP_6D(5840, 0, -6950, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6AB)

    def lambda_6C3():
        OP_67(0, 4710, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6C3)

    def lambda_6DB():
        OP_6C(68000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6DB)

    ChrTalk(    #3
        0x8,
        "Who are you people?!\x02",
    )

    CloseMessageWindow()
    OP_8E(0x101, 0xFFFFFD44, 0x0, 0xFFFFE4F8, 0x1388, 0x0)
    OP_8E(0x101, 0x316, 0x0, 0xFFFFE82C, 0x1388, 0x0)
    TurnDirection(0x101, 0x9, 0)

    ChrTalk(    #4
        0x101,
        (
            "#000FYou don't need to know\x01",
            "our names!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        (
            "#010FWords will serve no purpose\x01",
            "here. Let's go!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_796():
        OP_94(0x0, 0xFE, 0x0, 0x2710, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_796)

    def lambda_7AC():
        OP_94(0x0, 0xFE, 0x0, 0x2710, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7AC)

    def lambda_7C2():
        OP_94(0x0, 0xFE, 0x0, 0x2710, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_7C2)
    OP_6D(10400, 0, -6130, 700)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    Battle(0x3AD, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_808"),
        (SWITCH_DEFAULT, "loc_80B"),
    )


    label("loc_808")

    OP_B4(0x0)
    Return()

    label("loc_80B")

    EventBegin(0x0)
    OP_6D(9140, 0, -6380, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(44000, 0)
    OP_6E(280, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    SetChrPos(0x101, 9260, 0, -5570, 81)
    SetChrPos(0x108, 10200, 0, -6390, 96)
    SetChrPos(0x102, 8460, 0, -7540, 100)
    Sleep(500)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #6
        0x101,
        (
            "#000FNow, where's the princess\x01",
            "being held?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #7
        0x102,
        (
            "#010FThis place is huge.\x02\x03",

            "We'll just have to search it\x01",
            "room-by-room.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x108, 270, 400)

    ChrTalk(    #8
        0x108,
        (
            "#070FIf we just hang around here,\x01",
            "you can bet we're going to\x01",
            "have more company, and soon.\x02\x03",

            "Let's get a move on.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_2_4CB end

    def Function_3_998(): pass

    label("Function_3_998")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 4)), scpexpr(EXPR_END)), "loc_9A0")
    Return()

    label("loc_9A0")

    OP_A2(0x654)
    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, -52180, 0, 20500, 180)
    SetChrPos(0x9, -50170, 0, 20530, 180)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_9EE():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_9EE)

    def lambda_9FC():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9FC)

    def lambda_A0A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A0A)
    OP_6D(-50570, 0, 17760, 2000)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x108, -50910, 0, 8080, 0)
    SetChrPos(0x102, -50140, 0, 6930, 0)
    SetChrPos(0x101, -52160, 0, 7020, 0)

    def lambda_A6B():
        OP_8E(0xFE, 0xFFFF38C8, 0x0, 0x35D4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_A6B)

    def lambda_A86():
        OP_8E(0xFE, 0xFFFF34FE, 0x0, 0x30DE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A86)

    def lambda_AA1():
        OP_8E(0xFE, 0xFFFF3BDE, 0x0, 0x3278, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AA1)

    ChrTalk(    #9
        0x8,
        "Wha... Who are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x9,
        "Why do you look so familiar?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "H-Hey! You guys won the Martial\x01",
            "Arts Competition!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x9,
        (
            "That means you're with the\x01",
            "Bracer Guild!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x108,
        (
            "#070FDing ding ding! That is correct.\x01",
            "And as a prize, you get a fist\x01",
            "to the face!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BB3():
        OP_8E(0xFE, 0xFFFF3878, 0x0, 0x9A92, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_BB3)

    def lambda_BCE():
        OP_8E(0xFE, 0xFFFF3878, 0x0, 0x9A92, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BCE)

    def lambda_BE9():
        OP_8E(0xFE, 0xFFFF3878, 0x0, 0x9A92, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BE9)
    OP_6D(-51250, 0, 20190, 500)
    OP_44(0x101, 0xFF)
    OP_44(0x108, 0xFF)
    OP_44(0x102, 0xFF)
    Battle(0x3AE, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_C34"),
        (SWITCH_DEFAULT, "loc_C37"),
    )


    label("loc_C34")

    OP_B4(0x0)
    Return()

    label("loc_C37")

    EventBegin(0x0)
    OP_6D(-48790, 0, 18830, 0)
    SetChrPos(0x8, -53840, 0, 18820, 298)
    SetChrPos(0x9, -53890, 0, 17410, 315)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    SetChrPos(0x101, -50330, 0, 18280, 295)
    SetChrPos(0x108, -50350, 0, 16900, 285)
    SetChrPos(0x102, -49040, 0, 18430, 283)

    ChrTalk(    #14
        0x101,
        (
            "#000FWhew... One group down.\x02\x03",

            "I guess they must have been\x01",
            "guarding this fancy door...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D0F():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_D0F)
    OP_8C(0x102, 315, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D8D")

    ChrTalk(    #15
        0x102,
        (
            "#010FYeah...which means there must be\x01",
            "something worth guarding behind it.\x02\x03",

            "Let's check it out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF6")

    label("loc_D8D")


    ChrTalk(    #16
        0x102,
        (
            "#010FThis might be the door to the\x01",
            "banquet hall that the butler\x01",
            "told us about.\x02\x03",

            "Let's check it out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF6")

    EventEnd(0x0)
    Return()

    # Function_3_998 end

    def Function_4_DF9(): pass

    label("Function_4_DF9")

    SetMapFlags(0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F92")
    OP_A2(0x655)
    EventBegin(0x0)
    OP_8B(0x0, 0xFFFF38FA, 0x5604, 0x190)
    OP_8B(0x1, 0xFFFF38FA, 0x5604, 0x190)
    OP_8B(0x2, 0xFFFF38FA, 0x5604, 0x190)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #17
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #18
        0x101,
        "#000FAwww, no!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x102,
        (
            "#010FIt seems pretty solid, and the locking\x01",
            "mechanism is quite secure. We definitely\x01",
            "won't be able to get in without the key.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F44")

    ChrTalk(    #20
        0x108,
        (
            "#070FHm... I guess we'll have to\x01",
            "leave this place for later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F8D")

    label("loc_F44")


    ChrTalk(    #21
        0x108,
        (
            "#070FHm... Maybe we should go talk\x01",
            "to that young chamberlain.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x4C, 0x1, 0x8)

    label("loc_F8D")

    EventEnd(0x1)
    Jump("loc_101B")

    label("loc_F92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 7)), scpexpr(EXPR_END)), "loc_FE0")
    OP_8B(0x0, 0xFFFF38FA, 0x5604, 0x190)
    OP_A2(0x658)
    OP_71(0x1, 0x10)
    OP_1C(0x1, 0x0, 0xFFFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #22
        "\x07\x05Used Spare Key.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jump("loc_101B")

    label("loc_FE0")

    OP_8B(0x0, 0xFFFF38FA, 0x5604, 0x190)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #23
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_101B")

    ClearMapFlags(0x80)
    Return()

    # Function_4_DF9 end

    def Function_5_1021(): pass

    label("Function_5_1021")

    EventBegin(0x0)
    OP_6D(-20, 0, 54380, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(57000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x10, 50, 250, 68860, 180)
    SetChrPos(0xD, 5680, 0, 58650, 180)
    SetChrPos(0xF, 3070, 0, 58560, 249)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x108, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, -110, 0, 50960, 0)
    SetChrPos(0x102, -110, 0, 50960, 0)
    SetChrPos(0x108, -110, 0, 50960, 0)
    SetChrPos(0xE, -110, 0, 50960, 0)
    SetChrPos(0x13, -110, 0, 50960, 0)
    SetChrPos(0x11, -110, 0, 50960, 0)
    SetChrPos(0x12, -110, 0, 50960, 0)

    def lambda_114F():
        OP_6D(750, 0, 56890, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_114F)

    def lambda_1167():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1167)

    def lambda_1179():
        OP_8E(0xFE, 0xFFFFFFC4, 0x0, 0xDFFC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1179)
    Sleep(500)

    def lambda_1199():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1199)

    def lambda_11AB():
        OP_8E(0xFE, 0x302, 0x0, 0xDBEC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11AB)
    Sleep(500)

    def lambda_11CB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_11CB)

    def lambda_11DD():
        OP_8E(0xFE, 0xFFFFFC4A, 0x0, 0xDA34, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_11DD)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #24
        0xF,
        "#140FY-You...?!\x02",
    )

    CloseMessageWindow()

    def lambda_1212():
        OP_6D(2460, 0, 58180, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1212)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)

    def lambda_1239():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1239)

    def lambda_1247():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1247)
    TurnDirection(0x101, 0xF, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #25
        0x101,
        (
            "#000FYo!\x01",
            "We're here to save your bacon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        (
            "#010FHello, Nial. You don't look in\x01",
            "too bad a shape.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xF,
        "#140FAre you serious?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10,
        "Estelle... Joshua...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "I never thought I'd see\x01",
            "you here...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1327():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1327)

    def lambda_1335():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1335)
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(    #30
        0x101,
        "#000F...Huh?\x02",
    )

    CloseMessageWindow()

    def lambda_135C():
        OP_6D(70, 250, 68760, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_135C)

    def lambda_1374():
        OP_67(0, 4420, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1374)

    def lambda_138C():
        OP_6C(11000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_138C)
    Sleep(1500)

    def lambda_13A1():
        OP_8E(0xFE, 0xFFFFFDE4, 0x0, 0x1041E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13A1)
    Sleep(100)

    def lambda_13C1():
        OP_8E(0xFE, 0x1EA, 0x0, 0x1041E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13C1)
    Sleep(300)

    def lambda_13E1():
        OP_8E(0xFE, 0xFFFFF6E6, 0x0, 0x10266, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_13E1)
    Sleep(100)

    def lambda_1401():
        OP_8E(0xFE, 0x8AC, 0x0, 0x10568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_1401)

    def lambda_141C():

        label("loc_141C")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_141C")

    QueueWorkItem2(0x108, 1, lambda_141C)

    def lambda_142D():

        label("loc_142D")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_142D")

    QueueWorkItem2(0xF, 1, lambda_142D)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #31
        0x101,
        (
            "#000FY-You're the princess.\x02\x03",

            "It's a pleasure to meet you.\x01",
            "We're with the...Bracer...Guild...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x10,
        (
            "I think it's a little late\x01",
            "for introductions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10,
        (
            "So, we meet again,\x01",
            "as promised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#000FErr...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(    #35
        0x101,
        "#000FKLOE!!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10,
        (
            "#040FEstelle...\x02\x03",

            "I sincerely hope you're joking.\x01",
            "You ought to have recognized\x01",
            "me sooner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#000FBut not with the dress, and\x01",
            "the hair, and the things...!\x02\x03",

            "What happened?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x102,
        (
            "#010FPardon us, Kloe.\x02\x03",

            "Estelle doesn't know how\x01",
            "to doubt people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#000FHey! What the hell's that\x01",
            "supposed to mean?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x10,
        (
            "#040FHa ha...\x01",
            "There's the Estelle I know.\x02\x03",

            "And, Joshua...?\x02\x03",

            "You'll still use that name\x01",
            "for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x102,
        (
            "#010FYes, since it seems to be\x01",
            "the one you'd prefer.\x02\x03",

            "Would you rather I use your\x01",
            "real name?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x10,
        (
            "#040FNo... But thank you.\x01",
            "I'm glad to hear it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#000F???\x02\x03",

            "Okay, so what are you\x01",
            "doing here, Kloe?\x02\x03",

            "And for that matter, why isn't\x01",
            "the princess here...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xF,
        (
            "#140FUhh...\x01",
            "She's right in front of you.\x02\x03",

            "That's the queen's granddaughter,\x01",
            "Princess Klaudia.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1835():
        OP_67(0, 6000, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1835)
    OP_6C(45000, 1500)

    ChrTalk(    #45
        0x101,
        (
            "#000F...Buh?\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46 op#A op#5
        0x101,
        "#000F#10AAAAAAAAAAAAH!!\x05\x02",
    )

    OP_6E(253, 1000)
    OP_44(0x108, 0xFF)
    OP_44(0xF, 0xFF)

    ChrTalk(    #47
        0x10,
        (
            "I'm sorry that I couldn't\x01",
            "tell you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x10,
        (
            "I had planned to tell both of\x01",
            "you the truth when we next met\x01",
            "in Grancel...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x10,
        (
            "But then the Intelligence\x01",
            "Division had me 'detained'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        (
            "#000FUhh...but why?\x02\x03",

            "Why would the princess be hiding\x01",
            "out in an ordinary school...?!\x02\x03",

            "And why did you have us\x01",
            "call you 'Kloe'...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x10,
        (
            "I'd like for you to keep\x01",
            "calling me that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x10,
        "My real name is Klaudia von Auslese...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x10,
        (
            "Kloe is a pet name that Jill\x01",
            "came up with using bits from\x01",
            "my whole name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        (
            "#000FReally...\x02\x03",

            "Uh, then what about your hair?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10,
        "Oh, this is just a wig.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x10,
        (
            "If I had the same hairdo as when\x01",
            "I was on campus, it would probably\x01",
            "just create trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xF,
        (
            "#140FCan't believe I missed the\x01",
            "connection myself.\x02\x03",

            "I've seen your picture often enough, and\x01",
            "I remember you from the mayoral scandal in\x01",
            "Ruan, but I never put two and two together...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x10,
        "Ha ha... I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x10,
        (
            "It doesn't seem that Uncle Dunan\x01",
            "or Mayor Dalmore recognized me,\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        (
            "#000FOh, yeah...and the duke's even\x01",
            "related to you.\x02\x03",

            "Oh! I forgot something important.\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x101, 0x10, 0x2BC, 0xBB8, 0x0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #61
        (
            "\x07\x05Estelle explained the whole story, including how they had come to rescue\x01",
            "Kloe at the queen's behest.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_8F(0x101, 0xFFFFFDE4, 0x0, 0x1041E, 0x7D0, 0x0)

    ChrTalk(    #62
        0x10,
        "I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x10,
        "To all three of you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x10,
        (
            "I extend my deepest gratitude\x01",
            "for coming to rescue me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        (
            "#000FAw, it was nothing.\x02\x03",

            "Heck, if we'd known that it was \x01",
            "our Kloe in here, no one would've\x01",
            "had to ask us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x10,
        "E-Estelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x102,
        (
            "#010FHa ha... No doubt.\x02\x03",

            "You should save your thanks for\x01",
            "Her Majesty, as she's the one\x01",
            "who deserves them.\x02\x03",

            "She had no concern for herself...\x01",
            "just that we should save you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x108,
        (
            "#070FI think your safety will give\x01",
            "her the strength to resist the\x01",
            "colonel's demands.\x02\x03",

            "Though doing so may endanger\x01",
            "her life...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x10,
        (
            "Yes...\x01",
            "That is her way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x10,
        (
            "If something is not done, then\x01",
            "she is in grave danger...\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xD, -230, 0, 55310, 346)
    SetChrChipByIndex(0x8, 8)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0xC, 1020, 0, 56140, 0)
    SetChrPos(0x8, 50, 0, 54770, 0)

    ChrTalk(    #71
        0xC,
        "I think I've seen enough of this little farce.\x02",
    )

    CloseMessageWindow()

    def lambda_203D():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_203D)

    def lambda_204B():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_204B)

    def lambda_2059():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2059)

    def lambda_2067():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2067)

    def lambda_2075():
        OP_6D(800, 0, 61890, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2075)

    def lambda_208D():
        OP_6E(297, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_208D)
    Sleep(2000)

    ChrTalk(    #72
        0xD,
        "P-Princess...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x10,
        "Rianne!\x02",
    )

    CloseMessageWindow()

    def lambda_20C2():
        OP_6D(850, 0, 60760, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_20C2)

    def lambda_20DA():
        OP_6E(261, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_20DA)
    SetChrChipByIndex(0x101, 0)

    def lambda_20EF():
        OP_8E(0xFE, 0xFFFFFD26, 0x0, 0xF9D8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20EF)
    Sleep(200)
    SetChrChipByIndex(0x102, 2)

    def lambda_2114():
        OP_8E(0xFE, 0x190, 0x0, 0xF96A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2114)
    Sleep(100)
    SetChrChipByIndex(0x108, 4)

    def lambda_2139():
        OP_8E(0xFE, 0xFFFFF68C, 0x0, 0xF604, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2139)
    Sleep(200)

    def lambda_2159():
        OP_8E(0xFE, 0xA, 0x0, 0xFFEF, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2159)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #74
        0x101,
        "#000FWhat the--?!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x10, 0x1)

    ChrTalk(    #75
        0x10,
        "She's General Morgan's granddaughter...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x10,
        (
            "He's imprisoned at the Haken Gate.\x01",
            "I'd say they're taking her to keep\x01",
            "him from causing any trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x102,
        (
            "#010FJust as they did with you\x01",
            "and Her Majesty...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xC,
        "This isn't just some idle threat!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xC,
        (
            "Every man in the Special Ops\x01",
            "has a dream, and we will stop\x01",
            "at NOTHING to achieve it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        (
            "#000FAnd that's something you're\x01",
            "PROUD of?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x10,
        "I'll make you a deal, Sergeant.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x10,
        (
            "Please, take me as your hostage,\x01",
            "rather than the child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xC,
        "Ha... Not a chance.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xC,
        (
            "I know I said we'll stop at nothing, but even\x01",
            "we don't have the nerve to harm a member of the\x01",
            "royal family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xC,
        (
            "General Morgan's grandkid, on the other hand,\x01",
            "suits our needs just fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xC,
        (
            "She's a valuable hostage, and it's not going to\x01",
            "cause any real problems if she was to end up\x01",
            "getting hurt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x10,
        "You're a monster...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        "#000FI'd have said 'coward,' myself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x108,
        (
            "#070FPathetic, disgusting, sick...\x01",
            "Pick an adjective.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xC,
        "Heh. You can talk all you want.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xC,
        (
            "It's almost time for the patrols to\x01",
            "return from the Royal Avenue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xC,
        (
            "Then we can round up the Guardsmen\x01",
            "and the bracers. Not bad for one\x01",
            "night's work!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x12,
        (
            "Oh, I'm afraid that won't\x01",
            "be happening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x12,
        (
            "We already took your buddies\x01",
            "out on our way over here.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_2684():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2684)

    def lambda_2692():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2692)

    def lambda_26A0():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_26A0)

    def lambda_26AE():
        OP_6D(500, 0, 59390, 800)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_26AE)
    OP_6E(280, 800)

    def lambda_26CF():

        label("loc_26CF")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_26CF")

    QueueWorkItem2(0xC, 1, lambda_26CF)

    def lambda_26E0():

        label("loc_26E0")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_26E0")

    QueueWorkItem2(0x8, 1, lambda_26E0)

    def lambda_26F1():

        label("loc_26F1")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_26F1")

    QueueWorkItem2(0xD, 1, lambda_26F1)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0x12, 0x20)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x12, 16)
    ClearChrFlags(0x12, 0x80)

    def lambda_2726():

        label("loc_2726")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2726")

    QueueWorkItem2(0x12, 1, lambda_2726)
    OP_96(0x12, 0xFFFFF7A4, 0x0, 0xD5C0, 0x3E8, 0x1F40)
    OP_99(0x12, 0x2, 0x4, 0xBB8)
    PlayEffect(0x8, 0xFF, 0xFF, 50, 1000, 54770, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    TurnDirection(0x8, 0x12, 0)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 18)

    def lambda_27A3():
        OP_94(0x1, 0xFE, 0xB4, 0xBB8, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_27A3)
    OP_99(0x12, 0x4, 0x9, 0xBB8)
    OP_44(0xD, 0xFF)
    OP_44(0x8, 0xFF)

    ChrTalk(    #95 op#A op#5
        0x8,
        "#10AAgh!\x05\x02",
    )

    WaitChrThread(0x8, 0x1)
    SetChrChipByIndex(0x8, 17)

    def lambda_27E2():
        OP_99(0xFE, 0x0, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_27E2)
    Sleep(500)

    def lambda_27F7():
        OP_8E(0xFE, 0xFFFFF4DE, 0x0, 0xD912, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_27F7)
    Sleep(100)
    OP_8F(0xC, 0x6CC, 0x0, 0xDACA, 0x1388, 0x0)
    WaitChrThread(0xD, 0x1)
    OP_96(0x12, 0xFFFFF858, 0x0, 0xDA16, 0x1F4, 0x1F40)
    TurnDirection(0xD, 0x12, 400)
    Sleep(200)

    ChrTalk(    #96
        0xC,
        "Wha...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xD,
        "*sniffle*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xD,
        "WAAAAAAHHHH!!!\x02",
    )

    CloseMessageWindow()

    def lambda_2887():

        label("loc_2887")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_2887")

    QueueWorkItem2(0x101, 1, lambda_2887)

    def lambda_2898():

        label("loc_2898")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_2898")

    QueueWorkItem2(0x102, 1, lambda_2898)

    def lambda_28A9():

        label("loc_28A9")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_28A9")

    QueueWorkItem2(0x108, 1, lambda_28A9)

    def lambda_28BA():

        label("loc_28BA")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_28BA")

    QueueWorkItem2(0xF, 1, lambda_28BA)

    def lambda_28CB():

        label("loc_28CB")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_28CB")

    QueueWorkItem2(0x10, 1, lambda_28CB)

    ChrTalk(    #99
        0x12,
        (
            "#020FThere, there...\x01",
            "It's all right...\x02\x03",

            "Hi, you two.\x01",
            "Long time no see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        "#000FSch-Schera?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x102,
        "#010FYou came...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xC,
        (
            "Damn it all... Who the hell\x01",
            "do you think you are?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x13,
        (
            "*sigh*... Some people just\x01",
            "have no manners.\x02",
        )
    )

    CloseMessageWindow()
    PlayEffect(0x8, 0xFF, 0xFF, 1590, 1000, 54930, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xC, 18)

    def lambda_2A03():
        OP_96(0xFE, 0xBD6, 0x0, 0xDFFC, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2A03)

    ChrTalk(    #104 op#A op#5
        0xC,
        "#10AGah...\x05\x02",
    )

    Sleep(400)

    def lambda_2A36():

        label("loc_2A36")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_2A36")

    QueueWorkItem2(0x12, 1, lambda_2A36)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2A52():
        OP_96(0xFE, 0x442, 0x0, 0xDDCC, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2A52)
    Sleep(200)
    OP_99(0x12, 0x2, 0x4, 0xFA0)
    PlayEffect(0x8, 0xFF, 0xFF, 3180, 1500, 56940, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xC, 0x4)

    def lambda_2AB8():
        OP_6D(6320, 0, 57730, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2AB8)

    def lambda_2AD0():
        OP_8F(0xFE, 0x2508, 0x1F4, 0xDCE6, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2AD0)
    OP_99(0x12, 0x4, 0x9, 0x7D0)
    WaitChrThread(0xC, 0x1)
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xC, 17)

    ChrTalk(    #105 op#A op#5
        0xC,
        "#10AOOF!\x05\x02",
    )

    PlayEffect(0x12, 0xFF, 0xC, 0, 0, -500, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_6B(3070, 0)
    OP_6B(3000, 80)
    Sleep(500)
    OP_8F(0xC, 0x2512, 0x0, 0xDCE6, 0x3E8, 0x0)
    OP_99(0xC, 0x0, 0x3, 0x7D0)

    ChrTalk(    #106
        0x12,
        "#020FThink of that as my special gift.\x02",
    )

    CloseMessageWindow()
    OP_6D(280, 0, 58100, 2000)

    ChrTalk(    #107
        0x101,
        (
            "#000FThat's just cruel...\x02\x03",

            "Hey, who fired that shot...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x102,
        "#010F...Olivier, I'd guess.\x02",
    )

    CloseMessageWindow()
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x12, 14)
    TurnDirection(0x12, 0x13, 400)

    ChrTalk(    #109
        0x13,
        "Bingo! ♪\x02",
    )

    CloseMessageWindow()

    def lambda_2C41():

        label("loc_2C41")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_2C41")

    QueueWorkItem2(0x12, 1, lambda_2C41)

    def lambda_2C52():

        label("loc_2C52")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_2C52")

    QueueWorkItem2(0xD, 1, lambda_2C52)

    def lambda_2C63():

        label("loc_2C63")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_2C63")

    QueueWorkItem2(0x101, 1, lambda_2C63)

    def lambda_2C74():

        label("loc_2C74")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_2C74")

    QueueWorkItem2(0x102, 1, lambda_2C74)

    def lambda_2C85():

        label("loc_2C85")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_2C85")

    QueueWorkItem2(0x108, 1, lambda_2C85)

    def lambda_2C96():

        label("loc_2C96")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_2C96")

    QueueWorkItem2(0xF, 1, lambda_2C96)

    def lambda_2CA7():

        label("loc_2CA7")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_2CA7")

    QueueWorkItem2(0x10, 1, lambda_2CA7)
    ClearChrFlags(0x13, 0x80)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2CC8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_2CC8)

    def lambda_2CDA():
        OP_8E(0xFE, 0x1E, 0x0, 0xD7F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2CDA)
    Sleep(100)
    OP_6D(550, 0, 58110, 2000)

    ChrTalk(    #110
        0x13,
        (
            "#030FAnd the star makes his dramatic entrance!\x01",
            "Please, hold your applause until after\x01",
            "the performance has ended...\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)

    def lambda_2D88():
        OP_8E(0xFE, 0xFFFFFB78, 0x0, 0xE128, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2D88)
    Sleep(100)
    SetChrChipByIndex(0x102, 65535)

    def lambda_2DAD():
        OP_8E(0xFE, 0xF0, 0x0, 0xE2C2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2DAD)
    Sleep(300)

    def lambda_2DCD():
        OP_8E(0xFE, 0x78, 0x0, 0xE90C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2DCD)
    Sleep(500)
    SetChrChipByIndex(0x108, 65535)

    def lambda_2DF2():
        OP_8E(0xFE, 0xFFFFF8D0, 0x0, 0xE452, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_2DF2)
    Sleep(100)

    def lambda_2E12():
        OP_8E(0xFE, 0x9A6, 0x0, 0xE902, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_2E12)
    Sleep(100)
    Sleep(2000)
    OP_44(0x12, 0xFF)

    ChrTalk(    #111
        0x108,
        (
            "#070FHa ha... And the drama turns\x01",
            "into a comedy!\x02\x03",

            "Nice seeing you again, Scherazard.\x01",
            "It's been a long time.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x108, 400)

    ChrTalk(    #112
        0x12,
        (
            "#020FIndeed, it has.\x02\x03",

            "I never thought I'd find you in Liberl.\x02\x03",

            "But I was honestly quite relieved\x01",
            "when I heard that you'd fallen in\x01",
            "with Estelle and Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x108,
        (
            "#070FHa ha. Well, I think you're over-\x01",
            "estimating my capabilities...\x01",
            "like usual.\x02\x03",

            "As for you...you've only become\x01",
            "more beautiful.\x02\x03",

            "I barely even recognized you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x12,
        "#020FO-Oh...really?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x12, 400)
    Sleep(500)
    TurnDirection(0x13, 0x108, 400)
    Sleep(500)
    TurnDirection(0x13, 0x12, 400)

    ChrTalk(    #115
        0x13,
        (
            "#030FHmmm... I am suddenly brimming over\x01",
            "with something akin to jealousy.\x02\x03",

            "Am I merely a toy, to be used\x01",
            "when convenient, and cast aside\x01",
            "when boredom sets in?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x13, 400)

    ChrTalk(    #116
        0x12,
        (
            "#020FHey, Olivier. Aina's been wanting\x01",
            "to see you.\x02\x03",

            "She's hoping to go out for\x01",
            "drinks again.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x102, 400)

    ChrTalk(    #117
        0x13,
        (
            "#030FForgive me. I have committed\x01",
            "a grave offense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#000FI swear...\x01",
            "None of you ever change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x102,
        (
            "#010FI'm glad to see you, Schera.\x02\x03",

            "But I thought that the Royal\x01",
            "Army had the checkpoints\x01",
            "completely sealed off...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x102, 400)

    ChrTalk(    #120
        0x12,
        (
            "#020FYes...but we crossed Valleria\x01",
            "Lake by boat.\x02\x03",

            "And docked at Grancel Harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x102,
        "#010FThat's one way around a problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        (
            "#000FBut how did you wind up falling\x01",
            "in with the failed...excuse me,\x01",
            "'Traveling'...musician?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x12,
        (
            "#020FWe ran into each other at the\x01",
            "local guild branch.\x02\x03",

            "He was like a lost puppy, so I\x01",
            "didn't have much choice other\x01",
            "than to bring him along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x13,
        (
            "#030FHa ha ha...\x02\x03",

            "I simply couldn't allow such an\x01",
            "amusing and interesting show\x01",
            "to go on without me...\x02\x03",

            "And may I ask who this\x01",
            "fair lady is?\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    OP_44(0x101, 0xFF)
    OP_8E(0x102, 0x3AC, 0x0, 0xE36C, 0x7D0, 0x0)
    TurnDirection(0x102, 0x10, 400)
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(    #125
        0x101,
        (
            "#000FOh, right. Introductions.\x02\x03",

            "This is the queen's granddaughter,\x01",
            "Her Highness Princess Klaudia.\x02\x03",

            "She's a friend of ours.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_34DA():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_34DA)

    def lambda_34E8():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_34E8)
    OP_44(0x10, 0xFF)

    ChrTalk(    #126
        0x10,
        (
            "It is a pleasure to meet\x01",
            "you both.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x10,
        (
            "Thank you very much for\x01",
            "coming to help me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x12,
        (
            "#020FThink nothing of it. I'm simply\x01",
            "doing my duty as a bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x13,
        (
            "#030FAnd I could scarcely consider myself\x01",
            "a gentleman if I did not leap to the\x01",
            "aid of a lovely lady of noble birth.\x02\x03",

            "The honor and pleasure at this\x01",
            "meeting is entirely my own.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x11, -110, 0, 50960, 0)
    SetChrPos(0xE, -110, 0, 50960, 0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    ChrTalk(    #130
        0x11,
        "Your Highness! Are you well?\x02",
    )

    CloseMessageWindow()

    def lambda_36A6():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36A6)

    def lambda_36B4():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_36B4)

    def lambda_36C2():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_36C2)

    def lambda_36D0():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_36D0)

    def lambda_36DE():
        OP_8F(0xFE, 0x4A6, 0x0, 0xD9EE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_36DE)

    def lambda_36F9():
        OP_8F(0xFE, 0xFFFFF948, 0x0, 0xDEF8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_36F9)
    Sleep(500)

    def lambda_3719():

        label("loc_3719")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_3719")

    QueueWorkItem2(0x101, 1, lambda_3719)

    def lambda_372A():

        label("loc_372A")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_372A")

    QueueWorkItem2(0x102, 1, lambda_372A)

    def lambda_373B():

        label("loc_373B")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_373B")

    QueueWorkItem2(0x108, 1, lambda_373B)

    def lambda_374C():

        label("loc_374C")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_374C")

    QueueWorkItem2(0x13, 1, lambda_374C)
    ClearChrFlags(0x11, 0x80)

    def lambda_3762():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3762)

    def lambda_3774():
        OP_8E(0xFE, 0xFFFFFEA2, 0x0, 0xDF7A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3774)
    Sleep(1000)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x40)
    SetChrFlags(0xE, 0x4)

    def lambda_37A3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_37A3)

    def lambda_37B5():
        OP_8E(0xFE, 0xFFFFFCAE, 0x3E8, 0xDF66, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_37B5)
    Sleep(1000)

    ChrTalk(    #131
        0x10,
        "Julia...! Sieg!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xE,
        "Scree!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xE,
        "Screescree!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xE,
        "Screeeeeeee!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x10,
        (
            "Ha ha, good. I'm happy to\x01",
            "see you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x11,
        (
            "#170FThank goodness you're unharmed...\x02\x03",

            "I was so worried...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x10,
        "The feeling is mutual.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    AnonymousTalk(    #138
        (
            "\x07\x05Before long, the bracers involved in the diversion and the Royal Guardsmen\x01",
            "joined forces.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #139
        (
            "\x07\x05After seeing to it that the rescued hostages could get some rest, Estelle\x01",
            "and company gathered to assess their current situation.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_28(0x4B, 0x4, 0x10)
    OP_28(0x4C, 0x1, 0x40)
    OP_28(0x4C, 0x1, 0x80)
    OP_28(0x4C, 0x1, 0x100)
    OP_28(0x4D, 0x4, 0x2)
    OP_28(0x4D, 0x4, 0x4)
    OP_28(0x4D, 0x1, 0x1)
    OP_28(0x4D, 0x1, 0x2)
    OP_1B(0x0, 0x0, 0xFFFF)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4300   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_1021 end

    def Function_6_39D1(): pass

    label("Function_6_39D1")

    EventBegin(0x0)
    OP_6D(920, 250, 64110, 0)
    OP_67(0, 5940, -10000, 0)
    OP_6B(1560, 0)
    OP_6C(45000, 0)
    OP_6E(588, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x11, -140, 250, 68110, 180)
    SetChrPos(0x102, -2000, 0, 66540, 90)
    SetChrPos(0x13, -3440, 0, 65990, 90)
    SetChrPos(0x108, -3210, 0, 67070, 90)
    SetChrPos(0x101, 2020, 0, 66210, 270)
    SetChrPos(0x10, 2630, 0, 67290, 270)
    SetChrPos(0x12, 2980, 0, 66110, 270)
    SetChrPos(0x17, -50, 0, 65269, 0)
    SetChrPos(0x16, 930, 0, 64510, 0)
    SetChrPos(0x14, -1040, 0, 64410, 0)
    SetChrPos(0x15, -50, 0, 63940, 0)
    SetChrPos(0x18, -940, 0, 61330, 0)
    SetChrPos(0x19, 50, 0, 61320, 0)
    SetChrPos(0x1A, 1030, 0, 61320, 0)
    SetChrPos(0x1B, -940, 0, 60000, 0)
    SetChrPos(0x1C, 50, 0, 60000, 0)
    SetChrPos(0x1D, 1030, 0, 60000, 0)
    SetChrChipByIndex(0x10, 24)
    OP_6D(920, 250, 67890, 2000)

    ChrTalk(    #140
        0x11,
        (
            "#170F#6POkay, here's how we're going to\x01",
            "free Grancel Castle and the queen.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x102, 400)
    Sleep(400)

    ChrTalk(    #141
        0x11,
        (
            "#170F#6PFirst, Joshua and two others will\x01",
            "infiltrate the Grancel Sewers.\x02\x03",

            "You'll proceed to the Royal Guard\x01",
            "Room and open the castle gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x102,
        "#010FGot it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x108,
        "#070FTime to light a few fireworks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x13,
        (
            "#035FHa ha... Well, it does seem\x01",
            "appropriate for the beginning\x01",
            "of the final act.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 180, 400)
    Sleep(400)

    ChrTalk(    #145
        0x11,
        (
            "#170F#6PAs soon as the gates are open, the Guardsmen\x01",
            "and four of the bracers will make their way\x01",
            "to the castle by way of the streets.\x02\x03",

            "We need to make a real spectacle\x01",
            "to draw all of the guards together\x01",
            "in one place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x17,
        "#2P#840FYou're in good hands.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x16,
        (
            "#2P#821FAll right! I've been looking\x01",
            "forward to this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x11,
        "#176F#6PAnd finally...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x10, 400)
    Sleep(400)

    ChrTalk(    #149
        0x11,
        (
            "#175F#6PYour Highness, are you certain\x01",
            "I cannot get you to reconsider?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x10,
        (
            "#049F#4PI'm sorry...but I must be there\x01",
            "to help my grandmother.\x02\x03",

            "#040FAlso, I know how to pilot\x01",
            "an airship...\x02\x03",

            "I hope to be able to put\x01",
            "that skill to good use.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x11,
        (
            "#175F#6P...\x02\x03",

            "If I'd known this would happen,\x01",
            "I never would have taught you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x101,
        (
            "#006F#4PIt's okay, Lieutenant.\x02\x03",

            "We'll look after Kloe for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x12,
        (
            "#020F#4PI swear she will be kept safe or\x01",
            "my nickname isn't the Silver Streak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x11,
        (
            "#176F#6PI understand...\x01",
            "Please, do what you can.\x02\x03",

            "#170FOnce the men inside the castle have been\x01",
            "concentrated into one area, Estelle and her\x01",
            "team will set down in the Garden Terrace.\x02\x03",

            "Then, they will break into the\x01",
            "queen's room and rescue her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x101,
        "#006F#4PRoger!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 180, 400)
    Sleep(400)

    ChrTalk(    #156
        0x11,
        (
            "#176F#6PBoth operations will begin at the\x01",
            "stroke of the noon bell. Everyone\x01",
            "is to remain on alert until then.\x02\x03",

            "#177FAll right, you have your tasks.\x01",
            "Get to them! Dismissed!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    SetMessageWindowPos(300, 200, -1, -1)
    SetChrName("Royal Guardsmen")

    AnonymousTalk(    #157
        "\x07\x00#5SYes, ma'am!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x3FD)
    NewScene("ED6_DT01/T4302   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_39D1 end

    def Function_7_427C(): pass

    label("Function_7_427C")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42E8")

    ChrTalk(    #158
        0x101,
        (
            "#002FWe still haven't completed\x01",
            "Her Majesty's request.\x02\x03",

            "We have to find the princess!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43C3")

    label("loc_42E8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4353")

    ChrTalk(    #159
        0x102,
        (
            "#012FWe can leave once we set\x01",
            "the hostages free.\x02\x03",

            "We still haven't found\x01",
            "the princess.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43C3")

    label("loc_4353")


    ChrTalk(    #160
        0x108,
        (
            "#072FWe still haven't found\x01",
            "the princess.\x02\x03",

            "Until then, we have to take out\x01",
            "every single enemy around here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43C3")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_7_427C end

    SaveToFile()

Try(main)
