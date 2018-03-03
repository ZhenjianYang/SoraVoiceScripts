from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5400   ._SN',
        MapName             = 'Other',
        Location            = 'C5400.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60028",
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
        'Renne',                                # 9
        'Walter',                               # 10
        'Luciola',                              # 11
        'Bleublanc',                            # 12
        'Gilbert',                              # 13
        'Campanella',                           # 14
        'Enhanced Jaeger',                      # 15
        'Enhanced Jaeger',                      # 16
        'Enhanced Jaeger',                      # 17
        'Target Camera',                        # 18
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT27/CH03540 ._CH',             # 00
        'ED6_DT27/CH03510 ._CH',             # 01
        'ED6_DT27/CH03500 ._CH',             # 02
        'ED6_DT27/CH03523 ._CH',             # 03
        'ED6_DT27/CH03530 ._CH',             # 04
        'ED6_DT27/CH03750 ._CH',             # 05
        'ED6_DT26/CH20475 ._CH',             # 06
        'ED6_DT26/CH20412 ._CH',             # 07
        'ED6_DT26/CH20208 ._CH',             # 08
        'ED6_DT27/CH03600 ._CH',             # 09
        'ED6_DT26/CH20764 ._CH',             # 0A
        'ED6_DT26/CH20763 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT27/CH03540P._CP',             # 00
        'ED6_DT27/CH03510P._CP',             # 01
        'ED6_DT27/CH03500P._CP',             # 02
        'ED6_DT27/CH03523P._CP',             # 03
        'ED6_DT27/CH03530P._CP',             # 04
        'ED6_DT27/CH03750P._CP',             # 05
        'ED6_DT26/CH20475P._CP',             # 06
        'ED6_DT26/CH20412P._CP',             # 07
        'ED6_DT26/CH20208P._CP',             # 08
        'ED6_DT27/CH03600P._CP',             # 09
        'ED6_DT26/CH20764P._CP',             # 0A
        'ED6_DT26/CH20763P._CP',             # 0B
    )

    DeclNpc(
        X                   = 61490,
        Z                   = 0,
        Y                   = -22730,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -134180,
        Z                   = 0,
        Y                   = -28920,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x183,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -130090,
        Z                   = 0,
        Y                   = 9850,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -133800,
        Z                   = 0,
        Y                   = 48910,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 2740,
        Z                   = 0,
        Y                   = -24540,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -38630,
        Z                   = 0,
        Y                   = -68760,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -87010,
        Z                   = 0,
        Y                   = -24670,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -37010,
        Z                   = 0,
        Y                   = 66950,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
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


    DeclEvent(
        X                   = -42980,
        Y                   = -1000,
        Z                   = 75190,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 19,
    )

    DeclEvent(
        X                   = -36920,
        Y                   = -1000,
        Z                   = -67150,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 20,
    )

    DeclEvent(
        X                   = 70070,
        Y                   = -1000,
        Z                   = -234030,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 21,
    )


    DeclActor(
        TriggerX            = 61080,
        TriggerZ            = 0,
        TriggerY            = -184550,
        TriggerRange        = 1000,
        ActorX              = 61080,
        ActorZ              = 1000,
        ActorY              = -184550,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2CE",          # 00, 0
        "Function_1_361",          # 01, 1
        "Function_2_392",          # 02, 2
        "Function_3_3A8",          # 03, 3
        "Function_4_421",          # 04, 4
        "Function_5_49A",          # 05, 5
        "Function_6_517",          # 06, 6
        "Function_7_65D",          # 07, 7
        "Function_8_A90",          # 08, 8
        "Function_9_E50",          # 09, 9
        "Function_10_1475",        # 0A, 10
        "Function_11_1911",        # 0B, 11
        "Function_12_1D51",        # 0C, 12
        "Function_13_1D82",        # 0D, 13
        "Function_14_1DB3",        # 0E, 14
        "Function_15_1DE4",        # 0F, 15
        "Function_16_2DFD",        # 10, 16
        "Function_17_2E32",        # 11, 17
        "Function_18_2E8A",        # 12, 18
        "Function_19_2FA0",        # 13, 19
        "Function_20_3036",        # 14, 20
        "Function_21_3037",        # 15, 21
        "Function_22_3038",        # 16, 22
        "Function_23_35D5",        # 17, 23
        "Function_24_4337",        # 18, 24
    )


    def Function_0_2CE(): pass

    label("Function_0_2CE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_302")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)

    label("loc_302")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_349")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_32D")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 23)
    Jump("loc_349")

    label("loc_32D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_349")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 22)

    label("loc_349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_360")
    OP_A3(0x2504)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 15)

    label("loc_360")

    Return()

    # Function_0_2CE end

    def Function_1_361(): pass

    label("Function_1_361")

    OP_72(0x400, 0x0)
    ExitThread()
    OP_71(0x401, 0x0)
    ExitThread()
    OP_71(0x42B, 0x0)
    ExitThread()
    OP_71(0x42C, 0x0)
    ExitThread()
    OP_71(0x425, 0x0)
    ExitThread()
    OP_71(0x426, 0x0)
    ExitThread()
    OP_72(0x1002, 0x0)
    ExitThread()
    OP_72(0x1002, 0x0)
    ExitThread()
    Return()

    # Function_1_361 end

    def Function_2_392(): pass

    label("Function_2_392")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A7")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_392")

    label("loc_3A7")

    Return()

    # Function_2_392 end

    def Function_3_3A8(): pass

    label("Function_3_3A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_420")
    OP_8E(0xFE, 0xAD2, 0x0, 0x55E6, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0x131A, 0x0, 0x5582, 0xBB8, 0x0)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x13F6, 0x0, 0xFFFF9F34, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0xAB4, 0x0, 0xFFFFA024, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Jump("Function_3_3A8")

    label("loc_420")

    Return()

    # Function_3_3A8 end

    def Function_4_421(): pass

    label("Function_4_421")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_499")
    OP_8E(0xFE, 0xFFFEAC64, 0x0, 0x5726, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0xFFFEA340, 0x0, 0x562C, 0xBB8, 0x0)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xFFFEA2B4, 0x0, 0xFFFF9FB6, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0xFFFEAC1E, 0x0, 0xFFFF9FA2, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Jump("Function_4_421")

    label("loc_499")

    Return()

    # Function_4_421 end

    def Function_5_49A(): pass

    label("Function_5_49A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_516")
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0xFFFF4782, 0x0, 0x10842, 0xBB8, 0x0)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0xFFFF6F6E, 0x0, 0x10586, 0xBB8, 0x0)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    Jump("Function_5_49A")

    label("loc_516")

    Return()

    # Function_5_49A end

    def Function_6_517(): pass

    label("Function_6_517")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_523")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_65C")
    OP_99(0xFE, 0x0, 0x2, 0x3E8)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_556")
    Sleep(1000)
    Jump("loc_5AF")

    label("loc_556")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56B")
    Sleep(1500)
    Jump("loc_5AF")

    label("loc_56B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_580")
    Sleep(2000)
    Jump("loc_5AF")

    label("loc_580")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_595")
    Sleep(2500)
    Jump("loc_5AF")

    label("loc_595")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AA")
    Sleep(3000)
    Jump("loc_5AF")

    label("loc_5AA")

    Sleep(1800)

    label("loc_5AF")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_600")
    Sleep(1000)
    Jump("loc_659")

    label("loc_600")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_615")
    Sleep(1500)
    Jump("loc_659")

    label("loc_615")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_62A")
    Sleep(2000)
    Jump("loc_659")

    label("loc_62A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63F")
    Sleep(2500)
    Jump("loc_659")

    label("loc_63F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_654")
    Sleep(3000)
    Jump("loc_659")

    label("loc_654")

    Sleep(1800)

    label("loc_659")

    Jump("loc_523")

    label("loc_65C")

    Return()

    # Function_6_517 end

    def Function_7_65D(): pass

    label("Function_7_65D")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A1A")
    OP_A2(0x0)

    ChrTalk(    #0
        0x10,
        (
            "#260FOh, I wasn't expecting you to come, Loewe.\x02\x03",

            "Did the professor call you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x124,
        (
            "#120FHe certainly did. It's my turn, apparently.\x02\x03",

            "I hear you performed your part over at the tower \x01",
            "quite well, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        (
            "#260F*sigh* I wish I could say that.\x02\x03",

            "If I'd just had a liiiittle longer, I could've \x01",
            "slaughtered every last one of them, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x124,
        (
            "#120FYou didn't need to do that in the first place.\x02\x03",

            "With the Aureole's power in the professor's hands,\x01",
            "humanity is as good as extinct regardless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        "#260FHuh, you think?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x124,
        (
            "#120FIt doesn't take much pondering.\x02\x03",

            "We're talking about him gaining power beyond human\x01",
            "comprehension here. What will happen if he does \x01",
            "that is as clear as day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        (
            "#260F*giggle* I suppose you're right.\x02\x03",

            "He's always been quite the mischief-maker, after \x01",
            "all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x124,
        (
            "#120FNow it's just a case of seeing whether they get to\x01",
            "it first, or we do...\x02\x03",

            "Whatever the outcome ends up being, though, it'll \x01",
            "be decided soon enough.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A8C")

    label("loc_A1A")


    ChrTalk(    #8
        0x10,
        (
            "#260FThe professor with the world in his hands...\x02\x03",

            "Heehee. Things are really going to get \x01",
            "interesting soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A8C")

    TalkEnd(0x10)
    Return()

    # Function_7_65D end

    def Function_8_A90(): pass

    label("Function_8_A90")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DDD")
    OP_A2(0x1)

    ChrTalk(    #9
        0x11,
        (
            "#250FMan, you SEEN that huge thing up in the sky?\x02\x03",

            "Heh heh. Now things're REALLY gettin' interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x124,
        (
            "#120FIf you say so.\x02\x03",

            "As far as I'm concerned, it's nothing at all to do\x01",
            "with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x11,
        (
            "#250FHmph. Man, you really could stand to have a bit \x01",
            "more fun with life.\x02\x03",

            "Bah. If I'd known this was going to happen,\x01",
            "I would've got that damn kid when I last had\x01",
            "the chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x124,
        "#120FHe showed up at the tower you were at too, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x11,
        (
            "#250FHe wasn't half bad, but it's not hard to see his \x01",
            "strength's fighting from the shadows and not the \x01",
            "open.\x02\x03",

            "I'll get him next time, no doubting that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x124,
        (
            "#120FI certainly hope so...\x02\x03",

            "Still, don't underestimate him. He's a master at \x01",
            "what he does.\x02\x03",

            "Let your guard down, and you won't even know what\x01",
            "hit you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x11,
        (
            "#250FBah. What kind of a half-wit do you take me for? \x01",
            "I know that much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E4C")

    label("loc_DDD")


    ChrTalk(    #16
        0x11,
        (
            "#250FJust you wait. I'll be back with his head soon \x01",
            "enough.\x02\x03",

            "Heh heh. Somethin' to look forward to, huh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E4C")

    TalkEnd(0x11)
    Return()

    # Function_8_A90 end

    def Function_9_E50(): pass

    label("Function_9_E50")

    TalkBegin(0x12)
    ClearChrFlags(0x12, 0x10)
    TurnDirection(0x12, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E75")
    SetChrSubChip(0x12, 1)
    Jump("loc_E90")

    label("loc_E75")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E8B")
    SetChrSubChip(0x12, 2)
    Jump("loc_E90")

    label("loc_E8B")

    SetChrSubChip(0x12, 0)

    label("loc_E90")

    OP_8C(0x12, 180, 0)
    SetChrFlags(0x12, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13A8")
    OP_A2(0x2)

    ChrTalk(    #17
        0x12,
        (
            "#240F*giggle* Oh my, this is quite the surprise.\x02\x03",

            "What brings you here? Feeling lonely and in need \x01",
            "of company?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x124,
        (
            "#120FThat's enough of that.\x02\x03",

            "I think you know well enough that I'm not here to \x01",
            "hear that kind of nonsense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x12,
        (
            "#240FHeehee. I was only playing around.\x02\x03",

            "Still, now the Gospel Plan is finally in its \x01",
            "finishing stages...\x02\x03",

            "I suppose it's almost your time to shine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x124,
        (
            "#120FMost likely so.\x02\x03",

            "...Still, if you don't mind me asking...\x02\x03",

            "Just what drove you to stick around and help the \x01",
            "professor for so long to begin with?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x12,
        (
            "#240FHeehee. It was just how fate deigned it to be.\x02\x03",

            "I've been looking for something for a long time, \x01",
            "and I finally found it. That's all there is to it,\x01",
            "really.\x02\x03",

            "In that sense, I don't think my reasoning is all \x01",
            "that different to any of the others gathered here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x124,
        (
            "#120F...I suppose you're right.\x02\x03",

            "Well, I hope you manage to get whatever it is \x01",
            "you've finally found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x12,
        (
            "#240FI'm not sure I'd put much faith in that.\x02\x03",

            "If anything, I fear I may already be too late...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x124,
        (
            "#120F...\x02\x03",

            "...Regardless, we've come this far. I intend to\x01",
            "keep fighting to the bitter end so I can come\x01",
            "away from all this without any regrets.\x02\x03",

            "The path I walk has been a bloodstained one from\x01",
            "the start. There's nothing to be gained by turning\x01",
            "back now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_146C")

    label("loc_13A8")


    ChrTalk(    #25
        0x12,
        (
            "#240FI'm only really here helping the professor because\x01",
            "of a quirk of fate, if you will.\x02\x03",

            "In that sense, I don't think my reasoning is all \x01",
            "that different to any of the others gathered here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_146C")

    SetChrSubChip(0x12, 0)
    TalkEnd(0x12)
    Return()

    # Function_9_E50 end

    def Function_10_1475(): pass

    label("Function_10_1475")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1853")
    OP_A2(0x3)

    ChrTalk(    #26
        0x13,
        (
            "#230FOh my, to what do I owe this honor?\x02\x03",

            "I wasn't expecting the famed Bladelord himself to\x01",
            "pay a visit to my humble abode.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x124,
        (
            "#120FHeh. I'm impressed that you keep that mask of \x01",
            "yours on even during your off-time like this.\x02\x03",

            "Do you really hate exposing your true self that \x01",
            "much?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x13,
        (
            "#230FHeh. What a peculiar question.\x02\x03",

            "Especially given that you wear a mask yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x124,
        "#120F...What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x13,
        (
            "#230FHuman beings all assume a number of masks \x01",
            "throughout their lives.\x02\x03",

            "I imagine that deep down, you know what I mean, \x01",
            "do you not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x124,
        "#120F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x13,
        (
            "#230FI, on the other hand, possess but this one mask.\x02\x03",

            "It is my true, and only face; and my true face is\x01",
            "therefore perfectly visible when I wear it.\x02\x03",

            "So I don't believe one such as yourself, who uses\x01",
            "many, has any right to criticize me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x124,
        (
            "#120FHeh. When you put it like that, I suppose I don't.\x02\x03",

            "Perhaps there's a method in your madness after\x01",
            "all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x13,
        (
            "#230FWithout thought, there is no beauty.\x02\x03",

            "Simple enough, no?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_190D")

    label("loc_1853")


    ChrTalk(    #35
        0x13,
        (
            "#230FHuman beings all assume a number of masks \x01",
            "throughout their lives.\x02\x03",

            "Perhaps you should work on reducing your own \x01",
            "collection before attempting to jest at the \x01",
            "expense of mine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_190D")

    TalkEnd(0x13)
    Return()

    # Function_10_1475 end

    def Function_11_1911(): pass

    label("Function_11_1911")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CBB")
    OP_A2(0x4)

    ChrTalk(    #36
        0x14,
        "#1220FL-Lord Loewe?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x124,
        (
            "#120FPatrolling well, I see.\x02\x03",

            "...Nothing is amiss, I take it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x14,
        (
            "#1220FN-Nothing whatsoever, sir!\x02\x03",

            "I-I intend to continue giving my absolutely \x01",
            "fullest to whatever task is assigned to me, sir!\x02\x03",

            "I may be leaving here soon to begin a new mission,\x01",
            "but the same will be true for that, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x124,
        "#120FOh? And what mission would that be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x14,
        "#1220FAssaulting Jenis Royal Academy, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x124,
        (
            "#120F...What?\x02\x03",

            "...On whose orders?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x14,
        "#1220FL-Lord Campanella's, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x124,
        (
            "#120F...\x02\x03",

            "What does he think he's doing...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x14,
        "#1220FI-Is something the matter, sir?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x124,
        (
            "#120F...No. Good luck with your mission.\x02\x03",

            "Just be sure not to cause any more casualties than\x01",
            "necessary.\x02\x03",

            "...Given all the work that remains, I would rather\x01",
            "retain as many of our resources as possible, after\x01",
            "all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x14,
        (
            "#1220FOf course, sir! Thank you, sir!\x02\x03",

            "I will be sure to astound even you with my \x01",
            "spectacular leadership abilities!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D4D")

    label("loc_1CBB")


    ChrTalk(    #47
        0x14,
        (
            "#1220FI will be sure to lead the academy's assault to \x01",
            "great success!\x02\x03",

            "I hope you will look forward to seeing what a \x01",
            "great leader I can be!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D4D")

    TalkEnd(0x14)
    Return()

    # Function_11_1911 end

    def Function_12_1D51(): pass

    label("Function_12_1D51")

    TalkBegin(0x16)

    ChrTalk(    #48
        0x16,
        "◆Talk to Reinforced Jaeger (Repeat)\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x16)
    Return()

    # Function_12_1D51 end

    def Function_13_1D82(): pass

    label("Function_13_1D82")

    TalkBegin(0x17)

    ChrTalk(    #49
        0x17,
        "◆Talk to Reinforced Jaeger (Repeat)\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x17)
    Return()

    # Function_13_1D82 end

    def Function_14_1DB3(): pass

    label("Function_14_1DB3")

    TalkBegin(0x18)

    ChrTalk(    #50
        0x18,
        "◆Talk to Reinforced Jaeger (Repeat)\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x18)
    Return()

    # Function_14_1DB3 end

    def Function_15_1DE4(): pass

    label("Function_15_1DE4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(60330, 1000, 52870, 0)
    OP_67(0, 5360, -10000, 0)
    OP_6B(2980, 0)
    OP_6C(45000, 0)
    OP_6E(291, 0)
    SetChrPos(0x124, 59900, 1000, 52500, 90)
    SetChrChipByIndex(0x124, 6)
    SetChrSubChip(0x124, 2)
    SetChrFlags(0x124, 0x4)
    OP_4A(0x14, 255)
    Sleep(1000)
    Sleep(500)
    OP_22(0x1C2, 0x0, 0x64)
    Sleep(1000)
    SetMessageWindowPos(350, 120, -1, -1)
    SetChrName("Boy's Voice")

    AnonymousTalk(    #51
        (
            "\x07\x0CLoewe?\x02\x03",

            "Hey, Loewe!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AD(0x240060, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Loewe")

    AnonymousTalk(    #52
        "\x07\x0CHmm? What is it?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 120, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #53
        (
            "\x07\x0CCan I start eating now?\x02\x03",

            "I'm starving...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(280, 100, -1, -1)
    SetChrName("Karin")

    AnonymousTalk(    #54
        (
            "\x07\x0CHeehee. Oh, no, we can't have that, Joshua.\x02\x03",

            "We all promised to eat together, didn't we?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(380, 120, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #55
        "\x07\x0CB-But...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Loewe")

    AnonymousTalk(    #56
        (
            "\x07\x0CHaha. Sorry, I didn't realize you were that hungry.\x02\x03",

            "Just let me do ten more, then we can have lunch.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 120, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #57
        "Okay!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_23(0x1C2)
    OP_1D(0x4A)
    Sleep(1000)
    OP_AD(0x240061, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(40, 80, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #58
        (
            "\x07\x0C...Hey, Loewe?\x02\x03",

            "Is it true you're going to be taking the bracer \x01",
            "examination soon?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(180, 300, -1, -1)
    SetChrName("Loewe")

    AnonymousTalk(    #59
        "\x07\x0CHold on, who did you hear that from?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(40, 80, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #60
        (
            "\x07\x0CThe grown-ups were all talking about how you're \x01",
            "gonna be going into town for it. Is it true?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(180, 300, -1, -1)
    SetChrName("Loewe")

    AnonymousTalk(    #61
        (
            "\x07\x0C...Yeah, it is.\x02\x03",

            "I haven't decided exactly when, but it won't be in\x01",
            "the too distant future.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(40, 80, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #62
        (
            "\x07\x0COh...\x02\x03",

            "...If you pass, are you gonna be moving there for\x01",
            "good?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(180, 300, -1, -1)
    SetChrName("Loewe")

    AnonymousTalk(    #63
        (
            "\x07\x0CWhy do you ask?\x02\x03",

            "Think you'll be lonely without me?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(40, 80, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #64
        (
            "\x07\x0C...Y-Yeah, I guess.\x02\x03",

            "...Hey, if you really need to go there, can't we \x01",
            "all live there together?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(180, 300, -1, -1)
    SetChrName("Loewe")

    AnonymousTalk(    #65
        "\x07\x0CWhat?!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(40, 80, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #66
        (
            "\x07\x0CThat way I'd be able to learn to fight with a \x01",
            "sword, too...\x02\x03",

            "And you'd be able to be able to be with Karin, \x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(180, 300, -1, -1)
    SetChrName("Loewe")

    AnonymousTalk(    #67
        (
            "\x07\x0CHaha... You just had to throw that in, didn't you?\x02\x03",

            "Do you have any idea how much mira we'd need for \x01",
            "the three of us to live there?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(40, 80, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #68
        (
            "\x07\x0CAww... I thought it was a good idea, too.\x02\x03",

            "But I guess I'm just being silly.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(180, 300, -1, -1)
    SetChrName("Loewe")

    AnonymousTalk(    #69
        (
            "\x07\x0CNo, I don't think so.\x02\x03",

            "It's not feasible right now...but I'd certainly \x01",
            "like it to happen one day in the future.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(40, 80, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #70
        "\x07\x0CMe too!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0x7D0)
    OP_AE(0x1F4)
    Sleep(2000)
    OP_22(0x87, 0x0, 0x64)
    Sleep(1000)
    OP_43(0x124, 0x0, 0x0, 0x10)
    Sleep(2000)
    OP_22(0x72, 0x0, 0x64)
    Sleep(800)
    OP_22(0x72, 0x0, 0x64)
    Sleep(1000)
    SetMessageWindowPos(100, 100, -1, -1)
    SetChrName("Old Man's Voice")

    AnonymousTalk(    #71
        (
            "\x07\x0C#2SLoewe!\x02\x03",

            "LOEWE!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 300, -1, -1)
    SetChrName("Loewe")

    AnonymousTalk(    #72
        (
            "\x07\x0C...What is it?\x02\x03",

            "What are you shouting for?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 100, -1, -1)
    SetChrName("Old Man's Voice")

    AnonymousTalk(    #73
        "\x07\x0C#3SR-Run! Now!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 300, -1, -1)
    SetChrName("Loewe")

    AnonymousTalk(    #74
        "\x07\x0CWhat?! Why?!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_AD(0x240063, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #75
        "\x07\x0CWh-Where are you going?!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 50, -1, -1)
    SetChrName("Karin")

    AnonymousTalk(    #76
        "\x07\x0CIt doesn't matter! Just follow me! Hurry!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 50, -1, -1)
    SetChrName("Loewe")

    AnonymousTalk(    #77
        (
            "\x07\x0CJoshua, Karin! Go on ahead!\x02\x03",

            "Get yourselves to the next village! Hurry!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(380, 50, -1, -1)
    SetChrName("Karin")

    AnonymousTalk(    #78
        "\x07\x0CWhat about you?!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 50, -1, -1)
    SetChrName("Loewe")

    AnonymousTalk(    #79
        (
            "\x07\x0CI'm going to go and try to hold them off!\x02\x03",

            "I'll come after you as soon as I can. You know how\x01",
            "fast I can run.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(380, 50, -1, -1)
    SetChrName("Karin")

    AnonymousTalk(    #80
        (
            "\x07\x0CWell, if you're sure...\x02\x03",

            "But be careful! Please!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 50, -1, -1)
    SetChrName("Loewe")

    AnonymousTalk(    #81
        "\x07\x0CJust go!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(2000)
    OP_43(0x124, 0x1, 0x0, 0x11)
    WaitChrThread(0x124, 0x1)
    OP_44(0x124, 0xFF)
    Sleep(1000)
    OP_22(0x1CD, 0x0, 0x64)
    Sleep(2000)
    OP_1D(0x5B)
    Sleep(1000)
    OP_AD(0x240065, 0x0, 0x0, 0x12C)
    Sleep(1000)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Karin")

    AnonymousTalk(    #82
        (
            "\x07\x0CY-You really did come...\x02\x03",

            "I knew you'd come for us... I knew you would...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 50, -1, -1)
    SetChrName("Loewe")

    AnonymousTalk(    #83
        "\x07\x0CDon't try and talk!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Karin")

    AnonymousTalk(    #84
        (
            "\x07\x0CThank you... But it's too late for me now...\x02\x03",

            "...Thank you...for everything, Loewe...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(380, 50, -1, -1)
    SetChrName("Loewe")

    AnonymousTalk(    #85
        "\x07\x0CStay with us, Karin!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Karin")

    AnonymousTalk(    #86
        (
            "\x07\x0CPlease...\x02\x03",

            "Take care of...Joshua...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 50, -1, -1)
    SetChrName("Loewe")

    AnonymousTalk(    #87
        (
            "\x07\x0CI will!\x02\x03",

            "So you...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Karin")

    AnonymousTalk(    #88
        (
            "\x07\x0C...Thank...you...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 50, -1, -1)
    SetChrName("Loewe")

    AnonymousTalk(    #89
        "\x07\x0CK-Karin?!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0xBB8)
    OP_AE(0xC8)
    OP_23(0x1CD)
    SetMessageWindowPos(350, 50, -1, -1)
    SetChrName("Loewe")

    AnonymousTalk(    #90
        "\x07\x0C#5SKarin! Karin!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(4000)
    FadeToBright(1000, 0)
    Sleep(400)
    FadeToDark(1000, 0, -1)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #91
        0x124,
        "#121F#5P?!\x02",
    )

    CloseMessageWindow()
    Sleep(2000)

    ChrTalk(    #92
        0x124,
        (
            "#124F#5P...Ugh...\x02\x03",

            "That dream again...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(5470, 0, 17810, 0)
    OP_67(0, 5480, -10000, 0)
    OP_6B(3280, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x124, 8470, 0, 17170, 270)
    SetChrChipByIndex(0x124, 65535)
    SetChrSubChip(0x124, 0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1D(0x1C)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x9, 0)
    OP_70(0x9, 0xF)
    OP_73(0x9)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 3840, 0, 4990, 0)

    def lambda_2BC8():
        OP_8E(0xFE, 0x10A4, 0x0, 0x4204, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x124, 0, lambda_2BC8)
    Sleep(300)

    def lambda_2BE8():
        OP_8E(0xFE, 0x1054, 0x0, 0x3782, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_2BE8)
    WaitChrThread(0x124, 0x0)
    OP_6F(0x9, 15)
    OP_70(0x9, 0x0)
    WaitChrThread(0x16, 0x0)

    ChrTalk(    #93
        0x16,
        "L-Lord Loewe?\x02",
    )

    CloseMessageWindow()

    def lambda_2C2E():
        OP_6D(5560, 0, 17030, 1000)
        ExitThread()

    QueueWorkItem(0x124, 0, lambda_2C2E)
    OP_8C(0x124, 180, 400)
    WaitChrThread(0x124, 0x0)
    Sleep(300)

    ChrTalk(    #94
        0x124,
        "#121F#5PWhat is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x16,
        (
            "The professor awaits you in the cathedral, sir.\x02\x03",

            "He says he would like to speak with you regarding\x01",
            "the upcoming mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x124,
        "#121F#5PAll right. I'll go as soon as I can.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x16,
        "If you will excuse me, then, sir.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x16, 180, 400)
    Sleep(200)

    def lambda_2D53():
        OP_8E(0xFE, 0xF00, 0x0, 0x137E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_2D53)
    WaitChrThread(0x16, 0x0)
    SetChrPos(0x16, -38630, 0, -68760, 270)
    OP_43(0x16, 0x0, 0x0, 0x2)
    OP_6D(5470, 0, 17810, 1000)

    ChrTalk(    #98
        0x124,
        (
            "#121F#5P*sigh*...\x02\x03",

            "I guess I don't have the luxury of dwelling on the\x01",
            "past right now.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_4B(0x14, 255)
    EventEnd(0x0)
    Return()

    # Function_15_1DE4 end

    def Function_16_2DFD(): pass

    label("Function_16_2DFD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E31")
    OP_22(0x235, 0x0, 0x32)
    Sleep(1000)
    OP_22(0x1F7, 0x0, 0x32)
    Sleep(1000)
    OP_22(0x1F7, 0x0, 0x32)
    Sleep(500)
    OP_22(0x235, 0x0, 0x32)
    Sleep(800)
    Jump("Function_16_2DFD")

    label("loc_2E31")

    Return()

    # Function_16_2DFD end

    def Function_17_2E32(): pass

    label("Function_17_2E32")

    OP_24(0x235, 0x32)
    OP_24(0x1F7, 0x32)
    Sleep(300)
    OP_24(0x235, 0x28)
    OP_24(0x1F7, 0x28)
    Sleep(300)
    OP_24(0x235, 0x1E)
    OP_24(0x1F7, 0x1E)
    Sleep(300)
    OP_24(0x235, 0x14)
    OP_24(0x1F7, 0x14)
    Sleep(300)
    OP_24(0x235, 0xA)
    OP_24(0x1F7, 0xA)
    Sleep(300)
    OP_24(0x235, 0x0)
    OP_24(0x1F7, 0x0)
    Sleep(300)
    OP_23(0x235)
    OP_23(0x1F7)
    OP_23(0x87)
    Return()

    # Function_17_2E32 end

    def Function_18_2E8A(): pass

    label("Function_18_2E8A")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x124, 61000, 0, -185610, 0)
    SetChrSubChip(0x124, 0)
    OP_6D(61240, 0, -185600, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_20(0xBB8)

    def lambda_2EF0():
        OP_6D(60980, 500, -184400, 3000)
        ExitThread()

    QueueWorkItem(0x124, 0, lambda_2EF0)

    def lambda_2F08():
        OP_67(0, 5000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x124, 1, lambda_2F08)

    def lambda_2F20():
        OP_6B(3120, 3000)
        ExitThread()

    QueueWorkItem(0x124, 2, lambda_2F20)

    def lambda_2F30():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x124, 3, lambda_2F30)
    WaitChrThread(0x124, 0x0)
    OP_21()
    Sleep(300)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x10E)
    OP_22(0x132, 0x0, 0x64)
    Sleep(500)
    OP_73(0x2)

    def lambda_2F66():
        OP_8E(0xFE, 0xEE48, 0x0, 0xFFFD3EEC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x124, 1, lambda_2F66)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/C5401   ._SN", 125, 0, 0)
    IdleLoop()
    OP_64(0x4, 0x1)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_18_2E8A end

    def Function_19_2FA0(): pass

    label("Function_19_2FA0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3035")
    EventBegin(0x1)

    ChrTalk(    #99
        0x124,
        (
            "#124F...I've got no reason to go any further this way.\x02\x03",

            "#120FI should head to the cathedral.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x124, 180, 400)
    OP_90(0x124, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_3035")

    label("loc_3035")

    Return()

    # Function_19_2FA0 end

    def Function_20_3036(): pass

    label("Function_20_3036")

    Return()

    # Function_20_3036 end

    def Function_21_3037(): pass

    label("Function_21_3037")

    Return()

    # Function_21_3037 end

    def Function_22_3038(): pass

    label("Function_22_3038")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(62950, 0, 50300, 0)
    OP_67(0, 4660, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x40)
    OP_4A(0x14, 255)
    SetChrPos(0x14, 61500, 0, 49000, 90)
    OP_24(0x131, 0x3C)
    Sleep(300)
    OP_24(0x85, 0x64)
    OP_24(0x131, 0x32)
    Sleep(300)
    OP_24(0x85, 0x5A)
    OP_24(0x131, 0x28)
    Sleep(300)
    OP_24(0x85, 0x50)
    OP_24(0x131, 0x1E)
    Sleep(300)
    OP_24(0x85, 0x46)
    OP_24(0x131, 0x14)
    Sleep(300)
    OP_23(0x131)

    def lambda_30FA():
        OP_6B(3200, 2000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_30FA)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #100
        0x14,
        (
            "#1224F#6PWh-What?!\x02\x03",

            "What's HAPPENING?!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrChipByIndex(0x14, 11)
    SetChrSubChip(0x14, 0)
    SetChrFlags(0x14, 0x2)

    def lambda_3159():
        OP_99(0xFE, 0x0, 0x2, 0x5DC)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_3159)
    WaitChrThread(0x14, 0x2)
    OP_22(0x8E, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    Sleep(400)
    SetChrSubChip(0x14, 3)
    Sleep(100)

    def lambda_3193():
        OP_99(0xFE, 0x0, 0x2, 0x5DC)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_3193)
    WaitChrThread(0x14, 0x2)
    OP_22(0x8E, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    Sleep(800)

    ChrTalk(    #101
        0x14,
        (
            "#1227F#6PI-I thought we were going to use that floating \x01",
            "city to rule Liberl!\x02\x03",

            "Then we were going to use it to rule the whole \x01",
            "CONTINENT!\x02\x03",

            "#1225FSo why is this happening? This wasn't supposed\x01",
            "to happen!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #102
        0x14,
        (
            "#1224F#6P...W-Wait...\x02\x03",

            "Did anyone ever actually say we were gonna\x01",
            "do that? Or was I just thinking it on my own? \x01",
            "...I was, wasn't I?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x14)
    Sleep(500)

    ChrTalk(    #103
        0x14,
        "#1227F#3S#6PAaaaaargh!#2S\x02",
    )

    OP_7C(0x0, 0x96, 0xBB8, 0x12C)
    CloseMessageWindow()
    ClearChrFlags(0x14, 0x2)
    SetChrChipByIndex(0x14, 5)
    SetChrSubChip(0x14, 0)
    OP_8C(0x14, 315, 600)

    def lambda_339E():
        OP_6D(61460, 0, 54360, 1500)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_339E)

    def lambda_33B6():
        OP_8E(0xFE, 0xE9C0, 0x0, 0xC710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_33B6)
    WaitChrThread(0x14, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrFlags(0x14, 0x4)
    SetChrPos(0x19, 59840, 0, 53000, 0)

    def lambda_33F1():
        OP_96(0xFE, 0xE9C0, 0x2BC, 0xCEA4, 0x320, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_33F1)
    WaitChrThread(0x14, 0x1)
    OP_8C(0x14, 180, 500)
    Fade(250)
    SetChrFlags(0x14, 0x2)
    SetChrFlags(0x14, 0x800)
    SetChrChipByIndex(0x14, 10)
    SetChrSubChip(0x14, 8)
    Sleep(500)
    OP_99(0x14, 0x8, 0x6, 0x5DC)
    Sleep(300)

    def lambda_3447():
        OP_9E(0xFE, 0xF, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_3447)
    Sleep(1000)

    NpcTalk(    #104
        0x19,
        "Gilbert",
        (
            "#1228F#5P#30WI hate my life...\x02\x03",

            "All I seem to do is get humiliated by THEM\x01",
            "and abused by Lord Campanella lately...\x02\x03",

            "A-And then to top it all off, THIS happens?!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)

    NpcTalk(    #105 op#A op#5
        0x19,
        "Gilbert",
        "#1224F#5P#20AI... I...\x05\x02",
    )

    CloseMessageWindow()

    def lambda_353E():
        OP_6B(3000, 4000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_353E)
    FadeToDark(3000, 0, -1)
    Sleep(1500)

    NpcTalk(    #106 op#A
        0x19,
        "Gilbert",
        "#1227F#5P#45A#3SJust what have we all been doing?!#2S\x02",
    )

    OP_7C(0x0, 0x96, 0xBB8, 0x12C)
    CloseMessageWindow()
    Sleep(1000)
    OP_0D()
    OP_44(0x19, 0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMapFlags(0x2000000)
    SetMapFlags(0x100000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/C5400   ._SN", 125, 0, 0)
    IdleLoop()
    Return()

    # Function_22_3038 end

    def Function_23_35D5(): pass

    label("Function_23_35D5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(2000)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(71210, 0, -233330, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(3800, 0)
    OP_6C(53000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x16, 0x40)
    SetChrFlags(0x17, 0x40)
    OP_4A(0x16, 255)
    OP_4A(0x17, 255)
    SetChrPos(0x16, 59760, 0, -186600, 180)
    SetChrPos(0x17, 62240, 0, -186600, 180)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 72500, 0, -234000, 270)
    FadeToBright(1500, 0)
    OP_0D()
    OP_22(0xE, 0x0, 0x64)
    Sleep(1000)
    OP_72(0x101A, 0x0)
    ExitThread()
    OP_70(0x1A, 0xF)
    OP_73(0x1A)
    Sleep(500)

    def lambda_36BA():
        OP_8E(0xFE, 0xFDE8, 0x0, 0xFFFC6DF0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_36BA)
    Sleep(1000)

    def lambda_36DA():
        OP_6D(62100, -200, -216040, 10000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_36DA)

    def lambda_36F2():
        OP_67(0, 3500, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_36F2)

    def lambda_370A():
        OP_6C(30000, 10000)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_370A)

    def lambda_371A():
        OP_6B(3200, 10000)
        ExitThread()

    QueueWorkItem(0x19, 3, lambda_371A)

    def lambda_372A():
        OP_6E(434, 10000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_372A)
    WaitChrThread(0x15, 0x1)

    def lambda_373F():
        OP_8E(0xFE, 0xEE48, 0x0, 0xFFFC7D90, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_373F)
    WaitChrThread(0x15, 0x1)

    def lambda_375F():
        OP_8E(0xFE, 0xEE48, 0x0, 0xFFFD1E6C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_375F)
    WaitChrThread(0x19, 0x0)
    Fade(500)
    OP_6D(62290, 0, -184300, 0)
    OP_67(0, 4660, -10000, 0)
    OP_6B(3440, 0)
    OP_6C(35000, 0)
    OP_6E(262, 0)
    OP_44(0x15, 0x1)
    OP_0D()
    Sleep(500)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #107
        0x16,
        "#5PL-Lord Campanella!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x17,
        "#5PI-I'm relieved to see you're well, sir!\x02",
    )

    CloseMessageWindow()

    def lambda_384E():
        OP_6D(62170, 0, -185780, 2000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_384E)
    SetChrPos(0x15, 61000, 0, -196000, 0)

    def lambda_3877():
        OP_8E(0xFE, 0xEE48, 0x0, 0xFFFD19D0, 0x8FC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3877)

    def lambda_3892():

        label("loc_3892")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_3892")

    QueueWorkItem2(0x16, 2, lambda_3892)

    def lambda_38A3():

        label("loc_38A3")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_38A3")

    QueueWorkItem2(0x17, 2, lambda_38A3)
    WaitChrThread(0x15, 0x1)
    Sleep(500)

    ChrTalk(    #109
        0x15,
        (
            "#853F#6PHeehee. The same to you fine gentlemen.\x02\x03",

            "#850FI'm thoroughly impressed with your work\x01",
            "ethic. It takes guts to dedicate yourselves\x01",
            "to your duty even at a time like this.\x02\x03",

            "#851FYou should see what's happening outside!\x01",
            "It's a sight to see, you know?\x02\x03",

            "All the mira in the world couldn't buy you\x01",
            "tickets to see a show this incredible.\x02\x03",

            "#854FYou're not too late to check out the show if\x01",
            "you head out now. Why not go take a peek?\x01",
            "I won't tattle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x16,
        "#5PW-We couldn't possibly!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x17,
        (
            "#5PWe wouldn't dream of abandoning our posts\x01",
            "without permission!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x15,
        (
            "#853F#6PHaha... I suppose you wouldn't after the training\x01",
            "you've been through.\x02\x03",

            "#850FWell, no matter. Now, mind letting me inside?\x02\x03",

            "I've got something I need to take care of in the \x01",
            "sanctuary, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x17,
        "#5P...Sir?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x16,
        (
            "#5PB-But #5Pwe've been ordered not to let anyone\x01",
            "inside without the professor's permission...\x01",
            "Even you, Lord Campanella.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x15,
        (
            "#853F#6PHe's as dead as you'll be if won't let me\x01",
            "through. I don't think even I can get a dead\x01",
            "man's permission, now, can I?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #116
        0x16,
        "#5PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x17,
        "#5PB-But that's just not possible...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x15,
        (
            "#852F#6POh, dear! Is my word worth that little to you?\x02\x03",

            "#855FI'm hurt.\x02\x03",

            "#854FMaybe I should have a little fun with you like \x01",
            "I always do with darling Gilbert.\x02\x03",

            "That might make you a liiittle more inclined to\x01",
            "have more faith in me.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x16, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_3E80():
        OP_8F(0xFE, 0xE970, 0x0, 0xFFFD2844, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3E80)
    Sleep(100)

    def lambda_3EA0():
        OP_8F(0xFE, 0xF320, 0x0, 0xFFFD2844, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3EA0)
    WaitChrThread(0x16, 0x1)
    WaitChrThread(0x17, 0x1)
    Sleep(300)

    ChrTalk(    #119
        0x16,
        "#5PI... We weren't...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x17,
        (
            "#5PWe never once doubted your word, so you need\x01",
            "not trouble yourself on our behalf!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x15,
        (
            "#853F#6PThat's lovely to hear. Well, then, why don't you \x01",
            "go outside and watch the show like I suggested?\x02\x03",

            "#854FYou're under no obligation to guard this place now\x01",
            "that the man who ordered you to do so is no more.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #122
        0x16,
        "#5P#3SGladly, sir!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #123
        0x17,
        "#5P#3SG-Good luck with your business, sir!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x16, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_44(0x16, 0x2)

    def lambda_40A2():
        OP_6D(62170, 0, -192000, 4000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_40A2)
    OP_43(0x16, 0x0, 0x0, 0x18)
    Sleep(300)
    OP_62(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_44(0x17, 0x2)
    OP_43(0x17, 0x1, 0x0, 0x18)

    def lambda_40E3():
        OP_8C(0xFE, 180, 300)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_40E3)
    WaitChrThread(0x17, 0x1)
    WaitChrThread(0x19, 0x0)
    Sleep(1000)

    def lambda_4100():
        OP_6D(62160, 0, -188230, 2000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_4100)
    WaitChrThread(0x19, 0x0)
    Sleep(500)

    ChrTalk(    #124
        0x15,
        (
            "#853F#5PThey may have served their purpose now,\x01",
            "but it seems a terrible waste to steal their\x01",
            "memories and toss them out like garbage. \x02\x03",

            "#854FMaybe I should put them under my command.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x15, 0, 400)
    Sleep(300)

    def lambda_41EA():
        OP_6D(62160, 0, -186230, 2000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_41EA)

    def lambda_4202():
        OP_8E(0xFE, 0xEE48, 0x0, 0xFFFD27F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4202)
    WaitChrThread(0x15, 0x1)
    WaitChrThread(0x19, 0x0)
    Fade(500)
    SetChrPos(0x15, 61000, 0, -185610, 0)
    OP_6D(61000, 500, -184400, 0)
    OP_67(0, 5000, -10000, 0)
    OP_6B(3220, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x10E)
    OP_22(0x132, 0x0, 0x64)
    Sleep(500)
    OP_73(0x2)

    def lambda_429B():
        OP_8E(0xFE, 0xEE48, 0x0, 0xFFFD3EEC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_429B)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_24(0x85, 0x3C)
    Sleep(400)
    OP_24(0x85, 0x37)
    Sleep(400)
    OP_24(0x85, 0x32)
    Sleep(400)
    OP_24(0x85, 0x2D)
    Sleep(400)
    OP_24(0x85, 0x28)
    Sleep(400)
    OP_24(0x85, 0x23)
    Sleep(400)
    OP_24(0x85, 0x1E)
    Sleep(400)
    OP_24(0x85, 0x19)
    Sleep(400)
    OP_24(0x85, 0x14)
    Sleep(400)
    OP_24(0x85, 0xF)
    Sleep(400)
    OP_24(0x85, 0xA)
    Sleep(400)
    OP_23(0x85)
    Sleep(500)
    OP_A2(0x2504)
    NewScene("ED6_DT21/C5401   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_23_35D5 end

    def Function_24_4337(): pass

    label("Function_24_4337")

    OP_8E(0xFE, 0xE6A0, 0x0, 0xFFFD1C14, 0x1770, 0x0)
    OP_8E(0xFE, 0xE6A0, 0x0, 0xFFFCE3E8, 0x1770, 0x0)
    Return()

    # Function_24_4337 end

    SaveToFile()

Try(main)
