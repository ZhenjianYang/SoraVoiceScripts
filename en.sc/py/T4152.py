from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4152   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4152.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Private Datten',                       # 9
        'Peter',                                # 10
        'Royal Army Soldier',                   # 11
        'Royal Army Soldier',                   # 12
        'Royal Army Soldier',                   # 13
        'Grancel - North Block',                # 14
        'Grancel - South Block',                # 15
        'Grancel - N Warehouse District',       # 16
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
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01680 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01680P._CP',             # 01
    )

    DeclNpc(
        X                   = -89010,
        Z                   = 250,
        Y                   = -1030,
        Direction           = 189,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -78290,
        Z                   = 0,
        Y                   = -2530,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -55400,
        Z                   = 0,
        Y                   = -3050,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -78990,
        Z                   = 1250,
        Y                   = 8029,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -76250,
        Z                   = -3500,
        Y                   = -30490,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -39960,
        Z                   = 0,
        Y                   = 43920,
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
        X                   = -7520,
        Z                   = 300,
        Y                   = -20000,
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
        X                   = -117000,
        Z                   = 0,
        Y                   = -4090,
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


    DeclEvent(
        X                   = -63040,
        Y                   = -3750,
        Z                   = -33480,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 11,
    )

    DeclEvent(
        X                   = -63390,
        Y                   = -3750,
        Z                   = -24940,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = -78840,
        Y                   = 1250,
        Z                   = 12430,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 13,
    )


    DeclActor(
        TriggerX            = -72220,
        TriggerZ            = -3180,
        TriggerY            = -15630,
        TriggerRange        = 800,
        ActorX              = -72220,
        ActorZ              = -2000,
        ActorY              = -15630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_23E",          # 00, 0
        "Function_1_23F",          # 01, 1
        "Function_2_277",          # 02, 2
        "Function_3_29B",          # 03, 3
        "Function_4_320",          # 04, 4
        "Function_5_3AD",          # 05, 5
        "Function_6_419",          # 06, 6
        "Function_7_473",          # 07, 7
        "Function_8_4B6",          # 08, 8
        "Function_9_550",          # 09, 9
        "Function_10_5D4",         # 0A, 10
        "Function_11_633",         # 0B, 11
        "Function_12_637",         # 0C, 12
        "Function_13_63B",         # 0D, 13
        "Function_14_63F",         # 0E, 14
        "Function_15_C0B",         # 0F, 15
        "Function_16_ECF",         # 10, 16
    )


    def Function_0_23E(): pass

    label("Function_0_23E")

    Return()

    # Function_0_23E end

    def Function_1_23F(): pass

    label("Function_1_23F")

    OP_16(0x2, 0xFA0, 0xFFFD2D58, 0xFFFE0048, 0x23005D)
    OP_71(0xF, 0x4)
    OP_71(0xC, 0x10)
    OP_72(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_276")
    OP_1B(0x3, 0x0, 0xE)
    OP_1B(0x1, 0x0, 0xF)

    label("loc_276")

    Return()

    # Function_1_23F end

    def Function_2_277(): pass

    label("Function_2_277")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29A")
    OP_8D(0xFE, -83110, 1920, -74690, -5430, 3000)
    Jump("Function_2_277")

    label("loc_29A")

    Return()

    # Function_2_277 end

    def Function_3_29B(): pass

    label("Function_3_29B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_31F")
    OP_8E(0xFE, 0xFFFF63CA, 0x0, 0xFFFFF416, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFF291E, 0x0, 0xFFFFF416, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFF259A, 0x0, 0xFFFFF416, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    Jump("Function_3_29B")

    label("loc_31F")

    Return()

    # Function_3_29B end

    def Function_4_320(): pass

    label("Function_4_320")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3AC")
    OP_8E(0xFE, 0xFFFED716, 0x4E2, 0x1F5D, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFECB72, 0x4E2, 0x1F5D, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFEC014, 0x4E2, 0x1F5D, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFECB72, 0x4E2, 0x1F5D, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    Jump("Function_4_320")

    label("loc_3AC")

    Return()

    # Function_4_320 end

    def Function_5_3AD(): pass

    label("Function_5_3AD")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        "Going to the harbor when it's this dark?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Be careful you don't slip and fall into\x01",
            "the lake!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_3AD end

    def Function_6_419(): pass

    label("Function_6_419")

    TalkBegin(0xFE)

    ChrTalk(    #2
        0xFE,
        (
            "It's pretty late... I'd better be careful\x01",
            "walking the streets on my way home.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_419 end

    def Function_7_473(): pass

    label("Function_7_473")

    TalkBegin(0xFE)

    ChrTalk(    #3
        0xFE,
        (
            "It looked like a white bird just flew off\x01",
            "to the west.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_473 end

    def Function_8_4B6(): pass

    label("Function_8_4B6")

    TalkBegin(0xFE)

    ChrTalk(    #4
        0xFE,
        "Hey, you there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "You're welcome to walk about late at\x01",
            "night, but be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "If anything happens, shout as loudly\x01",
            "as you can for us.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_4B6 end

    def Function_9_550(): pass

    label("Function_9_550")

    TalkBegin(0xFE)

    ChrTalk(    #7
        0xFE,
        "What are you doing out this late at night?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "If you've got business here, please\x01",
            "come back when it's a bit brighter.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_550 end

    def Function_10_5D4(): pass

    label("Function_10_5D4")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #9
        (
            "\x07\x05House For Sale\x01",
            "※Also Zoned For Food Service\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_10_5D4 end

    def Function_11_633(): pass

    label("Function_11_633")

    SetPlaceName(0xB8)
    Return()

    # Function_11_633 end

    def Function_12_637(): pass

    label("Function_12_637")

    SetPlaceName(0xB7)
    Return()

    # Function_12_637 end

    def Function_13_63B(): pass

    label("Function_13_63B")

    SetPlaceName(0xAF)
    Return()

    # Function_13_63B end

    def Function_14_63F(): pass

    label("Function_14_63F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_911")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_703")
    TurnDirection(0x109, 0x101, 400)

    ChrTalk(    #10
        0x109,
        "#1063FSo these're the sewers?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 400)

    ChrTalk(    #11
        0x101,
        "#1015FYou don't think it's here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x109,
        (
            "#1063FNot too likely.\x02\x03",

            "Let's go somewhere else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        "#1002FUnderstood.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8F0")

    label("loc_703")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79E")

    ChrTalk(    #14
        0x109,
        "#1063FSo these're the sewers?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 400)

    ChrTalk(    #15
        0x101,
        "#1015FYou don't think it's here?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 400)

    ChrTalk(    #16
        0x109,
        (
            "#1063FNot too likely.\x02\x03",

            "Let's go somewhere else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F0")

    label("loc_79E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_852")

    ChrTalk(    #17
        0x103,
        "#0022FOh... These are the sewers, right?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #18
        0x101,
        "#1015FYou don't think it's here?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #19
        0x103,
        (
            "#0022FMmm, doesn't seem too likely.\x02\x03",

            "Let's go somewhere else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F0")

    label("loc_852")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F0")

    ChrTalk(    #20
        0x106,
        "#050FSo these are the sewers, huh?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #21
        0x101,
        "#1015FYou don't think it's here?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #22
        0x106,
        (
            "#050FAin't too likely.\x02\x03",

            "Let's go somewhere else.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F0")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    OP_A2(0x0)
    Jump("loc_AB0")

    label("loc_911")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97A")

    ChrTalk(    #23
        0x101,
        (
            "#1002FDoesn't look like Sieg's come here,\x01",
            "so we should probably go somewhere\x01",
            "else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A95")

    label("loc_97A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E0")

    ChrTalk(    #24
        0x109,
        (
            "#1063FWe can check this place out later.\x01",
            "We'll probably have more luck elsewhere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A95")

    label("loc_9E0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3D")

    ChrTalk(    #25
        0x103,
        (
            "#022FIf we do check here, it'll be last.\x01",
            "First, let's go somewhere else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A95")

    label("loc_A3D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A95")

    ChrTalk(    #26
        0x106,
        (
            "#050FHey, we can come back here later.\x01",
            "Let's try somewhere else first.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A95")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_AB0")

    Jump("loc_C0A")

    label("loc_AB3")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B95")
    TurnDirection(0x109, 0x0, 400)

    ChrTalk(    #27
        0x109,
        (
            "#1063FThis ain't gonna be where the\x01",
            "'tea party' is. Let's hurry to the docks!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B40")
    TurnDirection(0x0, 0x109, 400)

    ChrTalk(    #28
        0x101,
        "#1002FGot it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B8F")

    label("loc_B40")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B6B")
    TurnDirection(0x0, 0x109, 400)

    ChrTalk(    #29
        0x103,
        "#022FOf course.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B8F")

    label("loc_B6B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8F")
    TurnDirection(0x0, 0x109, 400)

    ChrTalk(    #30
        0x106,
        "#050FRight.\x02",
    )

    CloseMessageWindow()

    label("loc_B8F")

    OP_A2(0x0)
    Jump("loc_BEF")

    label("loc_B95")

    TurnDirection(0x109, 0x0, 400)

    ChrTalk(    #31
        0x109,
        (
            "#1063FThis ain't gonna be where the\x01",
            "'tea party' is. Let's hurry to the docks!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BEF")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_C0A")

    Return()

    # Function_14_63F end

    def Function_15_C0B(): pass

    label("Function_15_C0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D77")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CFA")
    TurnDirection(0x109, 0x0, 400)

    ChrTalk(    #32
        0x109,
        (
            "#1063FWe can put the North Block off until later.\x01",
            "First, let's search around here.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA5")
    TurnDirection(0x0, 0x109, 400)

    ChrTalk(    #33
        0x101,
        "#1002FGot it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CF4")

    label("loc_CA5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD0")
    TurnDirection(0x0, 0x109, 400)

    ChrTalk(    #34
        0x103,
        "#022FOf course.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CF4")

    label("loc_CD0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF4")
    TurnDirection(0x0, 0x109, 400)

    ChrTalk(    #35
        0x106,
        "#050FRight.\x02",
    )

    CloseMessageWindow()

    label("loc_CF4")

    OP_A2(0x1)
    Jump("loc_D59")

    label("loc_CFA")

    TurnDirection(0x109, 0x0, 400)

    ChrTalk(    #36
        0x109,
        (
            "#1063FWe can put the North Block off until later.\x01",
            "First, let's search around here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D59")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_ECE")

    label("loc_D77")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E59")
    TurnDirection(0x109, 0x0, 400)

    ChrTalk(    #37
        0x109,
        (
            "#1063FThis ain't gonna be where the\x01",
            "'tea party' is. Let's hurry to the docks!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E04")
    TurnDirection(0x0, 0x109, 400)

    ChrTalk(    #38
        0x101,
        "#1002FGot it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E53")

    label("loc_E04")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E2F")
    TurnDirection(0x0, 0x109, 400)

    ChrTalk(    #39
        0x103,
        "#022FOf course.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E53")

    label("loc_E2F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E53")
    TurnDirection(0x0, 0x109, 400)

    ChrTalk(    #40
        0x106,
        "#050FRight.\x02",
    )

    CloseMessageWindow()

    label("loc_E53")

    OP_A2(0x1)
    Jump("loc_EB3")

    label("loc_E59")

    TurnDirection(0x109, 0x0, 400)

    ChrTalk(    #41
        0x109,
        (
            "#1063FThis ain't gonna be where the\x01",
            "'tea party' is. Let's hurry to the docks!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB3")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_ECE")

    Return()

    # Function_15_C0B end

    def Function_16_ECF(): pass

    label("Function_16_ECF")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #42
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_16_ECF end

    SaveToFile()

Try(main)
