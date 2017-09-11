from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3150   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3150.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        'Kilika',                               # 9
        'Professor Alba',                       # 10
        'Dorothy',                              # 11
        'Factory Chief Murdock',                # 12
        'Stain',                                # 13
        'Elwyn',                                # 14
        'Ada',                                  # 15
        'Knowles',                              # 16
        'Didi',                                 # 17
        'Elkan',                                # 18
        'Gundolf',                              # 19
        'Wong',                                 # 20
        'Bruno',                                # 21
        'Monika',                               # 22
        'Karl',                                 # 23
        'Zin',                                  # 24
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
        'ED6_DT07/CH02610 ._CH',             # 00
        'ED6_DT07/CH02050 ._CH',             # 01
        'ED6_DT07/CH02070 ._CH',             # 02
        'ED6_DT07/CH02620 ._CH',             # 03
        'ED6_DT07/CH01200 ._CH',             # 04
        'ED6_DT07/CH01040 ._CH',             # 05
        'ED6_DT07/CH01030 ._CH',             # 06
        'ED6_DT07/CH01060 ._CH',             # 07
        'ED6_DT07/CH01160 ._CH',             # 08
        'ED6_DT07/CH01140 ._CH',             # 09
        'ED6_DT07/CH01260 ._CH',             # 0A
        'ED6_DT07/CH01760 ._CH',             # 0B
        'ED6_DT07/CH01530 ._CH',             # 0C
        'ED6_DT07/CH02490 ._CH',             # 0D
        'ED6_DT07/CH01190 ._CH',             # 0E
        'ED6_DT07/CH00070 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT07/CH02610P._CP',             # 00
        'ED6_DT07/CH02050P._CP',             # 01
        'ED6_DT07/CH02070P._CP',             # 02
        'ED6_DT07/CH02620P._CP',             # 03
        'ED6_DT07/CH01200P._CP',             # 04
        'ED6_DT07/CH01040P._CP',             # 05
        'ED6_DT07/CH01030P._CP',             # 06
        'ED6_DT07/CH01060P._CP',             # 07
        'ED6_DT07/CH01160P._CP',             # 08
        'ED6_DT07/CH01140P._CP',             # 09
        'ED6_DT07/CH01260P._CP',             # 0A
        'ED6_DT07/CH01760P._CP',             # 0B
        'ED6_DT07/CH01530P._CP',             # 0C
        'ED6_DT07/CH02490P._CP',             # 0D
        'ED6_DT07/CH01190P._CP',             # 0E
        'ED6_DT07/CH00070P._CP',             # 0F
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 0,
        Y                   = 1200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 4220,
        Z                   = 0,
        Y                   = -740,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )


    DeclActor(
        TriggerX            = 3480,
        TriggerZ            = 0,
        TriggerY            = -710,
        TriggerRange        = 400,
        ActorX              = 3500,
        ActorZ              = 1500,
        ActorY              = 1200,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1830,
        TriggerZ            = 1000,
        TriggerY            = 51000,
        TriggerRange        = 400,
        ActorX              = 1780,
        ActorZ              = 2500,
        ActorY              = 53000,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 53210,
        TriggerZ            = 0,
        TriggerY            = 520,
        TriggerRange        = 400,
        ActorX              = 52970,
        ActorZ              = 1500,
        ActorY              = 2400,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1320,
        TriggerZ            = 0,
        TriggerY            = -4700,
        TriggerRange        = 1400,
        ActorX              = -1320,
        ActorZ              = 2000,
        ActorY              = -4700,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 23,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3BA",          # 00, 0
        "Function_1_472",          # 01, 1
        "Function_2_473",          # 02, 2
        "Function_3_489",          # 03, 3
        "Function_4_4AD",          # 04, 4
        "Function_5_61B",          # 05, 5
        "Function_6_68F",          # 06, 6
        "Function_7_710",          # 07, 7
        "Function_8_7D3",          # 08, 8
        "Function_9_820",          # 09, 9
        "Function_10_BE3",         # 0A, 10
        "Function_11_CA4",         # 0B, 11
        "Function_12_E26",         # 0C, 12
        "Function_13_E2B",         # 0D, 13
        "Function_14_192C",        # 0E, 14
        "Function_15_2213",        # 0F, 15
        "Function_16_243F",        # 10, 16
        "Function_17_27A0",        # 11, 17
        "Function_18_27A5",        # 12, 18
        "Function_19_3553",        # 13, 19
        "Function_20_40BA",        # 14, 20
        "Function_21_4CD4",        # 15, 21
        "Function_22_5215",        # 16, 22
        "Function_23_5C8A",        # 17, 23
    )


    def Function_0_3BA(): pass

    label("Function_0_3BA")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_3C6"),
        (SWITCH_DEFAULT, "loc_3DE"),
    )


    label("loc_3C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DB")
    SetMapFlags(0x10000000)
    Event(0, 21)

    label("loc_3DB")

    Jump("loc_3DE")

    label("loc_3DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_471")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_403")
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 4220, 0, -740, 0)

    label("loc_403")

    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 1780, 1000, 53000, 183)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 52200, 0, 53760, 270)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 52110, 0, 50520, 255)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 59030, 0, 54500, 355)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 52970, 0, 2400, 172)

    label("loc_471")

    Return()

    # Function_0_3BA end

    def Function_1_472(): pass

    label("Function_1_472")

    Return()

    # Function_1_472 end

    def Function_2_473(): pass

    label("Function_2_473")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_488")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_473")

    label("loc_488")

    Return()

    # Function_2_473 end

    def Function_3_489(): pass

    label("Function_3_489")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4AC")
    OP_8D(0xFE, 52620, 51160, 59990, 53120, 3000)
    Jump("Function_3_489")

    label("loc_4AC")

    Return()

    # Function_3_489 end

    def Function_4_4AD(): pass

    label("Function_4_4AD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_617")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_510")

    ChrTalk(    #0
        0xFE,
        "It sure is noisy outside.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Are the kids skipping Sunday\x01",
            "School again?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_617")

    label("loc_510")

    OP_A2(0xB)

    ChrTalk(    #2
        0xFE,
        (
            "This orbal gun is able to maximize the\x01",
            "energy output of its control orbment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "It's a little off-balance and needs\x01",
            "a little more polish, but still, it's\x01",
            "up to spec.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "We're progressing nicely. We'll\x01",
            "have a production unit on the\x01",
            "shelves in no time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_617")

    TalkEnd(0xFE)
    Return()

    # Function_4_4AD end

    def Function_5_61B(): pass

    label("Function_5_61B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_68B")

    ChrTalk(    #5
        0x110,
        (
            "#150FEstelle! Let me know if you\x01",
            "find out anything, okay?\x02\x03",

            "This has 'SCOOP' written all\x01",
            "over it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68B")

    TalkEnd(0xFE)
    Return()

    # Function_5_61B end

    def Function_6_68F(): pass

    label("Function_6_68F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_70C")

    ChrTalk(    #6
        0xFE,
        "Product Descriptions...ugh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "Rate of fire...accuracy index...\x01",
            "projected run time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "It's all so dry!\x02",
    )

    CloseMessageWindow()

    label("loc_70C")

    TalkEnd(0xFE)
    Return()

    # Function_6_68F end

    def Function_7_710(): pass

    label("Function_7_710")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_7CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_773")

    ChrTalk(    #9
        0xFE,
        "What was it? Zhon? No.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "Vahn? Was that it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "No, that's not right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7CF")

    label("loc_773")

    OP_A2(0x9)

    ChrTalk(    #12
        0xFE,
        (
            "You know the guy I hired as my\x01",
            "last bodyguard, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "What was his name again?\x02",
    )

    CloseMessageWindow()

    label("loc_7CF")

    TalkEnd(0xFE)
    Return()

    # Function_7_710 end

    def Function_8_7D3(): pass

    label("Function_8_7D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_81C")

    ChrTalk(    #14
        0x10E,
        (
            "#130FThis looks like quite a mess.\x02\x03",

            "Do try to be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81C")

    TalkEnd(0xFE)
    Return()

    # Function_8_7D3 end

    def Function_9_820(): pass

    label("Function_9_820")

    TalkBegin(0x8)
    FadeToDark(300, 0, 70)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",        # 0
            "Report\x01",      # 1
            "Leave\x01",       # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98B")
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_A9(0x40)"), scpexpr(EXPR_END)), "loc_910")
    Sleep(200)

    ChrTalk(    #15
        0x8,
        (
            "#790FWelcome back. It looks like\x01",
            "you've finished your job.\x02\x03",

            "If you clear any other contracts,\x01",
            "make sure you come here and\x01",
            "report it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_982")

    label("loc_910")

    Sleep(200)

    ChrTalk(    #16
        0x8,
        (
            "#790FNothing to report today?\x02\x03",

            "If you clear any other contracts,\x01",
            "make sure you come here and\x01",
            "report it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_982")

    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_98B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_99C")
    TalkEnd(0x8)
    Return()

    label("loc_99C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 6)), scpexpr(EXPR_END)), "loc_9FF")

    ChrTalk(    #17
        0x8,
        (
            "#790FIt looks like you found yourself\x01",
            "some Zemuria Moss.\x02\x03",

            "Hurry. Get to the church.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BDF")

    label("loc_9FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_BDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5C")

    ChrTalk(    #18
        0x8,
        (
            "#790FAgate doesn't have a moment\x01",
            "to spare.\x02\x03",

            "Hurry. Get to the church.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BDF")

    label("loc_A5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B83")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 3400, 0, -1800, 0)
    SetChrPos(0x102, 3600, 0, -3160, 0)
    SetChrPos(0x107, 4470, 0, -2270, 0)
    TurnDirection(0x8, 0x101, 0)
    OP_8C(0x17, 180, 0)
    OP_4A(0x17, 255)
    OP_6D(3390, 0, -770, 1000)

    ChrTalk(    #19
        0x8,
        "#790FWhat did Father Vixen say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x102,
        "#012FHe said...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #21
        "\x07\x05Joshua relayed the information about the Zemuria Moss.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #22
        0x17,
        "#073FMoss, is it?\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Call(0, 22)
    Jump("loc_BDF")

    label("loc_B83")


    ChrTalk(    #23
        0x8,
        (
            "#790FYou've got Zin with you,\x01",
            "so take advantage of him.\x02\x03",

            "He's tough.\x01",
            "He can handle it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BDF")

    TalkEnd(0x8)
    Return()

    # Function_9_820 end

    def Function_10_BE3(): pass

    label("Function_10_BE3")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C35")

    ChrTalk(    #24
        0x17,
        (
            "#070FIs something wrong?\x02\x03",

            "Don't you need to get to\x01",
            "the church?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA0")

    label("loc_C35")


    ChrTalk(    #25
        0x17,
        (
            "#070FWell? What's the good word?\x02\x03",

            "Talk to Kilika if you need anything.\x01",
            "She's as reliable as they get!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA0")

    TalkEnd(0x17)
    Return()

    # Function_10_BE3 end

    def Function_11_CA4(): pass

    label("Function_11_CA4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_CEF")

    ChrTalk(    #26
        0xFE,
        (
            "I'm glad there wasn't any damage\x01",
            "to my store.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E22")

    label("loc_CEF")

    OP_A2(0x1)

    ChrTalk(    #27
        0xFE,
        (
            "I was so surprised when the\x01",
            "orbments shut down last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "I'd heard there were some rare\x01",
            "quartz crystals that could do\x01",
            "such a thing, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "...I didn't know it could be done\x01",
            "over such a wide radius.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "If that were weaponized, any arms\x01",
            "race between countries would be\x01",
            "completely upset.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E22")

    TalkEnd(0xFE)
    Return()

    # Function_11_CA4 end

    def Function_12_E26(): pass

    label("Function_12_E26")

    Call(0, 13)
    Return()

    # Function_12_E26 end

    def Function_13_E2B(): pass

    label("Function_13_E2B")

    TalkBegin(0xD)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA3")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 1)), scpexpr(EXPR_END)), "loc_E8C")
    OP_A9(0x4C)
    Jump("loc_E9A")

    label("loc_E8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_E98")
    OP_A9(0x4B)
    Jump("loc_E9A")

    label("loc_E98")

    OP_A9(0x3E)

    label("loc_E9A")

    OP_56(0x0)
    TalkEnd(0xD)
    Return()

    label("loc_EA3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EB4")
    TalkEnd(0xD)
    Return()

    label("loc_EB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_F9E")

    ChrTalk(    #31
        0xD,
        (
            "Good morning and welcome to\x01",
            "Bell Station!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xD,
        (
            "We have a wide selection of\x01",
            "the finest quality goods,\x01",
            "suited for your every need!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xD,
        "So...buy somethin' will ya!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xD,
        (
            "This store's success hinges on\x01",
            "all of my customers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1928")

    label("loc_F9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_FF5")

    ChrTalk(    #35
        0xD,
        "Hello there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xD,
        (
            "Here at Bell Station we have\x01",
            "anything you might need!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1928")

    label("loc_FF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_122D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_10A6")

    ChrTalk(    #37
        0xD,
        "My wife finally understands...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xD,
        (
            "...and told me I didn't have to\x01",
            "expand our product line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xD,
        (
            "My wife finally gets it. That\x01",
            "alone is a huge motivator.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_122A")

    label("loc_10A6")

    OP_A2(0x2)

    ChrTalk(    #40
        0xD,
        "Good morning!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xD,
        "I'm having a great day so far.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xD,
        (
            "Finally, my wife seems to be\x01",
            "getting what I'm doing... \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xD,
        (
            "She told me that we don't need\x01",
            "to expand our product line any\x01",
            "more than we have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xD,
        (
            "Running your own business can\x01",
            "be tough, so finding ways to\x01",
            "economize is top priority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xD,
        (
            "And not being forced to expand\x01",
            "will go a long way for both my\x01",
            "wallet and my customers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_122A")

    Jump("loc_1928")

    label("loc_122D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_1384")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_12BA")

    ChrTalk(    #46
        0xD,
        (
            "Hmm...usually my wife gets\x01",
            "angry at me when I cut prices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xD,
        (
            "But she's been in good spirits\x01",
            "lately. What's going on?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1381")

    label("loc_12BA")

    OP_A2(0x2)

    ChrTalk(    #48
        0xD,
        "My wife's been acting strange.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xD,
        (
            "She knows that during the incident\x01",
            "at the central factory I was giving\x01",
            "some of our products away for free.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xD,
        (
            "But she hasn't said a word about\x01",
            "it to me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1381")

    Jump("loc_1928")

    label("loc_1384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_14F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_13FC")

    ChrTalk(    #51
        0xD,
        (
            "My wife Ada gets such a stiff\x01",
            "neck sometimes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xD,
        (
            "She went to the church to get\x01",
            "some medicine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14ED")

    label("loc_13FC")

    OP_A2(0x2)

    ChrTalk(    #53
        0xD,
        (
            "My wife Ada gets such a stiff\x01",
            "neck sometimes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xD,
        (
            "She went to the church to get\x01",
            "some medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xD,
        (
            "I know they're researching\x01",
            "medicine at the central\x01",
            "factory as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xD,
        (
            "But they still have nothing on\x01",
            "the traditional remedies.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14ED")

    Jump("loc_1928")

    label("loc_14F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_1618")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_158B")

    ChrTalk(    #57
        0xD,
        (
            "My oldest boy has got quite an\x01",
            "interest in product placement\x01",
            "and presentation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xD,
        (
            "If I left him alone he'd spend\x01",
            "all day doing it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1615")

    label("loc_158B")

    OP_A2(0x2)
    TurnDirection(0xD, 0xF, 400)

    ChrTalk(    #59
        0xD,
        "Knowles!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xD,
        (
            "You need to stop handling the\x01",
            "merchandise so much!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xD,
        (
            "Remember your promise?\x01",
            "One arrangement per day.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)

    label("loc_1615")

    Jump("loc_1928")

    label("loc_1618")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_17AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_169E")

    ChrTalk(    #62
        0xD,
        (
            "The orbment in the center of town\x01",
            "actually stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xD,
        (
            "Guess this world is still full\x01",
            "of surprises, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17AB")

    label("loc_169E")

    OP_A2(0x2)

    ChrTalk(    #64
        0xD,
        "Were you all okay last night?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xD,
        (
            "I'd thought the lights had just\x01",
            "broken or something and was\x01",
            "on my way to the factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xD,
        (
            "When I got outside though, \x01",
            "the entire town was dark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xD,
        (
            "I don't have to be a genius to\x01",
            "know that something wasn't\x01",
            "right about that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17AB")

    Jump("loc_1928")

    label("loc_17AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_18A8")

    ChrTalk(    #68
        0xD,
        (
            "I'd love it if everybody thought\x01",
            "of my place as the little\x01",
            "'neighborhood' store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xD,
        (
            "I try to keep a little something\x01",
            "for everyone on the shelves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xD,
        (
            "It's hard to balance the logistics,\x01",
            "but nothing worthwhile ever came\x01",
            "easy, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1928")

    label("loc_18A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1928")

    ChrTalk(    #71
        0xD,
        (
            "Come on in!\x01",
            "Welcome to Bell Station!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xD,
        (
            "We're the only store that carries\x01",
            "everything from food to everyday\x01",
            "goods!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1928")

    TalkEnd(0xD)
    Return()

    # Function_13_E2B end

    def Function_14_192C(): pass

    label("Function_14_192C")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_199F")

    ChrTalk(    #73
        0xE,
        (
            "Looks like another hard month\x01",
            "ahead for us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xE,
        (
            "But we'll be ready for it and\x01",
            "get through it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_220F")

    label("loc_199F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_19D3")

    ChrTalk(    #75
        0xE,
        "Hello!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xE,
        "Welcome to Bell Station!\x02",
    )

    CloseMessageWindow()
    Jump("loc_220F")

    label("loc_19D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1AEA")

    ChrTalk(    #77
        0xE,
        (
            "I had a long talk with my husband\x01",
            "this morning about the direction\x01",
            "of this store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xE,
        (
            "We decided not to expand our\x01",
            "line of merchandise any more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xE,
        (
            "And I'm to be in charge of\x01",
            "product ordering and stock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xE,
        (
            "I wonder how it'll go. We won't\x01",
            "know without trying.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_220F")

    label("loc_1AEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_1CEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1C11")

    ChrTalk(    #81
        0xE,
        (
            "But still...I think I'm starting to\x01",
            "see what my husband is trying\x01",
            "to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xE,
        (
            "My husband is a bit more of a\x01",
            "dreamer than a salesman...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xE,
        (
            "...but he really wants to help\x01",
            "this community.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xE,
        (
            "It'd be so amazing if we could\x01",
            "build the kind of store that\x01",
            "realizes that dream.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CE9")

    label("loc_1C11")

    OP_A2(0x3)

    ChrTalk(    #85
        0xE,
        (
            "Today, my husband was out at\x01",
            "the central factory after the\x01",
            "incident giving out free supplies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xE,
        (
            "It's going to put us into the\x01",
            "red for the month...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xE,
        (
            "...but that's fine. We'll just\x01",
            "consider it pro bono.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CE9")

    Jump("loc_220F")

    label("loc_1CEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1E31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1D7F")

    ChrTalk(    #88
        0xE,
        (
            "I can't believe the central factory\x01",
            "was attacked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xE,
        (
            "How did my husband figure out\x01",
            "that something had happened\x01",
            "so quickly?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E2E")

    label("loc_1D7F")

    OP_A2(0x3)

    ChrTalk(    #90
        0xE,
        (
            "Is it true that someone attacked\x01",
            "the central factory?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xE,
        (
            "My husband left a little while ago,\x01",
            "and he still hasn't come home yet... \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xE,
        "I hope nothing's happened...\x02",
    )

    CloseMessageWindow()

    label("loc_1E2E")

    Jump("loc_220F")

    label("loc_1E31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1EE8")

    ChrTalk(    #93
        0xE,
        (
            "My husband said that something\x01",
            "seemed wrong and then he rushed\x01",
            "out of the store. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xE,
        (
            "He took a lot of merchandise\x01",
            "along with him, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xE,
        "What is he thinking...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_220F")

    label("loc_1EE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2001")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1F83")

    ChrTalk(    #96
        0xE,
        (
            "Oh well. I still have plenty\x01",
            "of work to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xE,
        (
            "I'll just tidy up and then go to\x01",
            "the church to get some medicine\x01",
            "for my stiff neck.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FFE")

    label("loc_1F83")

    OP_A2(0x3)

    ChrTalk(    #98
        0xE,
        (
            "We've been able to accomplish\x01",
            "so much due to the orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xE,
        (
            "But yesterday's incident made\x01",
            "me start thinking...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FFE")

    Jump("loc_220F")

    label("loc_2001")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2178")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_20AD")

    ChrTalk(    #100
        0xE,
        (
            "If we don't keep our best selling\x01",
            "product in stock, we won't make\x01",
            "any profits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xE,
        (
            "Oh, my shoulders are so stiff it's\x01",
            "started to give me a headache.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2175")

    label("loc_20AD")

    OP_A2(0x3)

    ChrTalk(    #102
        0xE,
        (
            "My husband never orders the\x01",
            "proper amounts of anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xE,
        (
            "I keep telling him to take more\x01",
            "care of the merchandise that\x01",
            "sells better...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xE,
        (
            "Doesn't he know anything about\x01",
            "being a salesman?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2175")

    Jump("loc_220F")

    label("loc_2178")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_220F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_21D0")

    ChrTalk(    #105
        0xE,
        (
            "Looking at our books makes my\x01",
            "neck and shoulders start acting\x01",
            "up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_220F")

    label("loc_21D0")

    OP_A2(0x3)

    ChrTalk(    #106
        0xE,
        "...Oh dear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xE,
        (
            "This month's going to be\x01",
            "a tight one.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_220F")

    TalkEnd(0xE)
    Return()

    # Function_14_192C end

    def Function_15_2213(): pass

    label("Function_15_2213")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_2260")

    ChrTalk(    #108
        0xFE,
        "That was strange.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "Mom actually paid Dad\x01",
            "a compliment!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_243B")

    label("loc_2260")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_22F6")

    ChrTalk(    #110
        0xFE,
        (
            "Dad took a lot of stuff with\x01",
            "him when he left...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "I can understand the food and\x01",
            "medicine, but why dolls?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        "What a mess this is.\x02",
    )

    CloseMessageWindow()
    Jump("loc_243B")

    label("loc_22F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_233A")

    ChrTalk(    #113
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        "...There. Perfect.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        "It's fine as it is.\x02",
    )

    CloseMessageWindow()
    Jump("loc_243B")

    label("loc_233A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_243B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_23C4")

    ChrTalk(    #116
        0xFE,
        (
            "Dad told me to only rearrange\x01",
            "the shelves once a day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "But I've got to put back the\x01",
            "stuff that customers moved!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_243B")

    label("loc_23C4")

    OP_A2(0x4)

    ChrTalk(    #118
        0xFE,
        (
            "And this fish should go a little\x01",
            "more to the left...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        "...There we are.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        "Everything's all balanced now.\x02",
    )

    CloseMessageWindow()

    label("loc_243B")

    TalkEnd(0xFE)
    Return()

    # Function_15_2213 end

    def Function_16_243F(): pass

    label("Function_16_243F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_24D6")

    ChrTalk(    #121
        0xFE,
        (
            "Hurry, Doctor!\x01",
            "It's an emergency!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "Mommy's neck is stiff again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "What's that, you say? We must\x01",
            "contact Father Vixen at once!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_279C")

    label("loc_24D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_2512")

    ChrTalk(    #124
        0xFE,
        (
            "It isn't dark outside like it\x01",
            "was yesterday!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_279C")

    label("loc_2512")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2541")

    ChrTalk(    #125
        0xFE,
        "Mommy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        "Where'd Daddy go?\x02",
    )

    CloseMessageWindow()
    Jump("loc_279C")

    label("loc_2541")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_25A3")

    ChrTalk(    #127
        0xFE,
        "Yesterday it was dark out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "It was like when I stick my\x01",
            "head under the covers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_279C")

    label("loc_25A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_276A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_265C")

    ChrTalk(    #129
        0xFE,
        (
            "Professor! The orbal...pr-pr-...\x01",
            "precushion is dropping!\x01",
            "We need MOAR POWAH STAT!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "What's that? But the Orbal\x01",
            "Engine readings are green!\x01",
            "GREEEEEN, I TELL YOU!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2767")

    label("loc_265C")

    OP_A2(0x5)

    ChrTalk(    #131
        0xFE,
        "It's TITA!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "Tita, let's play Orbaldilly Engineers\x01",
            "again! This time I get to hobgoblin\x01",
            "the ding-bezel-orbalerator, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x107,
        (
            "#060FSorry, Didi. I have to show my\x01",
            "friends around first.\x02\x03",

            "Maybe next time, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        "Oookaaay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        "Yes, MA'AM, PROFESSOR TITA!\x02",
    )

    CloseMessageWindow()

    label("loc_2767")

    Jump("loc_279C")

    label("loc_276A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_279C")

    ChrTalk(    #136
        0xFE,
        (
            "Who are you guys?\x01",
            "Pirates? Or ninjas?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_279C")

    TalkEnd(0xFE)
    Return()

    # Function_16_243F end

    def Function_17_27A0(): pass

    label("Function_17_27A0")

    Call(0, 18)
    Return()

    # Function_17_27A0 end

    def Function_18_27A5(): pass

    label("Function_18_27A5")

    TalkBegin(0x11)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2805")
    OP_0D()
    OP_A9(0x3D)
    OP_56(0x0)
    TalkEnd(0x11)
    Return()

    label("loc_2805")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2816")
    TalkEnd(0x11)
    Return()

    label("loc_2816")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2A09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_28F4")

    ChrTalk(    #137
        0x11,
        (
            "Say what you like, Stain has it\x01",
            "pretty well made. I should learn\x01",
            "from his example.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x11,
        (
            "I think he's a bit too set in his\x01",
            "ways of course, but..\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x11,
        (
            "That's all part of the learning\x01",
            "experience, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A06")

    label("loc_28F4")

    OP_A2(0x6)

    ChrTalk(    #140
        0x11,
        (
            "Yesterday I talked to Stain,\x01",
            "the owner, about our stock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x11,
        (
            "I decided to try going with his\x01",
            "recommendations this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x11,
        (
            "That doesn't mean I've started\x01",
            "subscribing to his 'Dependable\x01",
            "Above All' philosophy yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x11,
        (
            "But it's all part of the\x01",
            "learning experience.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A06")

    Jump("loc_354F")

    label("loc_2A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2B4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2A97")

    ChrTalk(    #144
        0x11,
        (
            "I didn't think Karl'd ever say\x01",
            "that about Stain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x11,
        (
            "Guess he's started thinking\x01",
            "like him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x11,
        "Great. It's spreading.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B4A")

    label("loc_2A97")

    OP_A2(0x6)

    ChrTalk(    #147
        0x11,
        (
            "Early this morning Karl came to\x01",
            "the store and said, 'I get what\x01",
            "Stain means now,' and left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x11,
        (
            "I didn't think Karl'd ever say\x01",
            "that about Stain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x11,
        "Maybe he's...right?\x02",
    )

    CloseMessageWindow()

    label("loc_2B4A")

    Jump("loc_354F")

    label("loc_2B4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2C36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2BB0")

    ChrTalk(    #150
        0x11,
        "That engineer, Karl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x11,
        (
            "It seems like Stain's indoctrinated\x01",
            "him at last.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C33")

    label("loc_2BB0")

    OP_A2(0x6)

    ChrTalk(    #152
        0x11,
        (
            "Early this morning Karl came to\x01",
            "the store and said, 'I get what\x01",
            "Stain means now,' and left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x11,
        "What could have happened?\x02",
    )

    CloseMessageWindow()

    label("loc_2C33")

    Jump("loc_354F")

    label("loc_2C36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_2C93")

    ChrTalk(    #154
        0x11,
        "Hey, thanks for staying!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x11,
        (
            "I'm not closing up just yet,\x01",
            "so take your time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_354F")

    label("loc_2C93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2D75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2CFA")

    ChrTalk(    #156
        0x11,
        "Was anything damaged?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x11,
        (
            "I hope this doesn't disrupt the\x01",
            "research timetable...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D72")

    label("loc_2CFA")

    OP_A2(0x6)

    ChrTalk(    #158
        0x11,
        (
            "Hey, did you hear?! The central\x01",
            "factory was attacked! \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x11,
        (
            "I was inside the store talking,\x01",
            "so I didn't see it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D72")

    Jump("loc_354F")

    label("loc_2D75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2EF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2DE3")

    ChrTalk(    #160
        0x11,
        "Now THAT is an orbal gun.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x11,
        (
            "If it were a little better balanced,\x01",
            "it'd sell like mad.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EF3")

    label("loc_2DE3")

    OP_A2(0x6)

    ChrTalk(    #162
        0x11,
        (
            "Karl from the central factory\x01",
            "brought over an experimental\x01",
            "orbal gun!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x11,
        (
            "It's a fine weapon. Got some\x01",
            "real power behind it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x11,
        (
            "It's a bit unbalanced and kind\x01",
            "of finicky sometimes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x11,
        (
            "...but I think you can overlook that\x01",
            "in light of its raw stopping power.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EF3")

    Jump("loc_354F")

    label("loc_2EF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_310F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2F7A")

    ChrTalk(    #166
        0x11,
        (
            "I really hope Karl brings us a\x01",
            "test unit soon...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x11,
        (
            "It's about the only thing I look\x01",
            "forward to these days.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_310C")

    label("loc_2F7A")

    OP_A2(0x6)

    ChrTalk(    #168
        0x11,
        "Hello, come on in.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x11,
        (
            "Stain, the owner, and I had\x01",
            "some words again about\x01",
            "stocking policies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x11,
        (
            "He just doesn't want us to carry\x01",
            "any of the experimental orbal\x01",
            "weapons here yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x11,
        (
            "I tried sticking to my ideas, but\x01",
            "in the end it's not my decision.\x01",
            "It's his store, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x11,
        (
            "I really hope Karl brings us a\x01",
            "test unit soon...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x11,
        (
            "It's about the only thing I look\x01",
            "forward to these days.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_310C")

    Jump("loc_354F")

    label("loc_310F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3239")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_319B")

    ChrTalk(    #174
        0x11,
        (
            "There's something big going on\x01",
            "at the central factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x11,
        (
            "All of their measuring devices\x01",
            "have to be going nuts.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3236")

    label("loc_319B")

    OP_A2(0x6)

    ChrTalk(    #176
        0x11,
        (
            "Last night I was tinkering with\x01",
            "that orbal gun...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x11,
        (
            "When suddenly my analyzer just\x01",
            "went dead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x11,
        (
            "I thought for a second I had\x01",
            "broken the gun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3236")

    Jump("loc_354F")

    label("loc_3239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_348F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_32D5")

    ChrTalk(    #179
        0x11,
        (
            "I can appreciate the owner's\x01",
            "philosophy about dependability\x01",
            "as much as anybody...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x11,
        (
            "...but he's too hardheaded about\x01",
            "it sometimes!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_348C")

    label("loc_32D5")

    OP_A2(0x6)

    ChrTalk(    #181
        0x11,
        (
            "This store's owner is Stain,\x01",
            "the guy who lives just next\x01",
            "door to here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x11,
        (
            "He's really pushing for us not to carry\x01",
            "any of the new cutting-edge weaponry.\x01",
            "Takes the joy out of the job, I tell ya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x11,
        (
            "He says that the newest stuff\x01",
            "isn't reliable enough for him to\x01",
            "stock in good faith...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x11,
        (
            "But he's turning down the newest prototypes from\x01",
            "the best factory inventors! Some of these things\x01",
            "can perforate a Rhinocider! What a waste!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_348C")

    Jump("loc_354F")

    label("loc_348F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_354F")

    ChrTalk(    #185
        0x11,
        (
            "Greetings, weapon enthusiasts!\x01",
            "Welcome to Stain Arms & Guards!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x11,
        (
            "Do the sight of fell accoutrements make\x01",
            "your palms sweaty? Well, shop here!\x01",
            "We cater to the violently-inclined!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_354F")

    TalkEnd(0x11)
    Return()

    # Function_18_27A5 end

    def Function_19_3553(): pass

    label("Function_19_3553")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_36CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_35F3")

    ChrTalk(    #187
        0xFE,
        (
            "I know the scientists are leery,\x01",
            "but I think we should trust\x01",
            "Agate on this one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "There are things sometimes that\x01",
            "we just gotta do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36C8")

    label("loc_35F3")


    ChrTalk(    #189
        0xFE,
        (
            "Hey, you guys. I heard about your\x01",
            "little rescue mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        (
            "I know it's not the ending you're\x01",
            "looking for, but we ought to trust\x01",
            "Agate on this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "He'll be able to get those\x01",
            "scientists out of there safe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36C8")

    Jump("loc_40B6")

    label("loc_36CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_3BA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 6)), scpexpr(EXPR_END)), "loc_379F")

    ChrTalk(    #192
        0xFE,
        (
            "Glad to see Wong working\x01",
            "so hard in my absence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "I was worried he was going to\x01",
            "get down on himself because\x01",
            "of the incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "Guess Kilika knocked that\x01",
            "nonsense out of him, though!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BA3")

    label("loc_379F")

    OP_A2(0x57E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 5)), scpexpr(EXPR_END)), "loc_3861")

    ChrTalk(    #195
        0x101,
        "#000FGundolf!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x102,
        "#010FYou're back from the capital?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "Yeah, I got the news. I flew\x01",
            "back quick as I could.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        "I got the rundown from Kilika...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        "...but is Agate okay?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3945")

    label("loc_3861")


    ChrTalk(    #200
        0xFE,
        (
            "You guys are those junior\x01",
            "bracers, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        "I'm Gundolf, Zeiss branch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "I got the news and came from\x01",
            "my other assignment in the\x01",
            "capital as soon as I could.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "I got the rundown from Kilika,\x01",
            "but is Agate all right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3945")


    ChrTalk(    #204
        0x101,
        (
            "#000FHe seems past the worst of it.\x02\x03",

            "Wait a second, are you one\x01",
            "of Agate's friends?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        (
            "Yeah, we've run into each other\x01",
            "a few times out in the field.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "He's kind of made a name for\x01",
            "himself by doing the stuff that's\x01",
            "patently insane.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        (
            "But what doesn't kill him only\x01",
            "makes him stronger, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "You guys and Agate are okay\x01",
            "to handle the rest of this\x01",
            "assignment, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "I should be able to help out a\x01",
            "little with some of the smaller\x01",
            "details, if you want...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x101,
        (
            "#000FThanks, Gundolf!\x02\x03",

            "That'd be great of you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x102,
        "#010FThank you again, Gundolf.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "No problem.\x01",
            "I'm counting on you, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BA3")

    Jump("loc_40B6")

    label("loc_3BA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_40B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_403A")
    OP_A2(0x57D)

    ChrTalk(    #213
        0x13,
        "What? An assignment?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x13,
        "You? Now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x12,
        "Yeah, just a little one.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x12,
        (
            "The army kind of asked for me\x01",
            "specifically...so I'm off to the\x01",
            "capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x12,
        (
            "It's not just you, anyway...\x01",
            "you've got those two juniors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x12,
        (
            "Put your heads together. You'll\x01",
            "be fine. I won't be gone more\x01",
            "than a couple of days or so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x13,
        "Yes, sir...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x13,
        "I'll do my best.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x12,
        "Good. And relax.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x12,
        "Hello.  \x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x0, 400)

    ChrTalk(    #223
        0x12,
        "Who's this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x12,
        "You guys have good timing.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E33")
    OP_A2(0x57C)

    ChrTalk(    #225
        0x13,
        "...Excuse me?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x0, 400)

    ChrTalk(    #226
        0x13,
        (
            "You wouldn't, by any chance,\x01",
            "be junior bracers would you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x101,
        (
            "#000FWhat?\x02\x03",

            "Y-Yeah, we are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x102,
        "#010FI'm Junior Bracer Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x101,
        "#000FI'm Estelle.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E81")

    label("loc_3E33")

    TurnDirection(0x13, 0x0, 400)

    ChrTalk(    #230
        0x13,
        "Estelle, Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x13,
        (
            "You've shown up at quite a\x01",
            "convenient time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E81")


    ChrTalk(    #232
        0x12,
        "So, it IS you two.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x12,
        "Just like Kilika said.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x102,
        (
            "#010FExcuse me...are you on your\x01",
            "way to the capital?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x12,
        (
            "Yeah, I was. A small...request...\x01",
            "came up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x12,
        (
            "I'm leaving things here in Zeiss\x01",
            "to you two and Wong for the\x01",
            "time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x12,
        "Don't burn the place down!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x13,
        (
            "...So, yes.\x01",
            "We could use your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x101,
        "#000FSure. You can rely on us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x102,
        "#010FWe'll do our best.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x12,
        (
            "It's settled then. I'll leave\x01",
            "things to you all.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x10)
    ClearChrFlags(0x13, 0x10)
    Jump("loc_40B6")

    label("loc_403A")


    ChrTalk(    #242
        0x12,
        (
            "Don't do anything that'll make\x01",
            "me regret leaving you guys in\x01",
            "charge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x12,
        (
            "Make sure you give them a\x01",
            "proper hand, Wong.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40B6")

    TalkEnd(0x12)
    Return()

    # Function_19_3553 end

    def Function_20_40BA(): pass

    label("Function_20_40BA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_420A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_415A")

    ChrTalk(    #244
        0xFE,
        (
            "I heard you were on your way\x01",
            "to the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        (
            "It'll be fine...you two are going\x01",
            "to make great bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0xFE,
        "Good luck to you both.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4207")

    label("loc_415A")

    OP_A2(0x8)

    ChrTalk(    #247
        0xFE,
        "Hello, you two...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        (
            "I heard about how well your\x01",
            "rescue mission went.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "It's still too early to pat ourselves\x01",
            "on the backs...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xFE,
        "...but you did good. Thanks.\x02",
    )

    CloseMessageWindow()

    label("loc_4207")

    Jump("loc_4CD0")

    label("loc_420A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_471D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_469E")
    OP_A2(0x57D)

    ChrTalk(    #251
        0x13,
        "What? An assignment?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x13,
        "You? Now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x12,
        "Yeah, just a little one.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x12,
        (
            "The army kind of asked for me\x01",
            "specifically...so I'm off to the\x01",
            "capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x12,
        (
            "It's not just you, anyway...\x01",
            "you've got those two juniors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x12,
        (
            "Put your heads together. You'll\x01",
            "be fine. I won't be gone more\x01",
            "than a couple of days or so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x13,
        "Yes, sir...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x13,
        "I'll do my best.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x12,
        "Good. And relax.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x12,
        "Hello.  \x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x0, 400)

    ChrTalk(    #261
        0x12,
        "Who's this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x12,
        "You guys have good timing.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4497")
    OP_A2(0x57C)

    ChrTalk(    #263
        0x13,
        "...Excuse me?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x0, 400)

    ChrTalk(    #264
        0x13,
        (
            "You wouldn't, by any chance,\x01",
            "be junior bracers would you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x101,
        (
            "#000FWhat?\x02\x03",

            "Y-Yeah, we are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x102,
        "#010FI'm Junior Bracer Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x101,
        "#000FI'm Estelle.\x02",
    )

    CloseMessageWindow()
    Jump("loc_44E5")

    label("loc_4497")

    TurnDirection(0x13, 0x0, 400)

    ChrTalk(    #268
        0x13,
        "Estelle, Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x13,
        (
            "You've shown up at quite a\x01",
            "convenient time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44E5")


    ChrTalk(    #270
        0x12,
        "So, it IS you two.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x12,
        "Just like Kilika said.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x102,
        (
            "#010FExcuse me...are you on your\x01",
            "way to the capital?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x12,
        (
            "Yeah, I was. A small...request...\x01",
            "came up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x12,
        (
            "I'm leaving things here in Zeiss\x01",
            "to you two and Wong for the\x01",
            "time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x12,
        "Don't burn the place down!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x13,
        (
            "...So, yes.\x01",
            "We could use your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x101,
        "#000FSure. You can rely on us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x102,
        "#010FWe'll do our best.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x12,
        (
            "It's settled then. I'll leave\x01",
            "things to you all.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x10)
    ClearChrFlags(0x13, 0x10)
    Jump("loc_471A")

    label("loc_469E")


    ChrTalk(    #280
        0xFE,
        (
            "Gundolf won't be here for the\x01",
            "time being...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xFE,
        (
            "We'll just have to make that\x01",
            "much extra effort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        "Got it, you two?\x02",
    )

    CloseMessageWindow()

    label("loc_471A")

    Jump("loc_4CD0")

    label("loc_471D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_4B71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B09")
    OP_A2(0x57C)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_477D")

    ChrTalk(    #283
        0xFE,
        "Oh, Tita!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        (
            "Strange, seeing you in the\x01",
            "weapons shop...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_479E")

    label("loc_477D")


    ChrTalk(    #285
        0xFE,
        "Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        "If it isn't Tita!\x02",
    )

    CloseMessageWindow()

    label("loc_479E")


    ChrTalk(    #287
        0xFE,
        "Hey...these guys are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x107,
        (
            "#060FThat's right. They're bracers.\x02\x03",

            "I'm showing them to my house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xFE,
        "Yeah, I thought so!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xFE,
        "I'm Wong, Zeiss branch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0xFE,
        (
            "I'm new here myself, so we're\x01",
            "kind of in the same boat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x101,
        (
            "#000FIs that right? Well, it's great\x01",
            "to meet you.\x02\x03",

            "I'm Junior Bracer Estelle.\x01",
            "This is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x102,
        (
            "#010FJoshua.\x02\x03",

            "A pleasure to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xFE,
        (
            "I'd heard from Kilika earlier\x01",
            "about some pretty amazing\x01",
            "juniors coming to Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        "Your reputation precedes you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x101,
        "#000FAw, you're making me blush.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x102,
        (
            "#010FI'm afraid we're not quite as\x01",
            "good as you might have heard.\x01",
            "We were just lucky.\x02\x03",

            "We had the help of some amazing\x01",
            "senior bracers and some very\x01",
            "generous civilians.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xFE,
        (
            "Ha, charisma is a praise-worthy\x01",
            "quality too, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xFE,
        (
            "At any rate, we're understaffed.\x01",
            "We need you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0xFE,
        "Welcome aboard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x101,
        "#000FThank you, Wong.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x102,
        "#010FIndeed. Thank you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B6E")

    label("loc_4B09")


    ChrTalk(    #303
        0xFE,
        (
            "Estelle, Joshua...we're counting\x01",
            "on you guys!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0xFE,
        "Even if it is just a temporary assignment...\x02",
    )

    CloseMessageWindow()

    label("loc_4B6E")

    Jump("loc_4CD0")

    label("loc_4B71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4CD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4C1C")

    ChrTalk(    #305
        0xFE,
        "Balance or effectiveness.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xFE,
        (
            "Well, whichever is more important\x01",
            "is ultimately up to the individual to\x01",
            "decide, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0xFE,
        "It certainly isn't up to me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4CD0")

    label("loc_4C1C")

    OP_A2(0x8)

    ChrTalk(    #308
        0xFE,
        "Decisions...decisions...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xFE,
        (
            "Do I want a balanced general\x01",
            "use weapon or do I want an\x01",
            "ace-in-the-hole cannon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0xFE,
        (
            "I ought to just buy both and stop\x01",
            "wasting time worrying.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CD0")

    TalkEnd(0xFE)
    Return()

    # Function_20_40BA end

    def Function_21_4CD4(): pass

    label("Function_21_4CD4")

    EventBegin(0x0)
    ClearMapFlags(0x10000000)
    OP_A2(0x58E)
    SetChrPos(0x101, 1750, 0, -4500, 53)
    SetChrPos(0x102, 730, 0, -5190, 44)
    SetChrPos(0x107, 1790, 0, -5680, 57)
    SetChrPos(0x17, 4240, 0, -800, 17)
    OP_4A(0x17, 255)
    OP_4A(0x8, 255)
    OP_6D(2460, 0, -2580, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0x17, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x17, 180, 400)

    ChrTalk(    #311
        0x17,
        "#070FAh, you're back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x101,
        (
            "#501FZin! I didn't know you were\x01",
            "still here!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4DF4():
        OP_6D(3390, 0, -770, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4DF4)

    def lambda_4E0C():
        OP_8E(0xFE, 0xD48, 0x0, 0xFFFFF8F8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4E0C)
    Sleep(300)

    def lambda_4E2C():
        OP_8E(0xFE, 0x1176, 0x0, 0xFFFFF722, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_4E2C)
    Sleep(300)

    def lambda_4E4C():
        OP_8E(0xFE, 0xE10, 0x0, 0xFFFFF3A8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4E4C)

    def lambda_4E67():

        label("loc_4E67")

        TurnDirection(0xFE, 0x17, 0)
        OP_48()
        Jump("loc_4E67")

    QueueWorkItem2(0x101, 1, lambda_4E67)

    def lambda_4E78():

        label("loc_4E78")

        TurnDirection(0xFE, 0x17, 0)
        OP_48()
        Jump("loc_4E78")

    QueueWorkItem2(0x102, 1, lambda_4E78)

    def lambda_4E89():

        label("loc_4E89")

        TurnDirection(0xFE, 0x17, 0)
        OP_48()
        Jump("loc_4E89")

    QueueWorkItem2(0x107, 1, lambda_4E89)
    Sleep(2000)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)

    ChrTalk(    #313
        0x101,
        "#000FThanks for carrying Agate earlier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x102,
        "#010FWe're in your debt.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x17,
        (
            "#071FHa ha. Think nothing of it.\x01",
            "Always glad to help a friend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x8,
        (
            "#790FSo...\x01",
            "How is Agate's condition?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x102,
        "#013FWell...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5143")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #318
        (
            "\x07\x05Joshua relayed what they knew about Agate's current condition and\x01",
            "about Father Vixen.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #319
        0x17,
        (
            "#072FHm... Then he is in greater\x01",
            "danger than I'd imagined.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x8,
        (
            "#792FTraditional church medicine,\x01",
            "then...\x02\x03",

            "It is our only option, I suppose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x101,
        (
            "#002FYeah... So we should try\x01",
            "the chapel.\x02\x03",

            "The longer we wait, the longer\x01",
            "Agate suffers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x102,
        (
            "#012FAll right.\x01",
            "To the Septian Church, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x8,
        "#790FPlease hurry.\x02",
    )

    CloseMessageWindow()
    OP_4B(0x17, 255)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Jump("loc_5214")

    label("loc_5143")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #324
        (
            "\x07\x05Joshua relayed what they knew about Agate's current condition and\x01",
            "about the Zemuria Moss.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #325
        0x17,
        (
            "#072FHm... Then he is in greater\x01",
            "danger than I'd imagined.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Call(0, 22)

    label("loc_5214")

    Return()

    # Function_21_4CD4 end

    def Function_22_5215(): pass

    label("Function_22_5215")

    OP_31(0x7, 0x0, 0x1B)
    OP_B5(0x7, 0x0)
    OP_B5(0x7, 0x1)
    OP_B5(0x7, 0x2)
    OP_B5(0x7, 0x3)
    OP_B5(0x7, 0x4)
    OP_B5(0x7, 0x5)
    OP_41(0x7, 0xD3)
    OP_41(0x7, 0xF5)
    OP_41(0x7, 0x113)
    OP_41(0x7, 0x261, 0x0)
    OP_41(0x7, 0x259, 0x1)
    OP_41(0x7, 0x25E, 0x2)
    OP_41(0x7, 0x274, 0x3)
    OP_35(0x7, 0xDC)
    OP_35(0x7, 0xDD)
    OP_35(0x7, 0xDE)
    OP_35(0x7, 0xDF)
    OP_36(0x7, 0x109)
    AddParty(0x7, 0xFF)
    SetChrFlags(0x17, 0x80)
    SetChrPos(0x101, 3400, 0, -1800, 0)
    SetChrPos(0x102, 3600, 0, -3160, 0)
    SetChrPos(0x107, 4470, 0, -2270, 0)
    SetChrPos(0x108, 4220, 0, -740, 180)
    OP_6D(3390, 0, -770, 1200)

    ChrTalk(    #326
        0x8,
        (
            "#790FIf you need Zemuria Moss...\x01",
            "One moment while I check the\x01",
            "information the church supplied...\x02\x03",

            "#792F...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5339():
        TurnDirection(0xFE, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_5339)
    OP_8C(0x8, 180, 400)

    def lambda_534E():
        OP_6D(3980, 0, 800, 1000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_534E)
    OP_8E(0x8, 0xE10, 0x0, 0x956, 0x5DC, 0x0)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x8)

    ChrTalk(    #327
        0x8,
        (
            "#790FAh, here we are.\x02\x03",

            "It can evidently be found in the northwest\x01",
            "area of the Kaldia Limestone Cave, at the\x01",
            "shore of an underground lake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x101,
        (
            "#002FNorthwest, limestone cave,\x01",
            "underground lake... Got it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x102,
        (
            "#010FYou might as well put it\x01",
            "in the notebook.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #330
        0x8,
        (
            "#790FI've heard it said that the monsters\x01",
            "in that place are quite strong.\x02\x03",

            "The last time the guild dispatched bracers to\x01",
            "gather moss, a team of four veterans was sent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0x101,
        "#004FFuh...Four veterans?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x102,
        (
            "#012FGathering the moss isn't going to be an easy\x01",
            "task, then...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x102, 400)

    ChrTalk(    #333
        0x108,
        "#070F#4PHmm... In that case...\x02",
    )

    CloseMessageWindow()

    def lambda_55DC():
        OP_6D(3390, 0, -770, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_55DC)
    OP_8E(0x8, 0xE88, 0x0, 0x514, 0x5DC, 0x0)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #334
        0x8,
        (
            "#791FAs such, I suggest you take\x01",
            "this gentleman with you.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 0)

    ChrTalk(    #335
        0x108,
        "#075FErk...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x8, 600)

    ChrTalk(    #336
        0x108,
        (
            "#072F#6PHey! Can I please finish\x01",
            "what I was going to say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x8,
        (
            "#792FOh. Do you not wish to\x01",
            "accompany them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x108,
        (
            "#073F#6PNo, I didn't say that...\x02\x03",

            "#075FOh, never mind! You're just as\x01",
            "frustrating to deal with as ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0x8,
        "#791FYou flatter me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0x108,
        "#072F#6PWell, it wasn't intended as flattery!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x107, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #341
        0x101,
        (
            "#506FU-Umm...\x02\x03",

            "Are you going to come with\x01",
            "us, Zin?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x108, 180, 400)

    ChrTalk(    #342
        0x108,
        (
            "#070FYes... That seems to be the\x01",
            "path that destiny indicates.\x02\x03",

            "I'm setting off for Grancel\x01",
            "tomorrow, but I can certainly\x01",
            "accompany you until then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x101,
        (
            "#001FThat's plenty of time!\x01",
            "Thank you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0x102,
        "#010FWe appreciate it.\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x107)
    OP_8C(0x107, 270, 400)

    ChrTalk(    #345
        0x107,
        (
            "#063F#2PU-Umm...\x01",
            "Excuse me...?\x02\x03",

            "I... I don't suppose I could come?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5967():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5967)
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #346
        0x101,
        "#004F#6PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0x107,
        (
            "#561F#2PI know that sometimes I slow\x01",
            "you down...\x02\x03",

            "But...\x02\x03",

            "#069FAgate's hurt because he\x01",
            "protected me...\x02\x03",

            "I feel like I've got to do something\x01",
            "to help...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0x101,
        "#003F#6PTita...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #349
        0x101,
        (
            "#005F#4PHey, Joshua?\x01",
            "What do you say?\x02\x03",

            "Can we take her with us?\x01",
            "Pleeeeease?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0x102,
        (
            "#015FDo I have a choice?\x02\x03",

            "#012FOkay, Tita.\x02\x03",

            "Do you promise to let us take the\x01",
            "lead and not do anything rash?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5B0A():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B0A)

    ChrTalk(    #351
        0x107,
        "#062F#2PI-I promise!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x108, 400)

    ChrTalk(    #352
        0x102,
        (
            "#010FThat's enough for me.\x01",
            "Do you mind, Zin?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x108,
        (
            "#070FIt's fine by me.\x02\x03",

            "#071FGood to have you with us,\x01",
            "little one.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x108, 400)

    ChrTalk(    #354
        0x107,
        "#560FTh-Thank you, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0x101,
        (
            "#006F#6PWell, if that's all settled, then\x01",
            "let's get to that limestone cave!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0x102,
        (
            "#010FFirst, we'll have to take\x01",
            "the Kaldia Tunnel from the\x01",
            "central factory basement.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x552)
    OP_28(0x42, 0x1, 0x20)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_22_5215 end

    def Function_23_5C8A(): pass

    label("Function_23_5C8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_5CA7")
    OP_2A(0x2D, 0x32, 0x2A, 0x28, 0x2B, 0x2C, 0x33, 0x34, 0xFFFF)
    Jump("loc_5D36")

    label("loc_5CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 2)), scpexpr(EXPR_END)), "loc_5CC4")
    OP_2A(0x2D, 0x32, 0x2A, 0x28, 0x2B, 0x2C, 0x33, 0x34, 0xFFFF)
    Jump("loc_5D36")

    label("loc_5CC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_5CDF")
    OP_2A(0x2D, 0x32, 0x2A, 0x28, 0x2B, 0x2C, 0x33, 0xFFFF)
    Jump("loc_5D36")

    label("loc_5CDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_5CFA")
    OP_2A(0x2D, 0x32, 0x2A, 0x28, 0x2B, 0x2C, 0x33, 0xFFFF)
    Jump("loc_5D36")

    label("loc_5CFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_5D15")
    OP_2A(0x2D, 0x32, 0x2A, 0x28, 0x2B, 0x2C, 0x33, 0xFFFF)
    Jump("loc_5D36")

    label("loc_5D15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_5D28")
    OP_2A(0x2D, 0x32, 0x2A, 0xFFFF)
    Jump("loc_5D36")

    label("loc_5D28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5D36")
    OP_2A(0x2D, 0x32, 0xFFFF)

    label("loc_5D36")

    TalkEnd(0xFF)
    Return()

    # Function_23_5C8A end

    SaveToFile()

Try(main)
