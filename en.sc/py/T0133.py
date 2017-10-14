from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0133   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0133.x',
        MapIndex            = 10,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0133_1 ._SN',
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
        'Paddington',                           # 9
        'Melders',                              # 10
        'Anton',                                # 11
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
        'ED6_DT07/CH01250 ._CH',             # 00
        'ED6_DT07/CH01250 ._CH',             # 01
        'ED6_DT07/CH01250 ._CH',             # 02
        'ED6_DT07/CH01250 ._CH',             # 03
        'ED6_DT07/CH01250 ._CH',             # 04
        'ED6_DT07/CH01250 ._CH',             # 05
        'ED6_DT07/CH01250 ._CH',             # 06
        'ED6_DT07/CH01250 ._CH',             # 07
        'ED6_DT07/CH01250 ._CH',             # 08
        'ED6_DT07/CH01250 ._CH',             # 09
        'ED6_DT07/CH01250 ._CH',             # 0A
        'ED6_DT07/CH01250 ._CH',             # 0B
        'ED6_DT07/CH01250 ._CH',             # 0C
        'ED6_DT07/CH01250 ._CH',             # 0D
        'ED6_DT07/CH01250 ._CH',             # 0E
        'ED6_DT07/CH01250 ._CH',             # 0F
        'ED6_DT07/CH01250 ._CH',             # 10
        'ED6_DT07/CH01000 ._CH',             # 11
        'ED6_DT07/CH01040 ._CH',             # 12
        'ED6_DT07/CH01044 ._CH',             # 13
    )

    AddCharChipPat(
        'ED6_DT07/CH01250P._CP',             # 00
        'ED6_DT07/CH01250P._CP',             # 01
        'ED6_DT07/CH01250P._CP',             # 02
        'ED6_DT07/CH01250P._CP',             # 03
        'ED6_DT07/CH01250P._CP',             # 04
        'ED6_DT07/CH01250P._CP',             # 05
        'ED6_DT07/CH01250P._CP',             # 06
        'ED6_DT07/CH01250P._CP',             # 07
        'ED6_DT07/CH01250P._CP',             # 08
        'ED6_DT07/CH01250P._CP',             # 09
        'ED6_DT07/CH01250P._CP',             # 0A
        'ED6_DT07/CH01250P._CP',             # 0B
        'ED6_DT07/CH01250P._CP',             # 0C
        'ED6_DT07/CH01250P._CP',             # 0D
        'ED6_DT07/CH01250P._CP',             # 0E
        'ED6_DT07/CH01250P._CP',             # 0F
        'ED6_DT07/CH01250P._CP',             # 10
        'ED6_DT07/CH01000P._CP',             # 11
        'ED6_DT07/CH01040P._CP',             # 12
        'ED6_DT07/CH01044P._CP',             # 13
    )

    DeclNpc(
        X                   = 3275,
        Z                   = 0,
        Y                   = 2522,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 3290,
        Z                   = 0,
        Y                   = 3300,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 55210,
        Z                   = 10300,
        Y                   = 44150,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )


    DeclActor(
        TriggerX            = -300,
        TriggerZ            = 0,
        TriggerY            = 4140,
        TriggerRange        = 800,
        ActorX              = -300,
        ActorZ              = 1000,
        ActorY              = 4140,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 53450,
        TriggerZ            = 10300,
        TriggerY            = 47970,
        TriggerRange        = 800,
        ActorX              = 53450,
        ActorZ              = 10000,
        ActorY              = 47970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 51520,
        TriggerZ            = 10300,
        TriggerY            = 46970,
        TriggerRange        = 1700,
        ActorX              = 51520,
        ActorZ              = 11300,
        ActorY              = 46970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_216",          # 00, 0
        "Function_1_2B7",          # 01, 1
        "Function_2_37B",          # 02, 2
        "Function_3_4F8",          # 03, 3
        "Function_4_C9E",          # 04, 4
        "Function_5_FB7",          # 05, 5
        "Function_6_1378",         # 06, 6
        "Function_7_14D2",         # 07, 7
        "Function_8_1500",         # 08, 8
        "Function_9_150A",         # 09, 9
    )


    def Function_0_216(): pass

    label("Function_0_216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_25D")
    SetChrPos(0x8, 55710, 10300, 47580, 270)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 54840, 10300, 46250, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24F")
    Jump("loc_25A")

    label("loc_24F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25A")
    Jump("loc_25A")

    label("loc_25A")

    Jump("loc_2B6")

    label("loc_25D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_27F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27C")
    ClearChrFlags(0xA, 0x80)

    label("loc_27C")

    Jump("loc_2B6")

    label("loc_27F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_289")
    Jump("loc_2B6")

    label("loc_289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_29A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_297")

    label("loc_297")

    Jump("loc_2B6")

    label("loc_29A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_2B1")
    SetChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AE")

    label("loc_2AE")

    Jump("loc_2B6")

    label("loc_2B1")

    SetChrFlags(0x8, 0x10)

    label("loc_2B6")

    Return()

    # Function_0_216 end

    def Function_1_2B7(): pass

    label("Function_1_2B7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_303")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_2EE")
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xEA60, 0x0)
    Jump("loc_303")

    label("loc_2EE")

    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0x13880, 0x0)

    label("loc_303")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31B")
    OP_B1("t0133_n")
    Jump("loc_358")

    label("loc_31B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_34F")
    OP_B1("t0133_y")
    OP_11(0xDB, 0xB7, 0xFF, 0x0, 0xFF78, 0x0)
    Jump("loc_358")

    label("loc_34F")

    OP_B1("t0133_n")

    label("loc_358")

    Jump("loc_369")

    label("loc_35B")

    OP_B1("t0133_n")
    ClearMapFlags(0x10)

    label("loc_369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_375")
    OP_64(0x2, 0x1)

    label("loc_375")

    OP_E8(0xDC, 0x5, 0x0, 0x0)
    Return()

    # Function_1_2B7 end

    def Function_2_37B(): pass

    label("Function_2_37B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A0")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_4E2")

    label("loc_3A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B9")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_4E2")

    label("loc_3B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D2")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_4E2")

    label("loc_3D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EB")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_4E2")

    label("loc_3EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_404")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_4E2")

    label("loc_404")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41D")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_4E2")

    label("loc_41D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_436")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_4E2")

    label("loc_436")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44F")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_4E2")

    label("loc_44F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_468")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_4E2")

    label("loc_468")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_481")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_4E2")

    label("loc_481")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49A")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_4E2")

    label("loc_49A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B3")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_4E2")

    label("loc_4B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CC")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_4E2")

    label("loc_4CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E2")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_4E2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4F7")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_4E2")

    label("loc_4F7")

    Return()

    # Function_2_37B end

    def Function_3_4F8(): pass

    label("Function_3_4F8")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_6AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x413, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_511")
    Call(0, 5)
    Jump("loc_6A7")

    label("loc_511")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_591")

    ChrTalk(    #0
        0xFE,
        "Nice to see you've all come back here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Don't just work all the time, all right?\x01",
            "Relax, enjoy life a little.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A7")

    label("loc_591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_603")

    ChrTalk(    #2
        0xFE,
        (
            "Melders doesn't have a clue why\x01",
            "orbments aren't working either...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "This isn't looking good...\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A7")

    label("loc_603")


    ChrTalk(    #4
        0xFE,
        (
            "My clock stopped at the same time\x01",
            "that strange thing appeared in the sky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "I can't imagine it's just a coincidence.\x01",
            "There must be some kind of connection.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A7")

    Jump("loc_C9A")

    label("loc_6AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_8DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_771")

    ChrTalk(    #6
        0xFE,
        (
            "Hmm, can't say I remember that\x01",
            "particular dish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "You might have more luck asking\x01",
            "the old ladies in town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "If they're around my age, they\x01",
            "might've made it at least once.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D9")

    label("loc_771")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x100)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_79C")
    Call(1, 0)
    Jump("loc_8D9")

    label("loc_79C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_81A")

    ChrTalk(    #9
        0xFE,
        "Seems that little brat Luke's gotten better.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "I can hear his voice clear across the\x01",
            "way as he runs around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D9")

    label("loc_81A")


    ChrTalk(    #11
        0xFE,
        "Seems that little brat Luke's gotten better.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "I can hear his voice clear across the\x01",
            "way as he runs around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "Haha. Rolent looks beautiful as ever\x01",
            "under the bright shining sun.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_8D9")

    Jump("loc_C9A")

    label("loc_8DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_A4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_985")

    ChrTalk(    #14
        0xFE,
        (
            "The non-aggression pact with the\x01",
            "Empire is a new step for Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "I should offer prayers for the souls of\x01",
            "those lost in the Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A4C")

    label("loc_985")


    ChrTalk(    #16
        0xFE,
        (
            "Right. Today's the signing ceremony,\x01",
            "as I recall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "This historic day shall be a new\x01",
            "milestone for Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "I should offer prayers for the souls of\x01",
            "those lost in the Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_A4C")

    Jump("loc_C9A")

    label("loc_A4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_B83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AC2")

    ChrTalk(    #19
        0xFE,
        (
            "The toll of the clock tower's bell\x01",
            "sounds muffled, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "All because of this darned fog!\x02",
    )

    CloseMessageWindow()
    Jump("loc_B80")

    label("loc_AC2")


    ChrTalk(    #21
        0xFE,
        "The fog's thick as milk again today, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "Don't know if it's my imagination or not,\x01",
            "but the clock tower bell's chime is getting\x01",
            "worse and worse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "It's all muffled sounding.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_B80")

    Jump("loc_C9A")

    label("loc_B83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_C9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C0F")

    ChrTalk(    #24
        0xFE,
        (
            "It's another peaceful day with not\x01",
            "a single worry in sight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "I certainly hope the days of war are\x01",
            "long behind us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C9A")

    label("loc_C0F")


    ChrTalk(    #26
        0xFE,
        "Ahhh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "It's another peaceful day with not\x01",
            "a single worry in sight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "I certainly hope the days of war are\x01",
            "long behind us.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_C9A")

    TalkEnd(0x8)
    Return()

    # Function_3_4F8 end

    def Function_4_C9E(): pass

    label("Function_4_C9E")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x413, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB0")
    Call(0, 5)
    Jump("loc_FB3")

    label("loc_CB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_D4C")

    ChrTalk(    #29
        0xFE,
        (
            "Still, why have all the orbments\x01",
            "stopped all of a sudden?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 270, 400)

    ChrTalk(    #30
        0xFE,
        (
            "That strange island up there must be\x01",
            "pulling some kind of nasty trick.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB3")

    label("loc_D4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E14")

    ChrTalk(    #31
        0xFE,
        (
            "I have absolutely no idea why all the\x01",
            "orbments suddenly stopped working.\x01",
            "I confess, I'm completely baffled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "That strange island up there must be\x01",
            "pulling some kind of nasty trick.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB3")

    label("loc_E14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F48")

    ChrTalk(    #33
        0xFE,
        (
            "Recently, I went up the clock tower to\x01",
            "have a look at that floating island, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "I still feel like I haven't managed to\x01",
            "pull my jaw from the floor since I saw\x01",
            "the damn thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "Ever since that thing appeared, all the\x01",
            "orbments stopped working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        "Pretty ominous, if you ask me.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_FB3")

    label("loc_F48")


    ChrTalk(    #37
        0xFE,
        (
            "Ever since that thing appeared, all the\x01",
            "orbments stopped working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "Pretty ominous, if you ask me.\x02",
    )

    CloseMessageWindow()

    label("loc_FB3")

    TalkEnd(0x9)
    Return()

    # Function_4_C9E end

    def Function_5_FB7(): pass

    label("Function_5_FB7")

    OP_4A(0x9, 255)
    OP_4A(0x8, 255)
    TurnDirection(0x9, 0x101, 400)
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #39
        0x9,
        "Oh, hello there, Estelle.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(    #40
        0x9,
        "And Joshua's here, too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        (
            "Haha. Been quite a long time,\x01",
            "young man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x102,
        (
            "#1040FI'm glad to see you two are the\x01",
            "same as always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x9,
        "Yep, same old, same old.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x9,
        (
            "This city's got a lot of old machines.\x01",
            "As always, I've got my hands full\x01",
            "running around workin' on 'em.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x8,
        (
            "Mmm, as he said, those old doodads\x01",
            "are always breaking down. He's having\x01",
            "a look at the clock tower for me now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        "Darned thing's stopped running!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#1004FOh, yeah. Totally forgot about the\x01",
            "clock tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x102,
        "#1035FThe clock itself is an orbment, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x9,
        (
            "Yep. All the orbments in town have\x01",
            "stopped working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x9,
        (
            "Well, it might be fruitless, but I figured\x01",
            "I could at least oil the parts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        "You all should hurry home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        (
            "Don't just work all the time, and\x01",
            "don't forget to enjoy your stay while\x01",
            "you're here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #53
        0x102,
        "#1040FHaha, yes...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #54
        0x101,
        "#1001FYeah, we'll take it easy.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2099)
    OP_4B(0x9, 255)
    OP_4B(0x8, 255)
    OP_8C(0x9, 180, 0)
    OP_8C(0x8, 135, 0)
    OP_A2(0x1)
    OP_A2(0x3)
    Return()

    # Function_5_FB7 end

    def Function_6_1378(): pass

    label("Function_6_1378")

    OP_EA(0x1, 0x5, 0x0, 0x0)
    TalkBegin(0xA)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_1460")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Talk\x01",        # 0
            "Report\x01",      # 1
            "Leave\x01",       # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1449")

    ChrTalk(    #55
        0xFE,
        "Oh, Goddess, I beseech thee!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "May these bracers safely find\x01",
            "the ingredients for the medicine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_145D")

    label("loc_1449")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_145D")
    Call(1, 4)
    Jump("loc_145D")

    label("loc_145D")

    Jump("loc_14CE")

    label("loc_1460")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1483")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_147C")
    Call(1, 2)
    Jump("loc_1480")

    label("loc_147C")

    Call(1, 1)

    label("loc_1480")

    Jump("loc_14CE")

    label("loc_1483")


    ChrTalk(    #57
        0xFE,
        "Oh, Goddess, I beseech thee!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "May I get close to that hot lady...\x02",
    )

    CloseMessageWindow()

    label("loc_14CE")

    TalkEnd(0xA)
    Return()

    # Function_6_1378 end

    def Function_7_14D2(): pass

    label("Function_7_14D2")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x2400D1, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    Sleep(500)
    OP_A2(0x20EA)
    TalkEnd(0xFF)
    Return()

    # Function_7_14D2 end

    def Function_8_1500(): pass

    label("Function_8_1500")

    NewScene("ED6_DT21/T0133   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_8_1500 end

    def Function_9_150A(): pass

    label("Function_9_150A")

    NewScene("ED6_DT21/T0133   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_9_150A end

    SaveToFile()

Try(main)
