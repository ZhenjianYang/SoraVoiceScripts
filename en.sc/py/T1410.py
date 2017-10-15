from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1410   ._SN',
        MapName             = 'Bose',
        Location            = 'T1410.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
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
        'Royal Army Soldier',                   # 9
        'Royal Army Soldier',                   # 10
        'General Morgan',                       # 11
        'Nolan',                                # 12
        'Amelia',                               # 13
        'Alvin',                                # 14
        'Shelby',                               # 15
        'Marco',                                # 16
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
        'ED6_DT07/CH01300 ._CH',             # 00
        'ED6_DT07/CH02083 ._CH',             # 01
        'ED6_DT07/CH01270 ._CH',             # 02
        'ED6_DT07/CH01150 ._CH',             # 03
        'ED6_DT07/CH01040 ._CH',             # 04
        'ED6_DT07/CH01140 ._CH',             # 05
        'ED6_DT07/CH01100 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH01300P._CP',             # 00
        'ED6_DT07/CH02083P._CP',             # 01
        'ED6_DT07/CH01270P._CP',             # 02
        'ED6_DT07/CH01150P._CP',             # 03
        'ED6_DT07/CH01040P._CP',             # 04
        'ED6_DT07/CH01140P._CP',             # 05
        'ED6_DT07/CH01100P._CP',             # 06
    )

    DeclNpc(
        X                   = 104300,
        Z                   = 0,
        Y                   = 107600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 201700,
        Z                   = 0,
        Y                   = 109600,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 209550,
        Z                   = 200,
        Y                   = 11820,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 18100,
        Z                   = 0,
        Y                   = 16400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 15350,
        Z                   = 0,
        Y                   = 15480,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 20700,
        Z                   = 0,
        Y                   = 13230,
        Direction           = 191,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 23470,
        Z                   = 0,
        Y                   = 12150,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 23470,
        Z                   = 0,
        Y                   = 12150,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )


    DeclActor(
        TriggerX            = 17690,
        TriggerZ            = 0,
        TriggerY            = 14350,
        TriggerRange        = 800,
        ActorX              = 18100,
        ActorZ              = 1500,
        ActorY              = 16400,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 207600,
        TriggerZ            = 0,
        TriggerY            = 11880,
        TriggerRange        = 800,
        ActorX              = 209550,
        ActorZ              = 1500,
        ActorY              = 11820,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 123890,
        TriggerZ            = 0,
        TriggerY            = 11990,
        TriggerRange        = 800,
        ActorX              = 123890,
        ActorZ              = 800,
        ActorY              = 11990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_24E",          # 00, 0
        "Function_1_29E",          # 01, 1
        "Function_2_303",          # 02, 2
        "Function_3_480",          # 03, 3
        "Function_4_4A4",          # 04, 4
        "Function_5_4A9",          # 05, 5
        "Function_6_146A",         # 06, 6
        "Function_7_1A2D",         # 07, 7
        "Function_8_1DC3",         # 08, 8
        "Function_9_1DC8",         # 09, 9
        "Function_10_275E",        # 0A, 10
        "Function_11_2BF9",        # 0B, 11
        "Function_12_3044",        # 0C, 12
        "Function_13_34D1",        # 0D, 13
        "Function_14_38B8",        # 0E, 14
    )


    def Function_0_24E(): pass

    label("Function_0_24E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_26C")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_29D")

    label("loc_26C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_276")
    Jump("loc_29D")

    label("loc_276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_296")
    SetChrFlags(0xA, 0x80)
    SetChrPos(0x9, 206990, -20, 101510, 45)
    Jump("loc_29D")

    label("loc_296")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_29D")

    label("loc_29D")

    Return()

    # Function_0_24E end

    def Function_1_29E(): pass

    label("Function_1_29E")

    OP_72(0x3, 0x10)
    OP_72(0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2B2")
    Jump("loc_2D1")

    label("loc_2B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_2BC")
    Jump("loc_2D1")

    label("loc_2BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2CA")
    OP_64(0x1, 0x1)
    Jump("loc_2D1")

    label("loc_2CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_2D1")

    label("loc_2D1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_302")
    OP_79(0x0, 0x2)
    OP_79(0x1, 0x2)
    OP_79(0x2, 0x2)
    OP_79(0x3, 0x2)
    OP_79(0x4, 0x2)
    OP_79(0x5, 0x2)
    OP_79(0x6, 0x2)
    OP_79(0x7, 0x2)
    OP_79(0x8, 0x2)
    OP_7B()

    label("loc_302")

    Return()

    # Function_1_29E end

    def Function_2_303(): pass

    label("Function_2_303")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_328")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_46A")

    label("loc_328")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_341")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_46A")

    label("loc_341")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35A")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_46A")

    label("loc_35A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_373")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_46A")

    label("loc_373")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38C")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_46A")

    label("loc_38C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A5")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_46A")

    label("loc_3A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BE")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_46A")

    label("loc_3BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D7")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_46A")

    label("loc_3D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F0")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_46A")

    label("loc_3F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_409")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_46A")

    label("loc_409")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_422")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_46A")

    label("loc_422")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43B")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_46A")

    label("loc_43B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_454")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_46A")

    label("loc_454")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46A")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_46A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_47F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_46A")

    label("loc_47F")

    Return()

    # Function_2_303 end

    def Function_3_480(): pass

    label("Function_3_480")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A3")
    OP_8D(0xFE, 20000, 13500, 21500, 11750, 1500)
    Jump("Function_3_480")

    label("loc_4A3")

    Return()

    # Function_3_480 end

    def Function_4_4A4(): pass

    label("Function_4_4A4")

    Call(0, 5)
    Return()

    # Function_4_4A4 end

    def Function_5_4A9(): pass

    label("Function_5_4A9")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xA)
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x0, 0)
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_539")
    Jump("loc_57B")

    label("loc_539")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_555")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_57B")

    label("loc_555")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_571")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_57B")

    label("loc_571")

    OP_51(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_57B")

    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_E3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C4")

    ChrTalk(    #0
        0xA,
        (
            "#160FAh, everyone.\x02\x03",

            "Normally, I'd congratulate you on your\x01",
            "work at the towers.\x02\x03",

            "#166FYou'll forgive me if I'm not feeling up to\x01",
            "flattery in the current situation, however.\x02\x03",

            "I know it's not your fault, but\x01",
            "congratulations will have to wait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        "#1015FAww, cut us some slack, General!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        (
            "#1043FIt is true that the situation has\x01",
            "gotten rather...dire.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_74C")

    ChrTalk(    #3
        0x106,
        "#053FThat's one way of puttin' it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A0")

    label("loc_74C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_779")

    ChrTalk(    #4
        0x103,
        "#026FTo say the least.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A0")

    label("loc_779")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A0")

    ChrTalk(    #5
        0x108,
        "#072FIndeed it has.\x02",
    )

    CloseMessageWindow()

    label("loc_7A0")


    ChrTalk(    #6
        0xA,
        (
            "#160FThanks to the generator Professor Russell\x01",
            "provided, we've regained communications,\x01",
            "at least.\x02\x03",

            "But now it's become clear that the Orbal\x01",
            "Shutdown Phenomenon really is affecting\x01",
            "the entire kingdom, from here to Air-Letten.\x02\x03",

            "I suspect you saw on your way in.\x01",
            "Our defense here is badly compromised.\x02\x03",

            "The best I can do here as a leader of the\x01",
            "military is show no weakness to the men.\x02\x03",

            "I hope you will continue to be the kingdom's\x01",
            "hands, bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        "#1006FYou bet, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        (
            "#1042FWe will do our best to live up\x01",
            "to your expectations.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    OP_A2(0x2097)
    Jump("loc_E38")

    label("loc_9C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_D9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_A70")

    ChrTalk(    #9
        0xA,
        (
            "#160FThe best I can do here as a leader of the\x01",
            "military is show no weakness to the men.\x02\x03",

            "I hope you will continue to be the kingdom's\x01",
            "hands, bracers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D9A")

    label("loc_A70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD8")

    ChrTalk(    #10
        0xA,
        (
            "#160FEven with our meager defenses prepared,\x01",
            "not being able to use orbal weaponry\x01",
            "is... Hrmph.\x02\x03",

            "If the enemy attempts to storm the gate,\x01",
            "our only chance to repel them would be\x01",
            "in deadly, hand-to-hand combat.\x02\x03",

            "#163FOur only mercy is that the enemy would\x01",
            "be in the same boat. It would come down\x01",
            "to skill of arms.\x02\x03",

            "On some level, I doubt the Empire would\x01",
            "want to risk it all on such archaic forms\x01",
            "of combat...\x02\x03",

            "#160FThis is nothing more than my wishful thinking,\x01",
            "however.\x02\x03",

            "It is our duty to always prepare for the worst,\x01",
            "and that includes Giliath Osborne treating the\x01",
            "lives of his men cannon fodder.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_D9A")

    label("loc_CD8")


    ChrTalk(    #11
        0xA,
        (
            "#166FThe enemy cannot use orbal weaponry either.\x02\x03",

            "It would all come down to a brutal\x01",
            "melee before the gate.\x02\x03",

            "I doubt even Giliath Osborne has the\x01",
            "stomach for that sort of slaughter, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D9A")

    Jump("loc_E38")

    label("loc_D9D")


    ChrTalk(    #12
        0xA,
        (
            "#160FThe best I can do here as a leader of the\x01",
            "military is show no weakness to the men.\x02\x03",

            "I hope you will continue to be the kingdom's\x01",
            "hands, bracers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E38")

    Jump("loc_1461")

    label("loc_E3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_F3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x349, 7)), scpexpr(EXPR_END)), "loc_E7A")

    ChrTalk(    #13
        0xA,
        (
            "#163F...\x02\x03",

            "Forgive me. I can say no more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F3B")

    label("loc_E7A")


    ChrTalk(    #14
        0xA,
        (
            "#160FEveryone. Good work with the dragon.\x02\x03",

            "#166FI can guess from your faces what you're\x01",
            "here to ask, but...\x02\x03",

            "#163F...\x02\x03",

            "I can say nothing more regarding that matter.\x02\x03",

            "Please understand.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A4F)

    label("loc_F3B")

    Jump("loc_1461")

    label("loc_F3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1461")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x349, 6)), scpexpr(EXPR_END)), "loc_FDA")

    ChrTalk(    #15
        0xA,
        (
            "#160FWe cooperate with the guild thanks to the\x01",
            "mutual trust we share.\x02\x03",

            "Should something happen, be sure to\x01",
            "contact the army, as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1461")

    label("loc_FDA")


    ChrTalk(    #16
        0xA,
        (
            "#160FAh, Cassius' daughter.\x02\x03",

            "I heard about what you did in the capital.\x01",
            "Good work.\x02\x03",

            "Schwarz's report mentioned another society\x01",
            "agent, of a...disturbing nature.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#1003FY-Yeah... It was a pretty big problem,\x01",
            "but we managed to fix it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x106,
        "#053FYeah, it got pretty hairy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xA,
        (
            "#163FHm. I imagine.\x02\x03",

            "From the reports, the members of this\x01",
            "'society' are fearsome foes indeed.\x02\x03",

            "We will need to be ever more on guard.\x02\x03",

            "#160FOut of curiosity...\x02\x03",

            "I take it you will be operating in this\x01",
            "region for the time being?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#1011FAh, yeah, that's the plan.\x02\x03",

            "Right now we're helping out the city of\x01",
            "Bose with some trouble-making monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xA,
        (
            "#165FI see. Monster hunting, excellent.\x02\x03",

            "#160FHowever, should anything happen, do not\x01",
            "hesitate to contact the army.\x02\x03",

            "Our cooperation with the guild is based\x01",
            "on mutual trust.\x02\x03",

            "Especially when it comes to certain groups\x01",
            "of undesirables.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13B5")

    ChrTalk(    #22
        0x103,
        (
            "#027FIf anything happens, we'll notify you\x01",
            "through the guild.\x02\x03",

            "That should be enough, I hope.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1413")

    label("loc_13B5")


    ChrTalk(    #23
        0x106,
        (
            "#050FIf anything happens, we'll send word\x01",
            "through the guild.\x02\x03",

            "No complaints then, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1413")


    ChrTalk(    #24
        0xA,
        (
            "#160FMm, yes, that will suffice.\x02\x03",

            "Make sure not to bite off too much.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A4E)

    label("loc_1461")

    SetChrSubChip(0xA, 0)
    TalkEnd(0xA)
    Return()

    # Function_5_4A9 end

    def Function_6_146A(): pass

    label("Function_6_146A")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_15B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1558")

    ChrTalk(    #25
        0xFE,
        "No movement from the Imperial Army, yet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "Ah, but that just makes me MORE nervous.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "You know what they say about the\x01",
            "calm before the storm and all that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "I can't help but think it feels like that.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_15B4")

    label("loc_1558")


    ChrTalk(    #29
        0xFE,
        "No movement from the Imperial Army, yet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "Ah, but that just makes me MORE nervous.\x02",
    )

    CloseMessageWindow()

    label("loc_15B4")

    Jump("loc_1A29")

    label("loc_15B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_16C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1668")

    ChrTalk(    #31
        0xFE,
        (
            "At this point we've mobilized just\x01",
            "about every reservist who can still\x01",
            "hold a weapon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "This is the biggest national crisis\x01",
            "in a decade, after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_16C3")

    label("loc_1668")


    ChrTalk(    #33
        0xFE,
        (
            "At this point we've mobilized just\x01",
            "about every reservist who can still\x01",
            "hold a weapon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16C3")

    Jump("loc_1A29")

    label("loc_16C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_17FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1740")

    ChrTalk(    #34
        0xFE,
        "We're finally back to standard operations.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "Well, wish they could give us some\x01",
            "leave, at least.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17F7")

    label("loc_1740")


    ChrTalk(    #36
        0xFE,
        "We're finally back to standard operations.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "Granted, with Erebonia always next door,\x01",
            "we can't exactly sit on our butts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "Wish they could give us some leave,\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_17F7")

    Jump("loc_1A29")

    label("loc_17FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1920")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_187F")

    ChrTalk(    #39
        0xFE,
        (
            "We might get mobilized ourselves to\x01",
            "fight that dragon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "Don't mind admitting that THAT\x01",
            "makes me nervous...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_191D")

    label("loc_187F")


    ChrTalk(    #41
        0xFE,
        "The fort's on full standby alert.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "We might get mobilized ourselves to\x01",
            "fight that dragon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "Don't mind admitting that THAT\x01",
            "makes me nervous...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_191D")

    Jump("loc_1A29")

    label("loc_1920")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1A29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_198F")

    ChrTalk(    #44
        0xFE,
        (
            "The deep fog over Rolent the other\x01",
            "day was crazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "Felt like I was swimming in milk!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A29")

    label("loc_198F")


    ChrTalk(    #46
        0xFE,
        (
            "I was dispatched as part of the\x01",
            "reinforcement force to Rolent the\x01",
            "other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        "That fog was ridiculous!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "Felt like I was swimming in milk!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1A29")

    TalkEnd(0x8)
    Return()

    # Function_6_146A end

    def Function_7_1A2D(): pass

    label("Function_7_1A2D")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1B85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1ABA")

    ChrTalk(    #49
        0xFE,
        (
            "The Empire doesn't seem to care much\x01",
            "about our little problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "Guess the non-aggression pact is\x01",
            "doing its job!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B82")

    label("loc_1ABA")


    ChrTalk(    #51
        0xFE,
        (
            "The Empire doesn't seem to care much\x01",
            "about our little problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "Normally they'd be all over us if we\x01",
            "even let our guard down a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "Guess the non-aggression pact is\x01",
            "doing its job!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1B82")

    Jump("loc_1DBF")

    label("loc_1B85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1D18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1C5B")

    ChrTalk(    #54
        0xFE,
        (
            "The dragon's apparently fled into\x01",
            "Nebel Valley.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "On top of being the roughest terrain in\x01",
            "Liberl, it's right on the Erebonian border...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "Gonna be real hard for us to do\x01",
            "anything there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D15")

    label("loc_1C5B")


    ChrTalk(    #57
        0xFE,
        (
            "The dragon's apparently fled into\x01",
            "Nebel Valley.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "Not much the Air Force will be able to\x01",
            "accomplish in a mountain valley like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "I wonder what the general's gonna do.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1D15")

    Jump("loc_1DBF")

    label("loc_1D18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1DBF")

    ChrTalk(    #60
        0xFE,
        (
            "The non-aggression pact is in place,\x01",
            "but our patrols are as heavy as always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "We can't afford to show the Empire even\x01",
            "a moment of weakness, I suppose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DBF")

    TalkEnd(0x9)
    Return()

    # Function_7_1A2D end

    def Function_8_1DC3(): pass

    label("Function_8_1DC3")

    Call(0, 9)
    Return()

    # Function_8_1DC3 end

    def Function_9_1DC8(): pass

    label("Function_9_1DC8")

    TalkBegin(0xB)
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
            "Rest\x01",       # 2
            "Leave\x01",      # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E36")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x54)
    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_1E36")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E4F")
    OP_0D()
    OP_A9(0x55)
    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_1E4F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E69")
    FadeToBright(300, 0)
    TalkEnd(0xB)
    Return()

    label("loc_1E69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_200A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F57")

    ChrTalk(    #62
        0xB,
        (
            "The troops are scared, but I dunno if\x01",
            "the Empire's really gonna attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xB,
        (
            "We have a treaty, after all, and their\x01",
            "guns won't even work, same as ours!\x01",
            "They won't attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xB,
        "The troops are just being skittish.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2007")

    label("loc_1F57")


    ChrTalk(    #65
        0xB,
        (
            "The troops are scared, but I dunno if\x01",
            "the Empire's really gonna attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xB,
        (
            "We have a treaty, after all, and their\x01",
            "guns won't even work, same as ours!\x01",
            "They won't attack.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2007")

    Jump("loc_275A")

    label("loc_200A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_21ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_211A")

    ChrTalk(    #67
        0xB,
        "Hey, welcome to my little border bar!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xB,
        (
            "The base is on alert, as you can see,\x01",
            "but hey, have a drink. Booze is the best\x01",
            "friend you can have in times of crisis, I say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xB,
        (
            "There's nothing to worry about, though.\x01",
            "Fights don't start that easily.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_21EA")

    label("loc_211A")


    ChrTalk(    #70
        0xB,
        (
            "The base is on alert, as you can see,\x01",
            "but hey, have a drink. Booze is the best\x01",
            "friend you can have in times of crisis, I say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xB,
        (
            "There's nothing to worry about, though.\x01",
            "Fights don't start that easily.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21EA")

    Jump("loc_275A")

    label("loc_21ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 0)), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_24B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_245E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_22E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2283")

    ChrTalk(    #72
        0xB,
        (
            "The dragon thing's all settled,\x01",
            "and now we're takin' it easy here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xB,
        "Time to start cookin' dinner!\x02",
    )

    CloseMessageWindow()
    Jump("loc_22E1")

    label("loc_2283")


    ChrTalk(    #74
        0xB,
        "Hey, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xB,
        (
            "The dragon thing's all settled,\x01",
            "and now we're takin' it easy here.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_22E1")

    Jump("loc_245B")

    label("loc_22E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_23DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2368")

    ChrTalk(    #76
        0xB,
        (
            "Thanks to this dragon business,\x01",
            "we're on alert status.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xB,
        (
            "The troops are on standby, preparing\x01",
            "to mobilize.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23D8")

    label("loc_2368")


    ChrTalk(    #78
        0xB,
        (
            "Thanks to this dragon business,\x01",
            "we're on alert status.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xB,
        (
            "Where did our peaceful drinkin'\x01",
            "days go...?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_23D8")

    Jump("loc_245B")

    label("loc_23DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_245B")

    ChrTalk(    #80
        0xB,
        "Hey, welcome to my little border bar!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xB,
        (
            "Can't serve you anything too complicated,\x01",
            "but we do have food and drink.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_245B")

    Jump("loc_24B4")

    label("loc_245E")


    ChrTalk(    #82
        0xB,
        "That sounds like quite the story.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xB,
        "I'd like to hear it over a drink someday.\x02",
    )

    CloseMessageWindow()

    label("loc_24B4")

    Jump("loc_275A")

    label("loc_24B7")


    ChrTalk(    #84
        0xB,
        "Hey, welcome to my little border bar!\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xB, 0x104, 400)
    Sleep(400)

    ChrTalk(    #85
        0xB,
        "Wait, you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x104,
        (
            "#031FHeh, it has been some time, my good man.\x02\x03",

            "I last graced your establishment when I first\x01",
            "came to Liberl, no? Such sweet memories.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #87
        0xB,
        (
            "Yeah, I thought it was you!\x01",
            "You're that per-, er, traveler from Erebonia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xB,
        "So how's Liberl been treating you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x104,
        (
            "#030FFar better than I ever imagined it would.\x02\x03",

            "#035FSpectacle, intrigue...hope.\x01",
            "It has been quite the journey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xB,
        (
            "What, seriously?\x01",
            "That sounds like quite the story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xB,
        "I'd like to hear it over a drink someday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x104,
        (
            "#031FHeh, should I find the time, my good man,\x01",
            "I would be glad to.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A50)
    OP_A2(0x2)

    label("loc_275A")

    TalkEnd(0xB)
    Return()

    # Function_9_1DC8 end

    def Function_10_275E(): pass

    label("Function_10_275E")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_27EC")

    ChrTalk(    #93
        0xFE,
        (
            "I heard that orbments have stopped\x01",
            "working all across the country!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "I thought Nolan had just broken the\x01",
            "stove at first.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BF5")

    label("loc_27EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2942")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28C2")

    ChrTalk(    #95
        0xFE,
        (
            "Haken Gate is always a little busy and\x01",
            "noisy, but this is something else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "The soldiers' expressions seem a lot\x01",
            "more serious than normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        "I hope nothing bad is going to happen...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_293F")

    label("loc_28C2")


    ChrTalk(    #98
        0xFE,
        (
            "Haken Gate is always a little busy and\x01",
            "noisy, but this is something else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        "I hope nothing bad is going to happen...\x02",
    )

    CloseMessageWindow()

    label("loc_293F")

    Jump("loc_2BF5")

    label("loc_2942")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_29A0")

    ChrTalk(    #100
        0xFE,
        "The fort's finally quiet again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        "I feel like I can finally get some sleep!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BF5")

    label("loc_29A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2A1B")

    ChrTalk(    #102
        0xFE,
        (
            "The dragon thing seems like it's\x01",
            "dragging out pretty badly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "The soldiers' expressions seem so anxious.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BF5")

    label("loc_2A1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_2BF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2AEB")

    ChrTalk(    #104
        0xFE,
        (
            "Mountain climbers are manly, I guess,\x01",
            "but they're so rough!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "Now, Colonel Richard?\x01",
            "Ohhhh, he was SOOO perfect and refined!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "*sigh* Why'd he have to end up starting\x01",
            "that coup...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BF5")

    label("loc_2AEB")


    ChrTalk(    #107
        0xFE,
        (
            "That customer over there is apparently\x01",
            "heading up into the mountains for a\x01",
            "climbing expedition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "Hmm, mountain climbers are manly,\x01",
            "I guess...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "But I don't really like those sweaty,\x01",
            "stinky types of men.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        "I much prefer refined, slim men of action!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2BF5")

    TalkEnd(0xC)
    Return()

    # Function_10_275E end

    def Function_11_2BF9(): pass

    label("Function_11_2BF9")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_2CE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2C6A")

    ChrTalk(    #111
        0xFE,
        (
            "We got permission to climb.\x01",
            "It was worth the wait!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        "Time to go climb us a mountain!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CDD")

    label("loc_2C6A")


    ChrTalk(    #113
        0xFE,
        (
            "We finally have permission to go climbing\x01",
            "up the Krones!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        "Just like Shelby said, it was worth waiting!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_2CDD")

    Jump("loc_3040")

    label("loc_2CE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2E75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2D6F")

    ChrTalk(    #115
        0xFE,
        (
            "Even if it's the army saying so,\x01",
            "I can't just abandon my climbing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "Maybe I SHOULD ignore 'em and\x01",
            "go do it anyway...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E72")

    label("loc_2D6F")


    ChrTalk(    #117
        0xFE,
        (
            "The Royal Army's warned us to stop our\x01",
            "climb.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "What a joke!\x01",
            "We've been waiting MONTHS for this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "Comin' out this far, only to be told to\x01",
            "turn back...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "It's enough to make me want to tell\x01",
            "the army to piss themselves and go\x01",
            "climbing anyway!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_2E72")

    Jump("loc_3040")

    label("loc_2E75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_3040")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2F39")

    ChrTalk(    #121
        0xFE,
        (
            "Shelby and I are what you'd call mountain men.\x01",
            "In fact, we're planning on climbing the Krone mountains\x01",
            "on the border.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "We're stopping over here to prepare\x01",
            "for the climb.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3040")

    label("loc_2F39")


    ChrTalk(    #123
        0xFE,
        (
            "Shelby and I are what you'd call mountain men.\x01",
            "In fact, we're planning on climbing the Krone mountains\x01",
            "on the border.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "The western region of Nebel Valley\x01",
            "is still pretty much unknown territory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "That means it's pretty attractive territory\x01",
            "for us!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_3040")

    TalkEnd(0xD)
    Return()

    # Function_11_2BF9 end

    def Function_12_3044(): pass

    label("Function_12_3044")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_31F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_30E5")

    ChrTalk(    #126
        0xFE,
        (
            "Gotta be careful picking the route we\x01",
            "want to try and take.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "After all, we'll be tackling a mountain\x01",
            "no man has ever scaled before.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31ED")

    label("loc_30E5")


    ChrTalk(    #128
        0xFE,
        (
            "With the wind today, we don't need\x01",
            "to worry too much about the fog.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "We still have to be careful about\x01",
            "the route we want to try and take.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "After all, we'll be tackling a mountain\x01",
            "no man has ever scaled before.\x01",
            "We need to be as careful as possible.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_31ED")

    Jump("loc_34CD")

    label("loc_31F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_3396")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3275")

    ChrTalk(    #131
        0xFE,
        (
            "If we wait, the warning will clear up.\x01",
            "I'm certain of it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "I wish my partner Alvin was a bit\x01",
            "more patient.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3393")

    label("loc_3275")


    ChrTalk(    #133
        0xFE,
        (
            "The army is advising all potential\x01",
            "climbers away from the mountains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "This is EXACTLY the sort of thing that\x01",
            "should test a climber's endurance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "The best thing we can do now is\x01",
            "wait patiently, not complain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "If we wait, the warning will clear up.\x01",
            "I'm certain of it!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_3393")

    Jump("loc_34CD")

    label("loc_3396")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_34CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3437")

    ChrTalk(    #137
        0xFE,
        (
            "The weather in Nebel Valley is prone\x01",
            "to change at the drop of a hat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "We've got to carefully see through its\x01",
            "shifting tides of clouds.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34CD")

    label("loc_3437")


    ChrTalk(    #139
        0xFE,
        (
            "We've got our rations, and we've checked\x01",
            "our equipment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "All that's left is to find the right time\x01",
            "to begin our ascent up the mountain.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_34CD")

    TalkEnd(0xE)
    Return()

    # Function_12_3044 end

    def Function_13_34D1(): pass

    label("Function_13_34D1")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_3672")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35E1")

    ChrTalk(    #141
        0xFE,
        "I wonder if Erebonia really will move.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "We just signed the non-aggression pact\x01",
            "with Liberl. Would the government really\x01",
            "ignore that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "No, what am I saying?\x01",
            "The fatherland would never throw away\x01",
            "its honor so easily. That isn't our way.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_366F")

    label("loc_35E1")


    ChrTalk(    #144
        0xFE,
        "I wonder if Erebonia really will move.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "We just signed the non-aggression pact\x01",
            "with Liberl. Would the government really\x01",
            "ignore that?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_366F")

    Jump("loc_38B4")

    label("loc_3672")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_38B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37DC")

    ChrTalk(    #146
        0xFE,
        (
            "With the airships grounded, I'm returning\x01",
            "to Erebonia on foot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "I never dreamed I'd run into a situation\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "As an Erebonian, I wish for glory\x01",
            "for the fatherland, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "But I believe that's best accomplished\x01",
            "through peace, not force of arms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "Making Erebonia and Liberl fear\x01",
            "one another serves no purpose.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_38B4")

    label("loc_37DC")


    ChrTalk(    #151
        0xFE,
        (
            "As an Erebonian, I wish for glory\x01",
            "for the fatherland, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "But I believe that's best accomplished\x01",
            "through peace, not force of arms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "Making Erebonia and Liberl fear\x01",
            "one another serves no purpose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38B4")

    TalkEnd(0xF)
    Return()

    # Function_13_34D1 end

    def Function_14_38B8(): pass

    label("Function_14_38B8")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #154
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_14_38B8 end

    SaveToFile()

Try(main)
