from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3105   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3105.x',
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
        'Maintenance Chief Gustav',             # 9
        'Gerald',                               # 10
        'Factory Chief Murdock',                # 11
        'Dorothy',                              # 12
        'Antoine',                              # 13
        'Captain Amalthea',                     # 14
        'Rutherford',                           # 15
        'Dodge',                                # 16
        'Bartholomew',                          # 17
        'Zeiss - Factory Block',                # 18
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
        'ED6_DT07/CH01290 ._CH',             # 00
        'ED6_DT07/CH02440 ._CH',             # 01
        'ED6_DT07/CH02620 ._CH',             # 02
        'ED6_DT07/CH02070 ._CH',             # 03
        'ED6_DT07/CH01700 ._CH',             # 04
        'ED6_DT07/CH02100 ._CH',             # 05
        'ED6_DT07/CH01020 ._CH',             # 06
        'ED6_DT07/CH01140 ._CH',             # 07
        'ED6_DT07/CH01450 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH01290P._CP',             # 00
        'ED6_DT07/CH02440P._CP',             # 01
        'ED6_DT07/CH02620P._CP',             # 02
        'ED6_DT07/CH02070P._CP',             # 03
        'ED6_DT07/CH01700P._CP',             # 04
        'ED6_DT07/CH02100P._CP',             # 05
        'ED6_DT07/CH01020P._CP',             # 06
        'ED6_DT07/CH01140P._CP',             # 07
        'ED6_DT07/CH01450P._CP',             # 08
    )

    DeclNpc(
        X                   = -37000,
        Z                   = -3800,
        Y                   = 145500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -20110,
        Z                   = 8000,
        Y                   = 121830,
        Direction           = 177,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
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
        TalkScenaIndex      = 11,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
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
        TalkScenaIndex      = 13,
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
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -18770,
        Z                   = 8000,
        Y                   = 89560,
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
        TriggerX            = -41010,
        TriggerZ            = 8000,
        TriggerY            = 122500,
        TriggerRange        = 800,
        ActorX              = -41010,
        ActorZ              = 10200,
        ActorY              = 122500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -38900,
        TriggerZ            = 8400,
        TriggerY            = 122040,
        TriggerRange        = 800,
        ActorX              = -38900,
        ActorZ              = 9900,
        ActorY              = 122040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_27A",          # 00, 0
        "Function_1_4DC",          # 01, 1
        "Function_2_4EF",          # 02, 2
        "Function_3_66C",          # 03, 3
        "Function_4_690",          # 04, 4
        "Function_5_6B4",          # 05, 5
        "Function_6_6D8",          # 06, 6
        "Function_7_6FC",          # 07, 7
        "Function_8_F5F",          # 08, 8
        "Function_9_11BA",         # 09, 9
        "Function_10_11F3",        # 0A, 10
        "Function_11_2416",        # 0B, 11
        "Function_12_3275",        # 0C, 12
        "Function_13_35F2",        # 0D, 13
        "Function_14_36DA",        # 0E, 14
        "Function_15_36DF",        # 0F, 15
        "Function_16_3F85",        # 10, 16
        "Function_17_44FA",        # 11, 17
        "Function_18_483A",        # 12, 18
        "Function_19_5929",        # 13, 19
        "Function_20_59E4",        # 14, 20
    )


    def Function_0_27A(): pass

    label("Function_0_27A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_END)), "loc_2B7")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -17880, 8000, 118110, 183)
    OP_43(0xE, 0x0, 0x0, 0x3)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44660, 8000, 129500, 5)
    Jump("loc_4DB")

    label("loc_2B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2F4")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -17880, 8000, 118110, 183)
    OP_43(0xE, 0x0, 0x0, 0x3)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44660, 8000, 129500, 5)
    Jump("loc_4DB")

    label("loc_2F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_314")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44750, -4000, 146070, 81)
    Jump("loc_4DB")

    label("loc_314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_37D")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -47500, -4000, 151780, 261)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -47500, -4000, 152840, 261)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -40130, 8000, 125930, 237)
    OP_43(0xC, 0x0, 0x0, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44750, -4000, 146070, 81)
    Jump("loc_4DB")

    label("loc_37D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_3BD")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -44530, -4000, 142000, 176)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44510, -4000, 140610, 21)
    SetChrFlags(0x10, 0x10)
    Jump("loc_4DB")

    label("loc_3BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3FA")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -58040, 4000, 125930, 187)
    OP_43(0x8, 0x0, 0x0, 0x6)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44750, -4000, 146070, 81)
    Jump("loc_4DB")

    label("loc_3FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_404")
    Jump("loc_4DB")

    label("loc_404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_441")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -49800, 8000, 117400, 3)
    OP_43(0x8, 0x0, 0x0, 0x5)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44750, -4000, 146070, 81)
    Jump("loc_4DB")

    label("loc_441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_461")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44750, -4000, 146070, 81)
    Jump("loc_4DB")

    label("loc_461")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_481")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44750, -4000, 146070, 81)
    Jump("loc_4DB")

    label("loc_481")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_4A1")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44750, -4000, 146070, 81)
    Jump("loc_4DB")

    label("loc_4A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4DB")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -40130, 8000, 125930, 237)
    OP_43(0xC, 0x0, 0x0, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44750, -4000, 146070, 81)

    label("loc_4DB")

    Return()

    # Function_0_27A end

    def Function_1_4DC(): pass

    label("Function_1_4DC")

    OP_16(0x2, 0xFA0, 0xFFFD6020, 0x4E20, 0x30053)
    Return()

    # Function_1_4DC end

    def Function_2_4EF(): pass

    label("Function_2_4EF")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_514")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_656")

    label("loc_514")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52D")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_656")

    label("loc_52D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_546")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_656")

    label("loc_546")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55F")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_656")

    label("loc_55F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_578")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_656")

    label("loc_578")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_591")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_656")

    label("loc_591")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AA")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_656")

    label("loc_5AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C3")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_656")

    label("loc_5C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DC")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_656")

    label("loc_5DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F5")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_656")

    label("loc_5F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60E")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_656")

    label("loc_60E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_627")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_656")

    label("loc_627")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_640")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_656")

    label("loc_640")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_656")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_656")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_66B")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_656")

    label("loc_66B")

    Return()

    # Function_2_4EF end

    def Function_3_66C(): pass

    label("Function_3_66C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_68F")
    OP_8D(0xFE, -19390, 119560, -16690, 116060, 3000)
    Jump("Function_3_66C")

    label("loc_68F")

    Return()

    # Function_3_66C end

    def Function_4_690(): pass

    label("Function_4_690")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6B3")
    OP_8D(0xFE, -35820, 123780, -43940, 129220, 3000)
    Jump("Function_4_690")

    label("loc_6B3")

    Return()

    # Function_4_690 end

    def Function_5_6B4(): pass

    label("Function_5_6B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6D7")
    OP_8D(0xFE, -45240, 117320, -51970, 121500, 3000)
    Jump("Function_5_6B4")

    label("loc_6D7")

    Return()

    # Function_5_6B4 end

    def Function_6_6D8(): pass

    label("Function_6_6D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6FB")
    OP_8D(0xFE, -56420, 122640, -59470, 129340, 3000)
    Jump("Function_6_6D8")

    label("loc_6FB")

    Return()

    # Function_6_6D8 end

    def Function_7_6FC(): pass

    label("Function_7_6FC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_END)), "loc_77F")

    ChrTalk(    #0
        0xFE,
        (
            "*sigh* What is this inspection\x01",
            "without any kind of notice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Those Royal Army guys have\x01",
            "no sense of protocol.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F5B")

    label("loc_77F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_7EB")

    ChrTalk(    #2
        0xFE,
        (
            "Well, the Cecilia will be\x01",
            "landing soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Better get started on all the\x01",
            "docking measures.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F5B")

    label("loc_7EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_8AB")

    ChrTalk(    #4
        0xFE,
        (
            "The factory ship's being\x01",
            "sent out of port.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "I know they're supposed to go\x01",
            "to Leiston, but flying out ahead\x01",
            "of schedule...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "I wonder if something's happened\x01",
            "out there...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F5B")

    label("loc_8AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_8FB")

    ChrTalk(    #7
        0xFE,
        "Okay, we're ready for landing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "May as well check the cargo.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F5B")

    label("loc_8FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_9E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_97D")

    ChrTalk(    #9
        0xFE,
        "Man, that Rehmann is so lucky.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "Since he's a pilot, he gets to\x01",
            "leave early any time he's got\x01",
            "a flight. \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E3")

    label("loc_97D")

    OP_A2(0x5)

    ChrTalk(    #11
        0xFE,
        "So, off to Leiston tomorrow?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "Seems there have been a lot\x01",
            "of flights there recently.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)

    label("loc_9E3")

    Jump("loc_F5B")

    label("loc_9E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_ABB")

    ChrTalk(    #13
        0xFE,
        (
            "That whole thing at the central\x01",
            "factory got worked out, didn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "What? They haven't caught the\x01",
            "guys who did it yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "That's troubling. I hope their\x01",
            "next target won't be the factory\x01",
            "ship!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F5B")

    label("loc_ABB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_D04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_BB3")

    ChrTalk(    #16
        0xFE,
        (
            "Hmph. It's the duke's fault the\x01",
            "royal family's got such a bad\x01",
            "name now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "I remember when the queen's\x01",
            "birthday celebration used to be\x01",
            "peaceful and enjoyable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "That pompous, tubby duke owes\x01",
            "me a quiet festival, damn it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D01")

    label("loc_BB3")

    OP_A2(0x5)

    ChrTalk(    #19
        0xFE,
        (
            "Last vacation I went to those\x01",
            "waterfalls over in Air-Letten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "Some duke from the royal family\x01",
            "was visiting there at the same time,\x01",
            "all incognito-like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "But he still made a gigantic fuss.\x01",
            "What a self-absorbed jerk. He\x01",
            "ruined my vacation!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "I don't think all of the royal\x01",
            "family are like him, of course,\x01",
            "but still...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D01")

    Jump("loc_F5B")

    label("loc_D04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_DB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D34")

    ChrTalk(    #23
        0xFE,
        "Well, time to head home!\x02",
    )

    CloseMessageWindow()
    Jump("loc_DB2")

    label("loc_D34")


    ChrTalk(    #24
        0xFE,
        (
            "What do you think of her?  \x01",
            "Isn't she a beauty?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "This is the crown jewel of\x01",
            "the central factory fleet,\x01",
            "the Leibnitz.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DB2")

    Jump("loc_F5B")

    label("loc_DB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_F17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_E41")

    ChrTalk(    #26
        0xFE,
        (
            "I still haven't heard the reason\x01",
            "for all of the orbments stopping\x01",
            "cold yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "I hope it never happens again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F14")

    label("loc_E41")

    OP_A2(0x5)

    ChrTalk(    #28
        0xFE,
        (
            "All the orbments stopped working\x01",
            "last night, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "It's such a good thing it didn't\x01",
            "happen during the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "I don't want to think what\x01",
            "would've happened if there\x01",
            "had been any ships in the air.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F14")

    Jump("loc_F5B")

    label("loc_F17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F5B")

    ChrTalk(    #31
        0xFE,
        "Docking is a go!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "Time for final liftoff check.\x02",
    )

    CloseMessageWindow()

    label("loc_F5B")

    TalkEnd(0xFE)
    Return()

    # Function_7_6FC end

    def Function_8_F5F(): pass

    label("Function_8_F5F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_FF9")

    ChrTalk(    #33
        0xFE,
        (
            "#690FSorry to keep you waiting.\x02\x03",

            "We've got another work order \x01",
            "from Leiston Fortress. I'd like\x01",
            "to leave today.\x02\x03",

            "I hope nothing happens.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11B6")

    label("loc_FF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_10C0")

    ChrTalk(    #34
        0xFE,
        "#690FTita, you hurt?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x107,
        (
            "#060F...\x02\x03",

            "Huh?\x02\x03",

            "N-No, sir! I'm...I'm fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "#690FSomething wrong? You spaced\x01",
            "out there for a second.\x02\x03",

            "Well, as long as you didn't\x01",
            "get hurt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x107,
        "#060F...\x02",
    )

    CloseMessageWindow()
    Jump("loc_11B6")

    label("loc_10C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_11B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_10F2")

    ChrTalk(    #38
        0xFE,
        "#690FHey, Tita. Be careful!\x02",
    )

    CloseMessageWindow()
    Jump("loc_11B6")

    label("loc_10F2")

    OP_A2(0x4)

    ChrTalk(    #39
        0xFE,
        (
            "#690FHey, Tita.\x02\x03",

            "Helping your grandpa out again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x107,
        (
            "#060FYes, sir.\x02\x03",

            "I've got to go to Elmo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "#690FIs that a fact, now? Well,\x01",
            "be careful out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x107,
        "#060FThank you, sir. Goodbye!\x02",
    )

    CloseMessageWindow()

    label("loc_11B6")

    TalkEnd(0xFE)
    Return()

    # Function_8_F5F end

    def Function_9_11BA(): pass

    label("Function_9_11BA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_11D8")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #43
        0xFE,
        "Nya-o.\x02",
    )

    CloseMessageWindow()
    Jump("loc_11EF")

    label("loc_11D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_11EF")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #44
        0xFE,
        "Nyao?\x02",
    )

    CloseMessageWindow()

    label("loc_11EF")

    TalkEnd(0xFE)
    Return()

    # Function_9_11BA end

    def Function_10_11F3(): pass

    label("Function_10_11F3")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1601")
    OP_A2(0x604)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -20510, 8000, 119230, 0)
    SetChrPos(0x102, -18980, 8000, 119430, 0)

    def lambda_1234():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1234)

    def lambda_1244():
        OP_6B(2750, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1244)
    OP_6D(-20210, 8000, 122050, 2000)

    ChrTalk(    #45
        0x9,
        "Hey, it's you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x9,
        (
            "I told you before, I don't know\x01",
            "when the ship's leaving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x9,
        (
            "If you'd just wait at the\x01",
            "Bracer Guild...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#000FUm, actually? There's been a\x01",
            "slight change in plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x102,
        (
            "#010FI apologize for the timing,\x01",
            "but can we still cancel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x9,
        "Sure, that's no problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x9,
        (
            "As long as it's before your\x01",
            "flight arrives in port there's\x01",
            "no cancellation fee. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x9,
        (
            "We just need to get your\x01",
            "tickets back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        "#000FGreat. Here you go.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #54
        "\x07\x05Returned Boarding Pass x2.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_3F(0x36A, 2)

    ChrTalk(    #55
        0x9,
        "Hey, that's a military patrol vessel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x9,
        "It's here early...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        "#000FWell! Gotta go, bye!\x02",
    )

    CloseMessageWindow()

    def lambda_14BD():
        OP_8E(0xFE, 0xFFFFB12C, 0x1F40, 0x192A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14BD)

    ChrTalk(    #58
        0x102,
        "#010FThank you for your help.\x02",
    )

    CloseMessageWindow()

    def lambda_14FB():
        OP_8E(0xFE, 0xFFFFB7F8, 0x1F40, 0x192A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14FB)

    ChrTalk(    #59
        0x9,
        (
            "No worries. Come back and see\x01",
            "us again sometime!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #60
        0xD,
        (
            "#180FWell, things are certainly\x01",
            "bustling around here.\x02\x03",

            "First, I believe I shall go see\x01",
            "the factory chief.\x02\x03",

            "I have to admire the colonel\x01",
            "for planning all of this.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T3101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2412")

    label("loc_1601")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17BD")
    OP_A2(0x602)
    OP_28(0x54, 0x1, 0x2)
    EventBegin(0x0)
    OP_69(0x9, 0x3E8)

    ChrTalk(    #61
        0x9,
        "Hello there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x9,
        (
            "I heard from Kilika. Shall we\x01",
            "get you all squared away?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        "#000FThat'd be great, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x9,
        (
            "Please fill out these forms with\x01",
            "your names and addresses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x102,
        "#010FThank you.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #66
        "\x07\x05Estelle filled out the boarding papers.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #67
        0x9,
        "Okay, here are your tickets.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x9,
        (
            "Make sure you show these when\x01",
            "you're boarding.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #69
        "\x07\x05Received Boarding Pass x2.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_3E(0x36A, 2)
    EventEnd(0x1)
    Jump("loc_2412")

    label("loc_17BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E0B")
    OP_A2(0x517)
    ClearMapFlags(0x1)
    OP_69(0x9, 0x3E8)

    ChrTalk(    #70
        0x9,
        "Hi, need a flight?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x9,
        (
            "The westbound airship just\x01",
            "departed a few moments ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        (
            "#000FNo, thank you. We don't need\x01",
            "an airship right now.\x02\x03",

            "Actually, we need to talk to...\x01",
            "Gustav, was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        "You mean the maintenance chief?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x9,
        "He's not here at the moment...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        "#000FWhat do you mean, 'not here'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x9,
        (
            "He went to Leiston Fortress two\x01",
            "or three days ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x9,
        (
            "Some kind of repair emergency\x01",
            "on a military patrol ship...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        "#000FLeiston Fortress?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x102,
        (
            "#010FAs in, the largest base in the Royal\x01",
            "Army, out by Lake Valleria?\x02\x03",

            "Up in the north part of Zeiss?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        (
            "#000FWonderful. He won't be coming\x01",
            "back from there any time soon. \x02\x03",

            "So what do we do about the\x01",
            "professor's request?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x9,
        (
            "I don't know anything about that,\x01",
            "but the chief is actually on his\x01",
            "way back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x9,
        "He just sent word to us...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        "#000FOh, hey, airship!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x9,
        "Speak of the devil...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85 op#A op#5
        0x9,
        (
            "#20AHere she comes. The Leibnitz is\x01",
            "on its way into port.\x05\x02",
        )
    )


    ChrTalk(    #86
        0x101,
        (
            "#000FAn orange airship...\x02\x03",

            "Hold the phone. Since when\x01",
            "are public airships orange?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x102,
        (
            "#010FNo, that doesn't look like a\x01",
            "regular public airship.\x02\x03",

            "The shape is wrong and it's\x01",
            "got work arms all over it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        "#000FNow that you mention it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x9,
        (
            "That's a central factory vessel,\x01",
            "the Leibnitz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x9,
        (
            "It's the same model as the\x01",
            "public transports, but it's had\x01",
            "several modifications.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x9,
        (
            "It's used for large scale\x01",
            "maintenance and transport.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        (
            "#000FHuh! A flying factory...\x02\x03",

            "Then, the maintenance chief is\x01",
            "on that airship?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x9,
        "That's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x9,
        (
            "Now's your chance. You need to\x01",
            "talk with him, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        "#000FWe do. Thanks a lot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x102,
        "#010FYes, thank you.\x02",
    )

    CloseMessageWindow()
    OP_69(0x0, 0x3E8)
    SetMapFlags(0x1)
    Jump("loc_2412")

    label("loc_1E0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1E7B")

    ChrTalk(    #97
        0x9,
        (
            "What is it? Your papers are\x01",
            "already finished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x9,
        (
            "Just show your tickets when\x01",
            "you get on-board.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2412")

    label("loc_1E7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1EFA")

    ChrTalk(    #99
        0x9,
        "Hey. Wow, you guys look busy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x9,
        (
            "We've just been ordered to get\x01",
            "our factory ship in the air. It's\x01",
            "a madhouse.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2412")

    label("loc_1EFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1F43")

    ChrTalk(    #101
        0x9,
        "The Cecilia is on schedule...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x9,
        "Time to read the news!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2412")

    label("loc_1F43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_20F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_200A")

    ChrTalk(    #103
        0x9,
        (
            "Did you see the front page of\x01",
            "the Liberl News?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x9,
        (
            "The pictures on their front \x01",
            "page have gotten nicer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x9,
        (
            "I'm looking forward to seeing\x01",
            "what they do with the next \x01",
            "edition.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20F2")

    label("loc_200A")

    OP_A2(0x0)

    ChrTalk(    #106
        0x9,
        (
            "All that mess at the central\x01",
            "factory really made some ink.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x9,
        (
            "I can't believe there are people\x01",
            "who have the guts to attack\x01",
            "the central factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x9,
        (
            "At this rate, the entire city\x01",
            "of Zeiss is going to be on\x01",
            "the front page.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20F2")

    Jump("loc_2412")

    label("loc_20F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_21D6")

    ChrTalk(    #109
        0x9,
        (
            "What, you already read it?\x01",
            "The Liberl News' latest issue?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x9,
        (
            "The mayor of Ruan got arrested.\x01",
            "Turns out he's a total crook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x9,
        (
            "And between sky bandits and\x01",
            "this Dalmore person...what is\x01",
            "this world coming to?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2412")

    label("loc_21D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_21FE")

    ChrTalk(    #112
        0x9,
        "So, did you find Gustav?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2412")

    label("loc_21FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_2361")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2290")

    ChrTalk(    #113
        0x9,
        (
            "Wasn't that whole sky bandit\x01",
            "thing in Bose settled by\x01",
            "bracers, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x9,
        (
            "How lucky we are to have the\x01",
            "Royal Army on duty...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_235E")

    label("loc_2290")

    OP_A2(0x0)

    ChrTalk(    #115
        0x9,
        (
            "I read about it in the Liberl\x01",
            "News, but that sky bandit\x01",
            "thing sure was crazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x9,
        (
            "It's a nightmare for us up here\x01",
            "if the public flights get stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x9,
        (
            "We've got to deal with all\x01",
            "the passengers!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_235E")

    Jump("loc_2412")

    label("loc_2361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2412")

    ChrTalk(    #118
        0x9,
        (
            "The airliner 'Cecilia' is currently\x01",
            "in port, having just arrived from\x01",
            "the west.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x9,
        (
            "All passengers en route to the\x01",
            "Grancel region, please proceed\x01",
            "to the gates.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2412")

    TalkEnd(0x9)
    Return()

    # Function_10_11F3 end

    def Function_11_2416(): pass

    label("Function_11_2416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_260B")
    EventBegin(0x0)

    ChrTalk(    #120
        0x8,
        "#690FReady for liftoff?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Liftoff]\x01",      # 0
            "[Prepare]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_24A6"),
        (1, "loc_25CD"),
        (SWITCH_DEFAULT, "loc_2608"),
    )


    label("loc_24A6")

    OP_A2(0x561)
    OP_28(0x43, 0x1, 0x400)
    OP_28(0x44, 0x4, 0x2)
    OP_28(0x44, 0x4, 0x4)

    ChrTalk(    #121
        0x8,
        (
            "#690FAll right! Let's load up!\x02\x03",

            "We're off to Leiston Fortress!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xA,
        (
            "#800FPlease...bring Professor Russell\x01",
            "back home safely.\x02\x03",

            "And...take care of Tita.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_255A():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_255A)

    def lambda_2568():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2568)

    def lambda_2576():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2576)
    TurnDirection(0x107, 0xA, 400)

    ChrTalk(    #123
        0x107,
        "#060FS-Sir...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x101,
        "#000FNo sweat!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x102,
        "#010FLet's go, then.\x02",
    )

    CloseMessageWindow()
    Call(0, 17)
    Jump("loc_2608")

    label("loc_25CD")

    OP_A2(0x572)

    ChrTalk(    #126
        0x8,
        (
            "#690FGot'cha. Let me know when\x01",
            "you're ready.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    label("loc_2608")

    Jump("loc_3274")

    label("loc_260B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3122")
    EventBegin(0x0)
    SetChrPos(0x101, -46160, -4000, 141480, 90)
    SetChrPos(0x106, -44780, -4000, 140260, 0)
    SetChrPos(0x107, -45700, -4000, 140390, 45)
    SetChrPos(0x102, -45780, -4000, 142250, 135)
    Fade(1000)

    def lambda_2668():
        OP_6C(45000, 0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2668)
    OP_6D(-45150, -4000, 141460, 0)

    ChrTalk(    #127
        0xA,
        (
            "#800FI've been waiting for you.\x01",
            "Is everybody ready?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x106,
        "#050FYeah, we can go any time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x107,
        "#060FIs the Leibnitz ready, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xA,
        (
            "#800FYeah, you were lucky that\x01",
            "last-minute military order\x01",
            "came through like that.\x02\x03",

            "We were just about to head\x01",
            "out to Leiston Fortress.\x02\x03",

            "We can take off any time.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    Sleep(500)
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(    #131
        0x101,
        (
            "#000FAny time?\x02\x03",

            "Won't it be hard to leave without,\x01",
            "you know, the ship?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 315, 400)
    Sleep(200)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    OP_8E(0x102, 0xFFFF467E, 0xFFFFF060, 0x230F0, 0x7D0, 0x0)

    ChrTalk(    #132
        0x102,
        "#010FEstelle, look down.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    def lambda_287F():
        OP_8E(0x101, 0xFFFF4688, 0xFFFFF060, 0x22CE0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_287F)

    def lambda_289A():
        OP_6C(314000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_289A)
    OP_6D(-49360, -4000, 145960, 2000)

    ChrTalk(    #133
        0x101,
        (
            "#000F...Oh.\x02\x03",

            "Do we have to, um, jump?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x107,
        "#060F*giggle* No, we don't.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #135
        0x101,
        "#000FWha-...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_2937():

        label("loc_2937")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_2937")

    QueueWorkItem2(0xA, 2, lambda_2937)

    def lambda_2948():

        label("loc_2948")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_2948")

    QueueWorkItem2(0x107, 2, lambda_2948)

    def lambda_2959():

        label("loc_2959")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_2959")

    QueueWorkItem2(0x106, 2, lambda_2959)
    Sleep(1000)
    OP_8C(0x101, 315, 400)

    ChrTalk(    #136
        0x101,
        "#000FWhat the...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x102,
        (
            "#010FWhat's happening to the\x01",
            "flight deck?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x106,
        (
            "#050FWhat, didn't you know?\x02\x03",

            "This place's got enough secrets\x01",
            "built into it to blow your mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        "#000FTo be honest, Agate...\x02",
    )

    CloseMessageWindow()

    def lambda_2A42():
        OP_8E(0x101, 0xFFFF4688, 0xFFFFF060, 0x22CE0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2A42)

    def lambda_2A5D():
        OP_6C(314000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A5D)
    OP_6D(-49360, -4000, 145960, 2000)
    OP_6F(0x0, 500)
    OP_70(0x0, 0x4B0)

    def lambda_2A8C():
        OP_6C(339000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A8C)
    OP_6D(-55390, -4000, 147110, 1500)

    def lambda_2AAD():
        OP_6B(2200, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2AAD)
    OP_67(0, 21600, -10000, 2000)

    def lambda_2ACE():
        OP_6B(3500, 3100)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2ACE)

    def lambda_2ADE():
        OP_6C(27000, 3100)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2ADE)
    OP_6D(-36640, -4000, 148800, 3100)
    SetChrPos(0x101, -46240, -4000, 141000, 90)
    SetChrPos(0x102, -46280, -4000, 142120, 90)

    def lambda_2B21():
        OP_6B(5500, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2B21)

    def lambda_2B31():
        OP_67(0, 11000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B31)
    OP_6C(90000, 5000)
    OP_73(0x0)
    Sleep(1000)

    def lambda_2B5A():
        OP_6B(3500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B5A)
    OP_6D(-45210, -4000, 142090, 2000)

    ChrTalk(    #140
        0x101,
        (
            "#000FI don't know how much more\x01",
            "mind I have left to blow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x102,
        (
            "#010FYou probably have more left\x01",
            "than I do, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xA,
        "#800FAnd all of this? It's all...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x101,
        (
            "#000FI know. It's all Professor Russell's\x01",
            "handiwork, right?\x02\x03",

            "Tita, your grandfather is\x01",
            "something else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x107,
        "#060FHehe, I couldn't agree more.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -36460, -4000, 144380, 270)

    ChrTalk(    #145
        0x8,
        "#690FThanks for waiting, guys!\x02",
    )

    CloseMessageWindow()
    OP_6D(-40270, -4000, 143040, 1000)

    ChrTalk(    #146
        0x107,
        "#060FS-Sir!\x02",
    )

    CloseMessageWindow()

    def lambda_2D0F():

        label("loc_2D0F")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2D0F")

    QueueWorkItem2(0xA, 2, lambda_2D0F)

    def lambda_2D20():

        label("loc_2D20")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2D20")

    QueueWorkItem2(0x102, 2, lambda_2D20)

    def lambda_2D31():

        label("loc_2D31")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2D31")

    QueueWorkItem2(0x101, 2, lambda_2D31)

    def lambda_2D42():

        label("loc_2D42")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2D42")

    QueueWorkItem2(0x107, 2, lambda_2D42)

    def lambda_2D53():

        label("loc_2D53")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2D53")

    QueueWorkItem2(0x106, 2, lambda_2D53)

    def lambda_2D64():
        OP_6D(-44110, -3800, 143890, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D64)

    def lambda_2D7C():
        OP_8E(0xFE, 0xFFFF4C0A, 0xFFFFF060, 0x2385C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_2D7C)

    def lambda_2D97():
        OP_8E(0xFE, 0xFFFF4A8E, 0xFFFFF060, 0x2341A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2D97)
    Sleep(100)

    def lambda_2DB7():
        OP_8E(0xFE, 0xFFFF4AFC, 0xFFFFF060, 0x23082, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_2DB7)
    Sleep(100)

    def lambda_2DD7():
        OP_8E(0xFE, 0xFFFF4B56, 0xFFFFF060, 0x22CFE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 3, lambda_2DD7)
    OP_8E(0x8, 0xFFFF57A4, 0xFFFFF128, 0x2329E, 0x7D0, 0x0)

    ChrTalk(    #147
        0x8,
        (
            "#690FHowdy, Tita. I already heard\x01",
            "everything from Murdock. \x02\x03",

            "Hard to believe what happened\x01",
            "to the professor.\x02\x03",

            "Guess it's up to us to help\x01",
            "him out of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x107,
        "#060FTh-Thank you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x106,
        "#050FYeah, we owe you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x8,
        (
            "#690FNot at all. I'm the one who\x01",
            "owes Professor Russell.\x02\x03",

            "Okie dokie. We're ready.\x02\x03",

            "Are we ready to liftoff?\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x107, 0xFF)
    OP_44(0x106, 0xFF)
    OP_44(0xA, 0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Liftoff]\x01",      # 0
            "[Prepare]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2FBD"),
        (1, "loc_30E4"),
        (SWITCH_DEFAULT, "loc_311F"),
    )


    label("loc_2FBD")

    OP_A2(0x561)
    OP_28(0x43, 0x1, 0x400)
    OP_28(0x44, 0x4, 0x2)
    OP_28(0x44, 0x4, 0x4)

    ChrTalk(    #151
        0x8,
        (
            "#690FAll right! Let's load up!\x02\x03",

            "We're off to Leiston Fortress!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xA,
        (
            "#800FPlease...bring Professor Russell\x01",
            "back home safely.\x02\x03",

            "And...take care of Tita.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3071():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3071)

    def lambda_307F():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_307F)

    def lambda_308D():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_308D)
    TurnDirection(0x107, 0xA, 400)

    ChrTalk(    #153
        0x107,
        "#060FS-Sir...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x101,
        "#000FNo sweat!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x102,
        "#010FLet's go, then.\x02",
    )

    CloseMessageWindow()
    Call(0, 17)
    Jump("loc_311F")

    label("loc_30E4")

    OP_A2(0x572)

    ChrTalk(    #156
        0x8,
        (
            "#690FGot'cha. Let me know when\x01",
            "you're ready.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    label("loc_311F")

    Jump("loc_3274")

    label("loc_3122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_319C")

    ChrTalk(    #157
        0xA,
        (
            "#800FGustav just finished all our\x01",
            "takeoff preparations.\x02\x03",

            "When you're ready to leave,\x01",
            "come back and see me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3274")

    label("loc_319C")

    OP_A2(0x3)

    ChrTalk(    #158
        0xA,
        "#800FHi. Are you ready yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x102,
        (
            "#010FWe still need a little more\x01",
            "time to finish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xA,
        (
            "#800FOkay well, Gustav just finished\x01",
            "all of our takeoff preparations.\x02\x03",

            "When you're ready to leave,\x01",
            "come back and see me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3274")

    Return()

    # Function_11_2416 end

    def Function_12_3275(): pass

    label("Function_12_3275")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_END)), "loc_3354")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_32DD")

    ChrTalk(    #161
        0xFE,
        (
            "Are all of the airships\x01",
            "running late?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "I might as well come back\x01",
            "later on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3351")

    label("loc_32DD")

    OP_A2(0x1)

    ChrTalk(    #163
        0xFE,
        (
            "Looks like all the airships are\x01",
            "running late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "Those military inspections sure\x01",
            "are slowing things down.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3351")

    Jump("loc_35EE")

    label("loc_3354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3458")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_338D")

    ChrTalk(    #165
        0xFE,
        "Or is it that I'm just here early?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3455")

    label("loc_338D")

    OP_A2(0x1)

    ChrTalk(    #166
        0xFE,
        (
            "Hi there! Are you all off to the\x01",
            "capital, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "I was just on my way to work\x01",
            "at the airship company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "If I finish fast enough, I was\x01",
            "thinking I'd go to the Royal\x01",
            "Birthday Celebration.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3455")

    Jump("loc_35EE")

    label("loc_3458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_35EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_34F2")

    ChrTalk(    #169
        0xFE,
        (
            "Airship engineering has\x01",
            "really advanced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "I imagine it won't be long before\x01",
            "we've got ships going out to even\x01",
            "Dodge's hometown.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EE")

    label("loc_34F2")

    OP_A2(0x1)

    ChrTalk(    #171
        0xFE,
        (
            "This morning I met a Republican\x01",
            "orbment merchant named Dodge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "He asked to see the landing pad,\x01",
            "and now I've been roped into\x01",
            "showing him around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "Over there, Dodge, is the port\x01",
            "for raw materials and the \x01",
            "construction bay's just down...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35EE")

    TalkEnd(0xFE)
    Return()

    # Function_12_3275 end

    def Function_13_35F2(): pass

    label("Function_13_35F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_36D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_367E")

    ChrTalk(    #174
        0xFE,
        (
            "One day I'd like to deal in\x01",
            "the airship business...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "But my hometown would need\x01",
            "to build a landing port first.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36D6")

    label("loc_367E")

    OP_A2(0x2)

    ChrTalk(    #176
        0xFE,
        (
            "I can't think of the words to\x01",
            "describe this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        "It's just...incredible.\x02",
    )

    CloseMessageWindow()

    label("loc_36D6")

    TalkEnd(0xFE)
    Return()

    # Function_13_35F2 end

    def Function_14_36DA(): pass

    label("Function_14_36DA")

    Call(0, 10)
    Return()

    # Function_14_36DA end

    def Function_15_36DF(): pass

    label("Function_15_36DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F84")
    OP_A2(0x518)
    OP_28(0x3F, 0x1, 0x800)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x3F, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_3705")
    OP_28(0x3F, 0x1, 0x2000)

    label("loc_3705")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)

    NpcTalk(    #178
        0x8,
        "Old Technician",
        "Hmm...? What do you want?\x02",
    )

    CloseMessageWindow()
    OP_6D(-42300, -3800, 143800, 1000)

    ChrTalk(    #179
        0x101,
        "#000FUm...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #180
        0x8,
        "Old Technician",
        (
            "The Leibnitz is for authorized\x01",
            "personnel only.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #181
        0x8,
        "Old Technician",
        "Sorry, but I need you to leave.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x101,
        (
            "#000FHeh heh... Actually, we\x01",
            "have authorization, at\x01",
            "least temporarily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x102,
        (
            "#010FWe heard there was a maintenance\x01",
            "chief by the name of Gustav\x01",
            "on board...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #184
        0x8,
        "Old Technician",
        "What do you want with me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x101,
        "#000FOh! Well, that's convenient.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #186
        (
            "\x07\x05Estelle explained that Professor Russell had asked them to find and borrow\x01",
            "a combustion engine.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #187
        0x8,
        (
            "#690FAhh, you're running errands\x01",
            "for Russell, are you?\x02\x03",

            "But a combustion engine, huh...?\x01",
            "Well, you've got good timing.\x01",
            "I'll give you that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x101,
        "#000FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x8,
        "#690FHang on a second...\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x8, -42300, -3800, 143800, 0)

    ChrTalk(    #190
        0x101,
        "#000FI wonder what he's doing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x102,
        "#010FIndeed.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    OP_6D(-43500, -3800, 143700, 1000)

    ChrTalk(    #192
        0x8,
        (
            "#690FHere you go. It's a heavy\x01",
            "beast, though, so be careful.\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x8, 0x0, 0x2BC, 0xBB8, 0x0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #193
        "\x07\x05Received Combustion Engine.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_8F(0x8, 0xFFFF5AC4, 0xFFFFF128, 0x231B8, 0xBB8, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BDD")

    ChrTalk(    #194
        0x101,
        (
            "#000FYow... You weren't kidding.\x02\x03",

            "But we can still manage\x01",
            "to carry it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x8,
        (
            "#690FHeh! You've got some spirit to\x01",
            "you, for such a young girl.\x02\x03",

            "Ha ha ha! I like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x101,
        (
            "#000FHa ha...\x01",
            "It's no big deal.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CA1")

    label("loc_3BDD")


    ChrTalk(    #197
        0x102,
        (
            "#010FIt's really heavy...but we\x01",
            "have to deal with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x8,
        (
            "#690FHeh! I'd have never expected\x01",
            "that kind of spirit out of\x01",
            "today's youth.\x02\x03",

            "Ha ha ha! I like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x102,
        "#010FIt's nothing special...\x02",
    )

    CloseMessageWindow()

    label("loc_3CA1")


    ChrTalk(    #200
        0x8,
        (
            "#690FIt's a pretty interesting\x01",
            "little coincidence...\x02\x03",

            "That old fart wants this thing\x01",
            "right after I got it back from\x01",
            "the military.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x101,
        "#000FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x102,
        "#010FFrom the military...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x8,
        (
            "#690FYeah... This thing was on loan\x01",
            "to them for a little while.\x02\x03",

            "They were using it for some\x01",
            "kind of research.\x02\x03",

            "As a matter of fact, I only\x01",
            "just got it back today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x101,
        (
            "#000FHuh...\x01",
            "Lucky for us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x102,
        "#010F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x101,
        "#000FWhat's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x102,
        "#010FOh...it's nothing.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 1)), scpexpr(EXPR_END)), "loc_3EC3")

    ChrTalk(    #208
        0x102,
        (
            "#010FNow that we've got what we\x01",
            "need, why don't we take it\x01",
            "back to the professor?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F0E")

    label("loc_3EC3")


    ChrTalk(    #209
        0x102,
        (
            "#010FNow we need gasoline.\x01",
            "Let's check down in the\x01",
            "basement workshop.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F0E")


    ChrTalk(    #210
        0x101,
        (
            "#000FSure thing.\x02\x03",

            "Thank you, Mr. Maintenance Chief!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x8,
        (
            "#690FSure, sure. Give my regards\x01",
            "to the old man.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x80)
    EventEnd(0x0)

    label("loc_3F84")

    Return()

    # Function_15_36DF end

    def Function_16_3F85(): pass

    label("Function_16_3F85")

    EventBegin(0x0)
    SetChrPos(0x108, -45670, -4000, 146000, 0)
    SetChrPos(0x101, -46540, -4000, 147540, 0)
    SetChrPos(0x102, -47220, -4000, 146840, 0)
    SetChrPos(0x107, -47150, -4000, 145610, 0)
    TurnDirection(0x101, 0x108, 0)
    TurnDirection(0x102, 0x108, 0)
    TurnDirection(0x107, 0x108, 0)
    TurnDirection(0x108, 0x102, 0)
    OP_6D(-45760, -4000, 146000, 0)
    OP_67(0, 9090, -10000, 0)
    OP_6B(2650, 0)
    OP_6C(111000, 0)
    OP_6E(262, 0)
    OP_A2(0x559)

    ChrTalk(    #212
        0x108,
        (
            "#070FI am truly sorry for having\x01",
            "to bid you farewell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x101,
        (
            "#000FHey, it's okay. We really\x01",
            "appreciate all your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x102,
        (
            "#010FAre you taking this ship\x01",
            "directly to Grancel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x108,
        (
            "#070FYes...\x01",
            "There is much I must do.\x02\x03",

            "If I weren't expected there, I would\x01",
            "gladly remain, and do my part to help\x01",
            "resolve this kidnapping incident.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x107, 400)

    ChrTalk(    #216
        0x108,
        "#070FForgive me, little one.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x107,
        (
            "#060FD-Don't be silly...\x01",
            "You've done a lot for us.\x02\x03",

            "Thank you so much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x108,
        (
            "#070FHa ha... And I appreciate\x01",
            "you saying so.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #219
        (
            "\x07\x00The express flight to Grancel aboard\x01",
            "the Cecilia will be departing shortly.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #220
        (
            "\x07\x00All passengers please go\x01",
            "to the departure gate.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #221
        0x108,
        (
            "#070FOops...\x01",
            "Time to make my exit.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_42D0():
        OP_6D(-40990, -4000, 146200, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_42D0)

    def lambda_42E8():
        OP_6B(3360, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_42E8)

    def lambda_42F8():
        OP_6C(32000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_42F8)
    SetChrFlags(0x108, 0x4)
    OP_8E(0x108, 0xFFFF4BEC, 0xFFFFF060, 0x23780, 0xBB8, 0x0)
    OP_8E(0x108, 0xFFFF4C6E, 0xFFFFF060, 0x232B2, 0xBB8, 0x0)

    def lambda_4335():
        OP_8E(0xFE, 0xFFFF50B0, 0xFFFFF060, 0x23A50, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4335)

    def lambda_4350():
        OP_8E(0xFE, 0xFFFF4BD8, 0xFFFFF060, 0x23898, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4350)

    def lambda_436B():
        OP_8E(0xFE, 0xFFFF4BF6, 0xFFFFF060, 0x23532, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_436B)
    OP_8E(0x108, 0xFFFF720C, 0xFFFFF060, 0x236C2, 0xBB8, 0x0)
    TurnDirection(0x108, 0x107, 400)

    ChrTalk(    #222
        0x108,
        (
            "#070FTake care... Hopefully, we will\x01",
            "meet again, fate willing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x101,
        (
            "#000FYou bet'cha!\x02\x03",

            "Oh... How long are you\x01",
            "going to be in Liberl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x108,
        (
            "#070FI couldn't say for certain...\x01",
            "but probably until the queen's\x01",
            "birthday celebration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x101,
        "#000FMaybe we'll see you there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x102,
        "#010FUntil then, take care.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x108,
        "#070FSame to you.\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    RemoveParty(0x7, 0xFF)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T3101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_3F85 end

    def Function_17_44FA(): pass

    label("Function_17_44FA")

    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x107, 0x80)
    SetChrFlags(0x106, 0x80)
    SetChrFlags(0x8, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x107, 0xFF)
    OP_44(0x106, 0xFF)
    OP_44(0xA, 0xFF)
    SetChrPos(0xB, -45980, 0, 129680, 0)
    ClearChrFlags(0xB, 0x80)
    Fade(1000)
    OP_6D(-40270, -4000, 145060, 0)
    OP_67(0, 11000, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(89000, 0)
    OP_6E(262, 0)

    ChrTalk(    #228
        0xA,
        "#800FI'll be counting on you, bracers...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xB,
        "Hey, wait!\x02",
    )

    CloseMessageWindow()

    def lambda_45C3():
        OP_6D(-45610, -3800, 142980, 2000)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_45C3)

    def lambda_45DB():

        label("loc_45DB")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_45DB")

    QueueWorkItem2(0xA, 1, lambda_45DB)
    OP_8E(0xB, 0xFFFF4A52, 0xFFFFF060, 0x23348, 0x1388, 0x0)

    ChrTalk(    #230
        0xB,
        (
            "#150F*huff* *huff*\x02\x03",

            "Whoa...head rush...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xA,
        "#800FHmm? Dorothy?\x02",
    )

    CloseMessageWindow()
    OP_44(0xA, 0xFF)
    OP_8E(0xA, 0xFFFF4A2A, 0xFFFFF060, 0x22AC4, 0x7D0, 0x0)
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xB, 0xA, 400)

    ChrTalk(    #232
        0xB,
        (
            "#150FOh! Chief!\x02\x03",

            "Were Estelle and crew aboard\x01",
            "that last ship?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xA,
        (
            "#800FThat's right...\x01",
            "How did you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xB,
        (
            "#150FThe guild tipped me.\x02\x03",

            "And there's biiiig trouble brewing, if what\x01",
            "my editors told me rings true. I wanted to\x01",
            "let them know before they left...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xA,
        "#800FWhat kind of trouble...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xB,
        (
            "#150FWeeeeeell... This is totally\x01",
            "off the record...\x02\x03",

            "...but it looks like members\x01",
            "of the Royal Guardsmen were\x01",
            "arrested for treason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xA,
        "#800FWh-What?!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/E0012   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_44FA end

    def Function_18_483A(): pass

    label("Function_18_483A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5928")
    EventBegin(0x0)
    OP_A2(0x603)
    OP_28(0x54, 0x1, 0x4)
    OP_28(0x54, 0x1, 0x8)
    SetChrPos(0xC, -46060, 0, 127820, 0)
    ClearChrFlags(0xC, 0x80)

    ChrTalk(    #238
        0xC,
        "Nya-go.\x02",
    )

    CloseMessageWindow()

    def lambda_4880():
        OP_6D(-46010, -1000, 131740, 2500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4880)

    def lambda_4898():
        OP_67(0, 7390, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4898)

    def lambda_48B0():
        OP_6B(3700, 4000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_48B0)

    def lambda_48C0():
        OP_6C(158000, 4000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_48C0)
    Sleep(3000)
    SetChrPos(0x101, -45400, -4000, 140210, 0)
    SetChrPos(0x102, -46510, -4000, 139810, 0)

    def lambda_48F7():

        label("loc_48F7")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_48F7")

    QueueWorkItem2(0x101, 3, lambda_48F7)

    def lambda_4908():

        label("loc_4908")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_4908")

    QueueWorkItem2(0x102, 3, lambda_4908)

    def lambda_4919():
        OP_8E(0xFE, 0xFFFF4D18, 0xFFFFF060, 0x21D40, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_4919)

    def lambda_4934():
        OP_6D(-45610, -4000, 139000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4934)
    Sleep(3000)

    ChrTalk(    #239
        0x101,
        (
            "#000FHey...\x01",
            "Wasn't this the cat...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x102,
        (
            "#010FYep, he's the one who sneaked\x01",
            "into that shipping container.\x02\x03",

            "His name's Antoine, if\x01",
            "I remember correctly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xC,
        "Nyao-n...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x101,
        (
            "#000FHa ha ha! Awwww...\x02\x03",

            "You scared me half to death!\x02\x03",

            "I hope you take some time \x01",
            "to think about why what\x01",
            "you did was wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xC,
        "Myaon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x101,
        "#000FNope, not listening.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x102,
        (
            "#010FHa ha...\x01",
            "I think he's playing dumb.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x8, -47160, 0, 129750, 0)
    ClearChrFlags(0x8, 0x80)

    ChrTalk(    #246
        0x8,
        "Hey! There you are!\x02",
    )

    CloseMessageWindow()

    def lambda_4B06():
        OP_6D(-46010, -4000, 137720, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4B06)

    def lambda_4B1E():

        label("loc_4B1E")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_4B1E")

    QueueWorkItem2(0x101, 3, lambda_4B1E)

    def lambda_4B2F():

        label("loc_4B2F")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_4B2F")

    QueueWorkItem2(0x102, 3, lambda_4B2F)

    def lambda_4B40():
        OP_8E(0xFE, 0xFFFF4ADE, 0xFFFFF060, 0x21AD4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4B40)
    Sleep(1000)

    def lambda_4B60():

        label("loc_4B60")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_4B60")

    QueueWorkItem2(0x101, 3, lambda_4B60)

    def lambda_4B71():

        label("loc_4B71")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_4B71")

    QueueWorkItem2(0x102, 3, lambda_4B71)

    def lambda_4B82():
        OP_8E(0xFE, 0xFFFF4D4A, 0x0, 0x1F521, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4B82)
    WaitChrThread(0x8, 0x1)

    ChrTalk(    #247
        0x101,
        "#000FHi, Gustav!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x8,
        (
            "#690FThe factory chief told me that\x01",
            "the rescue went off without a\x01",
            "hitch.\x02\x03",

            "The professor's always been a mentor\x01",
            "of sorts to all the engineers...\x02\x03",

            "So I just wanted to say thanks\x01",
            "on behalf of everyone here.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_8E(0x101, 0xFFFF4F20, 0xFFFFF060, 0x21E58, 0x7D0, 0x0)
    TurnDirection(0x101, 0xC, 400)

    ChrTalk(    #249
        0x101,
        (
            "#000FHa ha... Well, we couldn't have\x01",
            "pulled it off without you and\x01",
            "your crew's help.\x02\x03",

            "Tita was so surprised that\x01",
            "I thought her eyes might\x01",
            "pop out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x102,
        "#010FSo that really WAS on purpose?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x8,
        (
            "#690FHa ha ha! Well, to fool the\x01",
            "enemy, sometimes you have\x01",
            "to fool your allies first.\x02\x03",

            "So...what business do\x01",
            "you have at the gate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x101,
        (
            "#000FThe professor asked us to\x01",
            "go to Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x102,
        (
            "#010FWe're a little early for\x01",
            "the eleven o'clock flight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x8,
        (
            "#690FYeah... Well, it also looks\x01",
            "to be a little late.\x02\x03",

            "There's still time to drop off\x01",
            "your bags, so I think you can\x01",
            "take it easy in town for a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x101,
        (
            "#000FHmmm...\x01",
            "That sounds like fun.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x9, -47640, 0, 129250, 0)

    ChrTalk(    #256
        0x9,
        "Hey, you two!\x02",
    )

    CloseMessageWindow()

    def lambda_4F4B():
        OP_8E(0x9, 0xFFFF4EF8, 0xFFFFF15A, 0x2189A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4F4B)

    def lambda_4F66():
        OP_6D(-46700, -2500, 134910, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4F66)

    def lambda_4F7E():

        label("loc_4F7E")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_4F7E")

    QueueWorkItem2(0x101, 2, lambda_4F7E)

    def lambda_4F8F():

        label("loc_4F8F")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_4F8F")

    QueueWorkItem2(0x102, 2, lambda_4F8F)

    def lambda_4FA0():

        label("loc_4FA0")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_4FA0")

    QueueWorkItem2(0x8, 2, lambda_4FA0)
    Sleep(1500)

    def lambda_4FB6():

        label("loc_4FB6")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_4FB6")

    QueueWorkItem2(0x101, 2, lambda_4FB6)

    def lambda_4FC7():

        label("loc_4FC7")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_4FC7")

    QueueWorkItem2(0x102, 2, lambda_4FC7)

    def lambda_4FD8():

        label("loc_4FD8")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_4FD8")

    QueueWorkItem2(0x8, 2, lambda_4FD8)

    def lambda_4FE9():
        OP_6D(-46010, -4000, 137720, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4FE9)
    WaitChrThread(0x9, 0x1)
    TurnDirection(0x9, 0x102, 0)

    ChrTalk(    #257
        0x8,
        (
            "#690FWell, if it ain't Gerald.\x02\x03",

            "What's got you in such a panic?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #258
        0x9,
        "Perfect. You're all here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x9,
        (
            "To be honest, we've had\x01",
            "some trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x8,
        "#690FWhat kind of trouble?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x9,
        (
            "Well, we received a communique\x01",
            "from the airship corporation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x9,
        (
            "It looks like the ship will be\x01",
            "arriving a few hours late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x101,
        "#000FWha...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x102,
        "#010F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x8,
        (
            "#690FOkay, just what's going on here?\x02\x03",

            "More sky bandit trouble?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x9,
        "Well, something like that anyway.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x9,
        (
            "Seems to me that the terrorists\x01",
            "staged an ambush, to disrupt\x01",
            "the queen's birthday celebration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x9,
        (
            "All ships are grounded at port\x01",
            "while the military conducts\x01",
            "inspections.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x101,
        "#000F(Th-That would mean...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x102,
        (
            "#010F(They're probably looking\x01",
            "for the professor's group...)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #271
        0x9,
        (
            "Which means that the ship\x01",
            "that's bound for Grancel\x01",
            "is being held up in Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x9,
        (
            "Apparently, a military guard\x01",
            "ship is coming here from\x01",
            "Leiston Fortress, instead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x8,
        (
            "#690FAhh, I get it.\x02\x03",

            "But if that's the case, you're\x01",
            "going to be extremely busy\x01",
            "soon, aren't you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #274
        0x9,
        (
            "No kidding. I've got to explain\x01",
            "the situation to the customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x9,
        (
            "Which means that you two have\x01",
            "a good chunk of time to kill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x9,
        (
            "Just thought of something... If you\x01",
            "want to wait at the Bracer Guild,\x01",
            "I can get in touch with you there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x101,
        "#000FO-Okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x102,
        "#010FThank you very much.\x02",
    )

    CloseMessageWindow()
    OP_8E(0x9, 0xFFFF46F6, 0x0, 0x1F8E2, 0xBB8, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    SetChrPos(0x9, -18300, 8000, 121700, 180)

    ChrTalk(    #279
        0x8,
        (
            "#690F...Well, this stinks like\x01",
            "last year's diapers.\x02\x03",

            "If the military's coming here,\x01",
            "I know they'll want to check\x01",
            "out the Leibnitz.\x02\x03",

            "I'd better have a talk\x01",
            "with the factory chief.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5614():

        label("loc_5614")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_5614")

    QueueWorkItem2(0x101, 2, lambda_5614)

    def lambda_5625():

        label("loc_5625")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_5625")

    QueueWorkItem2(0x102, 2, lambda_5625)

    ChrTalk(    #280
        0x101,
        (
            "#000FYeah, if they check up on\x01",
            "what happened yesterday,\x01",
            "that won't be good.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5687():

        label("loc_5687")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_5687")

    QueueWorkItem2(0x8, 2, lambda_5687)

    ChrTalk(    #281
        0x102,
        "#010FBe careful, whatever you do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x8,
        (
            "#690FHa ha... I ain't so senile that\x01",
            "I need a couple of punk kids\x01",
            "to tell ME to be careful.\x02\x03",

            "Take it easy, you two.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    OP_8E(0x8, 0xFFFF46F6, 0x0, 0x1F8E2, 0xBB8, 0x0)
    SetChrFlags(0x8, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #283
        0x101,
        (
            "#000FJoshua...?\x01",
            "This doesn't look so hot.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #284
        0x102,
        (
            "#010FYeah... This could put\x01",
            "the airliner in danger.\x02\x03",

            "We've got time, so maybe we\x01",
            "should take the highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x101,
        (
            "#000FAw, man... And it's been so\x01",
            "long since I last got to ride\x01",
            "on an airship, too.\x02\x03",

            "This is all your fault,\x01",
            "Colonel Richard!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x102,
        (
            "#010FWell, try to look at it as\x01",
            "an ongoing opportunity to\x01",
            "advance your training.\x02\x03",

            "So I guess we need to\x01",
            "cancel our reservations\x01",
            "at the reception desk.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xC, 0x80)
    EventEnd(0x0)

    label("loc_5928")

    Return()

    # Function_18_483A end

    def Function_19_5929(): pass

    label("Function_19_5929")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #287
        (
            "\x07\x05Airship Arrivals & Departures\x01",
            "⇒ To Grancel\x01",
            "⇒ To Ruan\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #288
        (
            "\x07\x05※Dangerous/combustible objects prohibited.\x01",
            "　　　　《Liberl Orbalship Co.》\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_19_5929 end

    def Function_20_59E4(): pass

    label("Function_20_59E4")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #289
        (
            "\x07\x05Traffic Control Tower\x01",
            "※All unauthorized personnel are prohibited.\x01",
            "《Liberl Orbalship Co.》\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_20_59E4 end

    SaveToFile()

Try(main)
