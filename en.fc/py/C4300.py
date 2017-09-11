from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C4300   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4300.x',
        MapIndex            = 216,
        MapDefaultBGM       = "ed60035",
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
        'Agate',                                # 12
        'Tita',                                 # 13
        'Zin',                                  # 14
        'Professor Russell',                    # 15
        'Sieg',                                 # 16
        'Special Ops Soldier',                  # 17
        'Special Ops Soldier',                  # 18
        'Special Ops Soldier',                  # 19
        'Special Ops Soldier',                  # 20
        'Special Ops Soldier',                  # 21
        'Special Ops Soldier',                  # 22
        'Special Ops Soldier',                  # 23
        'Special Ops Soldier',                  # 24
        'Special Ops Soldier',                  # 25
        'Colonel Richard',                      # 26
        '2nd Lieutenant Lorence',               # 27
        'Mech',                                 # 28
        'Mech',                                 # 29
        'Cassius',                              # 30
        'Cassius',                              # 31
        'Cassius',                              # 32
        'Cassius',                              # 33
        'Cassius',                              # 34
        'Cassius',                              # 35
        'Cassius',                              # 36
        'Cassius',                              # 37
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
        'ED6_DT06/CH20053 ._CH',             # 03
        'ED6_DT07/CH00060 ._CH',             # 04
        'ED6_DT07/CH00070 ._CH',             # 05
        'ED6_DT07/CH02020 ._CH',             # 06
        'ED6_DT07/CH02320 ._CH',             # 07
        'ED6_DT07/CH02030 ._CH',             # 08
        'ED6_DT07/CH02200 ._CH',             # 09
        'ED6_DT07/CH01610 ._CH',             # 0A
        'ED6_DT09/CH10941 ._CH',             # 0B
        'ED6_DT09/CH10940 ._CH',             # 0C
        'ED6_DT07/CH00260 ._CH',             # 0D
        'ED6_DT07/CH00262 ._CH',             # 0E
        'ED6_DT07/CH00270 ._CH',             # 0F
        'ED6_DT07/CH00272 ._CH',             # 10
        'ED6_DT06/CH20051 ._CH',             # 11
    )

    AddCharChipPat(
        'ED6_DT07/CH00020P._CP',             # 00
        'ED6_DT07/CH00030P._CP',             # 01
        'ED6_DT07/CH00040P._CP',             # 02
        'ED6_DT06/CH20053P._CP',             # 03
        'ED6_DT07/CH00060P._CP',             # 04
        'ED6_DT07/CH00070P._CP',             # 05
        'ED6_DT07/CH02020P._CP',             # 06
        'ED6_DT07/CH02320P._CP',             # 07
        'ED6_DT07/CH02030P._CP',             # 08
        'ED6_DT07/CH02200P._CP',             # 09
        'ED6_DT07/CH01610P._CP',             # 0A
        'ED6_DT09/CH10941P._CP',             # 0B
        'ED6_DT09/CH10940P._CP',             # 0C
        'ED6_DT07/CH00260P._CP',             # 0D
        'ED6_DT07/CH00262P._CP',             # 0E
        'ED6_DT07/CH00270P._CP',             # 0F
        'ED6_DT07/CH00272P._CP',             # 10
        'ED6_DT06/CH20051P._CP',             # 11
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
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
        TalkScenaIndex      = 8,
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
        TalkScenaIndex      = 9,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 38290,
        TriggerZ            = 0,
        TriggerY            = -3310,
        TriggerRange        = 1000,
        ActorX              = 38290,
        ActorZ              = 1200,
        ActorY              = -3310,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_4FE",          # 00, 0
        "Function_1_54A",          # 01, 1
        "Function_2_594",          # 02, 2
        "Function_3_5AA",          # 03, 3
        "Function_4_65F",          # 04, 4
        "Function_5_735",          # 05, 5
        "Function_6_7CF",          # 06, 6
        "Function_7_85F",          # 07, 7
        "Function_8_8DE",          # 08, 8
        "Function_9_93D",          # 09, 9
        "Function_10_AF3",         # 0A, 10
        "Function_11_B39",         # 0B, 11
        "Function_12_B5C",         # 0C, 12
        "Function_13_19E2",        # 0D, 13
        "Function_14_1A74",        # 0E, 14
        "Function_15_1B10",        # 0F, 15
        "Function_16_1B8D",        # 10, 16
        "Function_17_2D24",        # 11, 17
        "Function_18_3362",        # 12, 18
        "Function_19_3481",        # 13, 19
    )


    def Function_0_4FE(): pass

    label("Function_0_4FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_515")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 12)

    label("loc_515")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_528")
    SetMapFlags(0x40000000)
    OP_A3(0x3FB)
    Event(0, 16)

    label("loc_528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_538")
    Call(0, 18)

    label("loc_538")

    OP_51(0xF, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_4FE end

    def Function_1_54A(): pass

    label("Function_1_54A")

    LoadEffect(0x5, "map\\\\mp027_00.eff")
    PlayEffect(0x5, 0x6, 0xFF, 38290, 1200, -3310, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_1_54A end

    def Function_2_594(): pass

    label("Function_2_594")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5A9")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_594")

    label("loc_5A9")

    Return()

    # Function_2_594 end

    def Function_3_5AA(): pass

    label("Function_3_5AA")

    TalkBegin(0x8)

    ChrTalk(    #0
        0x8,
        (
            "#022FSo, what is this 'Aureole' thing the\x01",
            "colonel's so thoroughly seeking?\x02\x03",

            "Doesn't SEEM all that desirable.\x01",
            "I mean, I sure as hell wouldn't\x01",
            "want the thing in MY house!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Return()

    # Function_3_5AA end

    def Function_4_65F(): pass

    label("Function_4_65F")

    TalkBegin(0x9)

    ChrTalk(    #1
        0x9,
        (
            "#035FI learned long ago that deals\x01",
            "made underground are never\x01",
            "fair, just or...healthy...\x02\x03",

            "#030FI daresay we should catch up to the\x01",
            "colonel and call him out--bring the\x01",
            "final curtain down on all of this.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Return()

    # Function_4_65F end

    def Function_5_735(): pass

    label("Function_5_735")

    TalkBegin(0xA)

    ChrTalk(    #2
        0xA,
        (
            "#042FMy grandmother should be fine.\x01",
            "Julia is with her.\x02\x03",

            "I just have to have faith that\x01",
            "those two will be safe, and face\x01",
            "what may come for me.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    # Function_5_735 end

    def Function_6_7CF(): pass

    label("Function_6_7CF")

    TalkBegin(0xB)

    ChrTalk(    #3
        0xB,
        (
            "#050FSo...any idea what route we're\x01",
            "taking?\x02\x03",

            "I want to catch that Colonel\x01",
            "Richard and lay some good, old\x01",
            "fashioned boot to his ass.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_6_7CF end

    def Function_7_85F(): pass

    label("Function_7_85F")

    TalkBegin(0xC)

    ChrTalk(    #4
        0xC,
        (
            "#063FEstelle... Joshua...\x02\x03",

            "Don't overdo it out there. If\x01",
            "things get too dangerous, you\x01",
            "come right back here, okay?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xC)
    Return()

    # Function_7_85F end

    def Function_8_8DE(): pass

    label("Function_8_8DE")

    TalkBegin(0xD)

    ChrTalk(    #5
        0xD,
        (
            "#070FZin the Immovable will make\x01",
            "sure everyone is safe here.\x02\x03",

            "You two go on ahead.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xD)
    Return()

    # Function_8_8DE end

    def Function_9_93D(): pass

    label("Function_9_93D")

    TalkBegin(0xE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                 # 0
            "Modify/Exchange\x01",      # 1
            "Buy\x01",                  # 2
            "Change Members\x01",       # 3
            "Leave\x01",                # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BC")
    Call(0, 10)
    OP_56(0x0)
    TalkEnd(0xE)
    Return()

    label("loc_9BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D6")
    Call(0, 11)
    OP_56(0x0)
    TalkEnd(0xE)
    Return()

    label("loc_9D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2A")
    EventBegin(0x0)
    OP_4A(0xE, 255)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    Call(0, 17)
    OP_4B(0xE, 255)
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    OP_4B(0xA, 255)
    OP_4B(0xB, 255)
    OP_4B(0xC, 255)
    OP_4B(0xD, 255)
    EventEnd(0x0)
    TalkEnd(0xE)
    Return()

    label("loc_A2A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A3B")
    TalkEnd(0xE)
    Return()

    label("loc_A3B")


    ChrTalk(    #6
        0xE,
        (
            "#100FJust talk to me if you need any\x01",
            "sort of orbment work done.\x02\x03",

            "I can even sell you tools, if you'd like.\x01",
            "Anything you could buy in the city's shops,\x01",
            "I can get for you here!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xE)
    Return()

    # Function_9_93D end

    def Function_10_AF3(): pass

    label("Function_10_AF3")


    ChrTalk(    #7
        0xE,
        (
            "#100FCome on, then. I'll fix those\x01",
            "up better than brand new!\x02",
        )
    )

    CloseMessageWindow()
    OP_0D()
    OP_A9(0x6A)
    Return()

    # Function_10_AF3 end

    def Function_11_B39(): pass

    label("Function_11_B39")


    ChrTalk(    #8
        0xE,
        "#100FWhat is it you need?\x02",
    )

    CloseMessageWindow()
    OP_0D()
    OP_A9(0x6B)
    Return()

    # Function_11_B39 end

    def Function_12_B5C(): pass

    label("Function_12_B5C")

    EventBegin(0x0)
    LoadEffect(0x0, "battle\\\\btbomb00.eff")
    FadeToBright(2000, 0)
    OP_6D(38000, 17050, -14020, 0)
    OP_67(0, 4150, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(418, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x19, 34660, 0, -13430, 270)
    SetChrPos(0x1A, 35900, 0, -15200, 270)
    SetChrPos(0x10, 36160, 0, -11160, 270)
    SetChrPos(0x11, 37460, 0, -14780, 270)
    SetChrPos(0x12, 37460, 0, -13340, 270)
    SetChrPos(0x13, 36220, 0, -17220, 270)
    SetChrPos(0x14, 37460, 0, -12070, 270)
    SetChrPos(0x15, 39500, 0, -13290, 270)
    SetChrPos(0x16, 39500, 0, -14730, 270)
    SetChrPos(0x17, 37460, 0, -16090, 270)
    FadeToBright(2000, 0)
    OP_6D(38000, 2550, -14020, 5000)

    ChrTalk(    #9
        0x10,
        "#5PWh-What is this place...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x11,
        (
            "#5PI never would have imagined that\x01",
            "something like this even existed...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D26():
        OP_6D(19210, 0, -13380, 3500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_D26)

    def lambda_D3E():
        OP_6C(135000, 6000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_D3E)
    Sleep(2000)

    def lambda_D53():
        OP_67(0, 10910, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_D53)

    def lambda_D6B():
        OP_6E(514, 4000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_D6B)
    Sleep(4000)
    Fade(1000)
    OP_6D(36830, 0, -13980, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(135000, 0)
    OP_6E(332, 0)
    OP_0D()

    ChrTalk(    #11
        0x19,
        (
            "#115F#5PHa ha...\x01",
            "It's larger than I expected.\x02\x03",

            "#110FLieutenant Lorence... If you'd\x01",
            "be so kind as to show us the\x01",
            "way to the lowest level?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x1A,
        "#281F#6PYes, sir...\x02",
    )

    CloseMessageWindow()
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1B, 0x4)
    SetChrFlags(0x1C, 0x4)
    SetChrPos(0x1B, 18010, 20220, 5070, 108)
    SetChrPos(0x1C, 16410, 20220, -120, 108)

    def lambda_EBC():

        label("loc_EBC")

        TurnDirection(0xFE, 0x1A, 0)
        OP_48()
        Jump("loc_EBC")

    QueueWorkItem2(0x1B, 3, lambda_EBC)

    def lambda_ECD():

        label("loc_ECD")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_ECD")

    QueueWorkItem2(0x1C, 3, lambda_ECD)
    ClearChrFlags(0x1B, 0x1)
    ClearChrFlags(0x1C, 0x1)

    def lambda_EE8():
        OP_8F(0xFE, 0x7A76, 0x0, 0xFFFFD03A, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_EE8)
    Sleep(300)

    def lambda_F08():
        OP_8F(0xFE, 0x79FE, 0x0, 0xFFFFC2C0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_F08)
    TurnDirection(0x1A, 0x1B, 400)

    def lambda_F2A():
        OP_6D(32409, 0, -13750, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_F2A)

    def lambda_F42():
        OP_6C(90000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_F42)

    def lambda_F52():
        OP_67(0, 7160, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_F52)
    OP_8E(0x1A, 0x869C, 0x0, 0xFFFFC482, 0x1388, 0x0)

    def lambda_F7E():

        label("loc_F7E")

        TurnDirection(0xFE, 0x1C, 0)
        OP_48()
        Jump("loc_F7E")

    QueueWorkItem2(0x1A, 1, lambda_F7E)

    def lambda_F8F():

        label("loc_F8F")

        TurnDirection(0xFE, 0x1B, 0)
        OP_48()
        Jump("loc_F8F")

    QueueWorkItem2(0x19, 1, lambda_F8F)
    SetChrChipByIndex(0x1A, 13)
    SetChrChipByIndex(0x19, 15)
    OP_22(0xE7, 0x0, 0x64)
    WaitChrThread(0x1B, 0x1)
    SetChrChipByIndex(0x1B, 12)
    SetChrFlags(0x1B, 0x1)
    SetChrFlags(0x1C, 0x1)

    def lambda_FC3():

        label("loc_FC3")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_FC3")

    QueueWorkItem2(0x1B, 0, lambda_FC3)
    TurnDirection(0x1B, 0x19, 0)
    WaitChrThread(0x1C, 0x1)
    SetChrChipByIndex(0x1C, 12)

    def lambda_FE7():

        label("loc_FE7")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_FE7")

    QueueWorkItem2(0x1C, 0, lambda_FE7)
    TurnDirection(0x1C, 0x1A, 0)
    TurnDirection(0x10, 0x1B, 0)
    TurnDirection(0x11, 0x1B, 0)
    TurnDirection(0x12, 0x1B, 0)
    TurnDirection(0x13, 0x1B, 0)
    TurnDirection(0x14, 0x1B, 0)
    TurnDirection(0x15, 0x1B, 0)
    TurnDirection(0x16, 0x1B, 0)
    TurnDirection(0x17, 0x1B, 0)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x16, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_10C9():
        OP_94(0x1, 0xFE, 0xB4, 0x44C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_10C9)

    def lambda_10DF():
        OP_94(0x1, 0xFE, 0xB4, 0x320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_10DF)
    Sleep(50)

    def lambda_10FA():
        OP_94(0x1, 0xFE, 0xB4, 0x2BC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_10FA)

    def lambda_1110():
        OP_94(0x1, 0xFE, 0xB4, 0x44C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1110)
    Sleep(100)

    def lambda_112B():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_112B)

    def lambda_1141():
        OP_94(0x1, 0xFE, 0xB4, 0x514, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1141)
    Sleep(50)

    def lambda_115C():
        OP_94(0x1, 0xFE, 0xB4, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_115C)
    Sleep(50)

    def lambda_1177():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_1177)
    WaitChrThread(0x0, 0x2)

    ChrTalk(    #13
        0x10,
        "Whoa...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x11,
        (
            "I-Is that some kind of\x01",
            "mechanical monster?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x19,
        (
            "#110F#6PWell, well...\x01",
            "So these must be 'archaisms.'\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1208():
        OP_6C(70000, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1208)
    OP_6B(2900, 1500)
    SetChrFlags(0x1A, 0x40)
    SetChrFlags(0x19, 0x40)

    def lambda_122B():
        OP_6D(30310, 0, -13620, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_122B)

    def lambda_1243():
        OP_6B(2500, 1000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_1243)

    def lambda_1253():
        OP_67(0, 5500, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1253)

    def lambda_126B():
        OP_6C(42000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_126B)
    OP_9F(0x1D, 0xFF, 0xC8, 0xC8, 0xC8, 0x0)
    OP_9F(0x1E, 0xFF, 0x96, 0x96, 0x96, 0x0)
    OP_9F(0x1F, 0xFF, 0x64, 0x64, 0x64, 0x0)
    OP_9F(0x20, 0xFF, 0x32, 0x32, 0x32, 0x0)
    OP_9F(0x21, 0xC8, 0xFF, 0xFF, 0xC8, 0x0)
    OP_9F(0x22, 0x96, 0xFF, 0xFF, 0x96, 0x0)
    OP_9F(0x23, 0x64, 0xFF, 0xFF, 0x64, 0x0)
    OP_9F(0x24, 0x32, 0xFF, 0xFF, 0x32, 0x0)
    OP_43(0x11, 0x0, 0x0, 0xD)
    Sleep(530)
    OP_22(0x1F5, 0x0, 0x64)
    PlayEffect(0x8, 0xFF, 0xFF, 31350, 1500, -12230, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_44(0x1B, 0xFF)
    Sleep(150)
    OP_22(0x1F8, 0x0, 0x64)
    PlayEffect(0x8, 0xFF, 0xFF, 31230, 1500, -15680, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_44(0x1C, 0xFF)
    Sleep(900)

    def lambda_1365():
        OP_6B(2900, 2000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_1365)

    def lambda_1375():
        OP_6C(19000, 2000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_1375)

    def lambda_1385():
        OP_67(0, 7160, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1385)

    def lambda_139D():
        OP_6D(30310, 0, -13620, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_139D)
    SetChrFlags(0x1B, 0x4)
    PlayEffect(0x0, 0xFF, 0x1B, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_13EF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_13EF)

    def lambda_1401():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_1401)
    Sleep(300)
    SetChrFlags(0x1C, 0x4)
    PlayEffect(0x0, 0xFF, 0x1C, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_145B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_145B)

    def lambda_146D():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_146D)
    Sleep(1500)

    def lambda_148D():
        OP_99(0xFE, 0x9, 0xB, 0x640)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_148D)

    def lambda_149D():
        OP_96(0xFE, 0x7AE4, 0x0, 0xFFFFC40A, 0x2BC, 0xFA0)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_149D)
    SetChrFlags(0x19, 0x800)

    def lambda_14C0():
        OP_99(0xFE, 0x5, 0xB, 0x7D0)
        ExitThread()

    QueueWorkItem(0x19, 3, lambda_14C0)
    WaitChrThread(0x19, 0x3)
    SetChrChipByIndex(0x19, 15)
    SetChrSubChip(0x19, 0)
    Sleep(500)

    ChrTalk(    #16
        0x10,
        "H-Holy shit...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x14,
        (
            "He took out that thing\x01",
            "in one stroke...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    SetChrFlags(0x19, 0x20)
    TurnDirection(0x19, 0x1A, 400)

    ChrTalk(    #18
        0x19,
        (
            "#111F#6PHa ha...\x01",
            "You were the quickest to react.\x02\x03",

            "You are, indeed, truly a force\x01",
            "to be reckoned with when you\x01",
            "don't hold back.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    SetChrFlags(0x1A, 0x20)
    TurnDirection(0x1A, 0x19, 400)

    def lambda_15CB():

        label("loc_15CB")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_15CB")

    QueueWorkItem2(0x1A, 3, lambda_15CB)

    ChrTalk(    #19
        0x1A,
        (
            "#280F#6PYou flatter me, sir.\x02\x03",

            "Your quick-draw technique, as well, was\x01",
            "quite remarkable to behold. I can see that\x01",
            "you've studied under the Divine Blade himself.\x02\x03",

            "I am humbled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x19,
        (
            "#115F#6PHa ha...\x01",
            "I still have a ways to go before I can\x01",
            "really humble anyone, I'm afraid.\x02\x03",

            "#116FBut...time waits for no man. The\x01",
            "skills I possess now will have to\x01",
            "be enough.\x02\x03",

            "My strength may be meager, but I must forge\x01",
            "this kingdom's future with my own two hands...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1A, 0)
    SetChrChipByIndex(0x1A, 9)
    ClearChrFlags(0x1A, 0x20)
    ClearChrFlags(0x1A, 0x800)

    def lambda_17B3():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_17B3)

    def lambda_17C3():
        OP_6D(35740, 0, -13960, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_17C3)
    ClearChrFlags(0x19, 0x20)
    ClearChrFlags(0x19, 0x800)
    SetChrChipByIndex(0x19, 8)
    OP_8E(0x19, 0x7B66, 0x0, 0xFFFFCBDA, 0x7D0, 0x0)
    OP_8C(0x19, 90, 400)
    WaitChrThread(0x0, 0x1)

    ChrTalk(    #21
        0x19,
        (
            "#114F#5PMy brave men! The way to the\x01",
            "ultimate power is open!\x02\x03",

            "A bright new dawn approaches\x01",
            "for our beloved Liberl!\x02\x03",

            "I expect only the best of each of you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x11,
        "#4PBy your order, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x12,
        (
            "#4PWe of the Special Ops will\x01",
            "work as one for the colonel!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    SetMessageWindowPos(40, 60, -1, -1)
    SetChrName("Special Ops Soldiers")

    AnonymousTalk(    #24
        "\x07\x00#3SFor the glory of Liberl!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    Sleep(400)
    SetMessageWindowPos(150, 100, -1, -1)
    SetChrName("Special Ops Soldiers")

    AnonymousTalk(    #25
        "\x07\x00#5SFor the glory of Liberl!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21()
    Sleep(2000)
    OP_22(0xD, 0x0, 0x64)
    Sleep(3000)
    SetMapFlags(0x100000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_B5C end

    def Function_13_19E2(): pass

    label("Function_13_19E2")

    OP_43(0x1A, 0x1, 0x0, 0xE)
    Sleep(70)
    OP_43(0x1D, 0x1, 0x0, 0xE)
    OP_43(0x19, 0x1, 0x0, 0xF)
    Sleep(70)
    OP_43(0x1E, 0x1, 0x0, 0xE)
    OP_43(0x21, 0x1, 0x0, 0xF)
    Sleep(70)
    OP_43(0x1F, 0x1, 0x0, 0xE)
    OP_43(0x22, 0x1, 0x0, 0xF)
    Sleep(70)
    OP_43(0x20, 0x1, 0x0, 0xE)
    OP_43(0x23, 0x1, 0x0, 0xF)
    Sleep(70)
    OP_43(0x24, 0x1, 0x0, 0xF)
    WaitChrThread(0x20, 0x1)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    WaitChrThread(0x24, 0x1)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    Return()

    # Function_13_19E2 end

    def Function_14_1A74(): pass

    label("Function_14_1A74")

    SetChrChipByIndex(0xFE, 13)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrPos(0xFE, 34460, 0, -15230, 270)

    def lambda_1A9A():

        label("loc_1A9A")

        TurnDirection(0xFE, 0x1C, 0)
        OP_48()
        Jump("loc_1A9A")

    QueueWorkItem2(0xFE, 3, lambda_1A9A)
    OP_96(0xFE, 0x8246, 0x0, 0xFFFFC31A, 0x3E8, 0x2328)
    OP_44(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 14)
    SetChrFlags(0xFE, 0x800)

    def lambda_1AD0():
        OP_99(0xFE, 0x0, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1AD0)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    OP_96(0xFE, 0x7F6B, 0x4B0, 0xFFFFC360, 0x4E2, 0x1388)
    OP_8F(0xFE, 0x7274, 0x96, 0xFFFFC41E, 0x32C8, 0x0)
    Return()

    # Function_14_1A74 end

    def Function_15_1B10(): pass

    label("Function_15_1B10")

    ClearChrFlags(0x1A, 0x800)
    SetChrChipByIndex(0xFE, 15)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrPos(0xFE, 34660, 0, -13430, 270)

    def lambda_1B3B():

        label("loc_1B3B")

        TurnDirection(0xFE, 0x1B, 0)
        OP_48()
        Jump("loc_1B3B")

    QueueWorkItem2(0xFE, 3, lambda_1B3B)
    OP_8F(0xFE, 0x8282, 0x0, 0xFFFFCFE0, 0x1388, 0x0)
    OP_44(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 16)
    SetChrFlags(0xFE, 0x800)

    def lambda_1B6E():
        OP_99(0xFE, 0x0, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_1B6E)
    OP_8E(0xFE, 0x70D0, 0x96, 0xFFFFD03A, 0x2AF8, 0x0)
    Return()

    # Function_15_1B10 end

    def Function_16_1B8D(): pass

    label("Function_16_1B8D")

    EventBegin(0x0)
    RemoveParty(0x4, 0xFF)
    RemoveParty(0x2, 0xFF)
    AddParty(0x1, 0xFF)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_4A(0xE, 255)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    SetChrPos(0x101, 37080, 0, -15050, 270)
    SetChrPos(0x102, 37170, 0, -12980, 270)
    SetChrPos(0xE, 38760, 0, -14790, 258)
    SetChrPos(0xB, 37850, 0, -16410, 222)
    SetChrPos(0xC, 39400, 0, -15590, 222)
    SetChrPos(0x9, 39020, 0, -12220, 293)
    SetChrPos(0x8, 39710, 0, -13330, 262)
    SetChrPos(0xD, 40420, 0, -14130, 260)
    SetChrPos(0xA, 38260, 0, -13640, 265)
    SetChrPos(0xF, 40960, 500, -20390, 314)
    OP_6D(80, 0, 35850, 0)
    OP_67(0, 9440, -34740, 0)
    OP_6B(1000, 0)
    OP_6C(0, 0)
    OP_6E(663, 0)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    FadeToBright(2000, 0)

    def lambda_1CF5():
        OP_6D(50, 0, -20330, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1CF5)
    Sleep(3000)

    def lambda_1D12():
        OP_6C(77000, 11000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1D12)
    Sleep(7000)

    def lambda_1D27():
        OP_6D(39590, 0, -14310, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D27)

    def lambda_1D3F():
        OP_67(0, 22340, -34740, 6000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1D3F)

    def lambda_1D57():
        OP_6E(343, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1D57)
    Sleep(6000)

    ChrTalk(    #26
        0x101,
        "#580FWh-What the heck...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x102,
        (
            "#5P#012FThey're ruins from the ancient\x01",
            "Zemurian civilization...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xE,
        (
            "#102F#6PAs old as these appear, I don't\x01",
            "get the feeling that this place\x01",
            "is completely dead...\x02\x03",

            "It seems to function just like\x01",
            "the equipment in the tetracyclic\x01",
            "towers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xB,
        (
            "#2P#057FThat ain't all that's moving.\x02\x03",

            "I get the feeling we've got\x01",
            "some pretty nasty creatures\x01",
            "around here, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xC,
        "#065F#4PW-Wow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "#022FThe structures nearby look to\x01",
            "be made of modern materials.\x02\x03",

            "I suppose Colonel Richard's had\x01",
            "some construction going on...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x9,
        (
            "#030FI suspect you're right.\x02\x03",

            "#035FBuilding anything at this depth\x01",
            "is rather impressive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xA,
        (
            "#043FThe ruins are even larger than\x01",
            "I'd suspected...\x02\x03",

            "If we're not careful, we could\x01",
            "get terribly lost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xD,
        (
            "#074FHmm...\x02\x03",

            "#072FIt may be best if we split up.\x01",
            "Two groups, one for scouting\x01",
            "and one to stay on standby.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_20C6():
        OP_6E(300, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_20C6)

    def lambda_20D6():
        OP_6C(90000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_20D6)

    def lambda_20E6():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_20E6)

    def lambda_20F4():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_20F4)
    Sleep(100)

    def lambda_2107():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2107)
    Sleep(100)

    def lambda_211A():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_211A)

    def lambda_2128():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2128)
    Sleep(100)

    def lambda_213B():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_213B)

    def lambda_2149():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2149)
    TurnDirection(0x102, 0xD, 400)
    TurnDirection(0x101, 0xD, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #35
        0x101,
        "#505FWhat do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x102,
        (
            "#010FBasically, we establish a base camp\x01",
            "of sorts in a secure location.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xD,
        (
            "#070FThat's the gist of it.\x02\x03",

            "The scouting party will find a way through,\x01",
            "and the ones on standby will be available\x01",
            "to switch out, as needed.\x02\x03",

            "Once the right path is found,\x01",
            "everyone moves forward to\x01",
            "establish a new base.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xB,
        "#051FMakes sense to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xE,
        (
            "#104F#6PIn that case, I believe that our\x01",
            "current location would be the\x01",
            "best place to start from.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 400)

    ChrTalk(    #40
        0xE,
        (
            "#100FEstelle and Joshua, you'll be\x01",
            "the ones to decide who's going\x01",
            "to be on which team.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_23B1():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_23B1)

    def lambda_23BF():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_23BF)

    def lambda_23CD():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_23CD)

    def lambda_23DB():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_23DB)

    def lambda_23E9():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_23E9)

    def lambda_23F7():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_23F7)

    def lambda_2405():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2405)
    Sleep(1000)

    ChrTalk(    #41
        0x101,
        "#004FWait, US?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x102,
        "#014FBut...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xE,
        (
            "#100F#6PYou two are at the very heart of\x01",
            "this operation.\x02\x03",

            "I doubt anyone will object.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        "#021FI agree.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xA,
        "#040FAs do I.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xC,
        "#560FI-I'll follow your lead...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xB,
        (
            "#2P#053FBah... Like I have a choice?\x01",
            "I'm in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        (
            "#035F#6PHeh... I have faith in you to\x01",
            "make the right choices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xD,
        "#070FSounds fine to me.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #50
        0x101,
        (
            "#505FJoshua...?\x01",
            "What do we do?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #51
        0x102,
        (
            "#010FNo need to think about\x01",
            "it too hard.\x02\x03",

            "If things get tough, we can\x01",
            "always turn back and switch\x01",
            "people out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        "#006FOh... Well, then...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Call(0, 17)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2658")
    OP_83(0x17, 0x0)

    label("loc_2658")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2674")
    OP_83(0x17, 0x0)

    label("loc_2674")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2690")
    OP_83(0x17, 0x0)

    label("loc_2690")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26AC")
    OP_83(0x18, 0x0)

    label("loc_26AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26C8")
    OP_83(0x18, 0x0)

    label("loc_26C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26E4")
    OP_83(0x18, 0x0)

    label("loc_26E4")

    SetChrFlags(0xF, 0x80)

    def lambda_26EF():
        TurnDirection(0xFE, 0xA, 0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_26EF)

    def lambda_26FD():
        TurnDirection(0xFE, 0xA, 0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_26FD)

    def lambda_270B():
        TurnDirection(0xFE, 0xA, 0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_270B)

    def lambda_2719():
        TurnDirection(0xFE, 0xA, 0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2719)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2838")
    SetChrPos(0xA, 36030, 0, -8640, 225)
    SetChrPos(0xF, 36210, 0, -9110, 225)
    SetChrChipByIndex(0xA, 17)
    SetChrSubChip(0xA, 1)
    OP_44(0xA, 0xFF)
    Sleep(1000)

    ChrTalk(    #53
        0xA,
        (
            "#040F#5PEstelle, I'm going to send\x01",
            "Sieg to accompany you.\x02\x03",

            "When you find a suitable spot\x01",
            "to use as a base, please send\x01",
            "him back.\x02\x03",

            "He'll be able to show us the\x01",
            "way to wherever you are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xF,
        "#310F#2PScree.\x02",
    )

    CloseMessageWindow()
    Jump("loc_296D")

    label("loc_2838")


    def lambda_283E():
        OP_8C(0xFE, 225, 0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_283E)
    SetChrPos(0x105, 36030, 0, -8640, 225)
    SetChrPos(0xF, 36210, 0, -9110, 225)
    SetChrChipByIndex(0x105, 17)
    SetChrSubChip(0x105, 1)
    Sleep(1000)

    ChrTalk(    #55
        0x105,
        (
            "#040F#5PWhen we find a suitable spot\x01",
            "to use as a base, I'll send\x01",
            "Sieg back here.\x02\x03",

            "He'll be able to show you the\x01",
            "way to wherever we are.\x02\x03",

            "Also, if I'm not in the scouting\x01",
            "party, I'll send Sieg along with\x01",
            "you guys instead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xF,
        "#310F#2PScree.\x02",
    )

    CloseMessageWindow()

    label("loc_296D")


    ChrTalk(    #57
        0x102,
        (
            "#010FAhh, good idea. That way, the\x01",
            "search party won't have to\x01",
            "backtrack to get the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        "#006FIt's up to you, Sieg!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xF,
        "#311F#2PScreee!\x02",
    )

    CloseMessageWindow()
    Fade(250)
    ClearChrFlags(0xF, 0x80)

    def lambda_2A12():

        label("loc_2A12")

        TurnDirection(0xFE, 0xF, 800)
        OP_48()
        Jump("loc_2A12")

    QueueWorkItem2(0x0, 1, lambda_2A12)

    def lambda_2A23():

        label("loc_2A23")

        TurnDirection(0xFE, 0xF, 800)
        OP_48()
        Jump("loc_2A23")

    QueueWorkItem2(0x1, 1, lambda_2A23)

    def lambda_2A34():

        label("loc_2A34")

        TurnDirection(0xFE, 0xF, 800)
        OP_48()
        Jump("loc_2A34")

    QueueWorkItem2(0x2, 1, lambda_2A34)

    def lambda_2A45():

        label("loc_2A45")

        TurnDirection(0xFE, 0xF, 800)
        OP_48()
        Jump("loc_2A45")

    QueueWorkItem2(0x3, 1, lambda_2A45)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A6B")
    SetChrFlags(0xA, 0x20)
    SetChrSubChip(0xA, 3)
    Jump("loc_2A79")

    label("loc_2A6B")

    OP_44(0x105, 0xFF)
    SetChrFlags(0x105, 0x20)
    SetChrSubChip(0x105, 3)

    label("loc_2A79")

    OP_22(0x8C, 0x0, 0x64)
    SetChrFlags(0xF, 0x40)
    SetChrFlags(0xF, 0x4)

    def lambda_2A8E():
        OP_8E(0xFE, 0x88FE, 0x7D0, 0xFFFFD7C4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2A8E)
    Sleep(100)

    def lambda_2AAE():
        OP_8E(0xFE, 0x88FE, 0x7D0, 0xFFFFD7C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2AAE)
    Sleep(100)

    def lambda_2ACE():
        OP_8E(0xFE, 0x88FE, 0x7D0, 0xFFFFD7C4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2ACE)
    Sleep(100)

    def lambda_2AEE():
        OP_8E(0xFE, 0x7B0C, 0x0, 0xFFFFCDA6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2AEE)

    def lambda_2B09():
        OP_6D(25620, 0, -12350, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2B09)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B40")
    SetChrChipByIndex(0xA, 2)
    ClearChrFlags(0xA, 0x20)
    SetChrSubChip(0xA, 0)
    Jump("loc_2B4F")

    label("loc_2B40")

    SetChrChipByIndex(0x105, 65535)
    ClearChrFlags(0x105, 0x20)
    SetChrSubChip(0x105, 0)

    label("loc_2B4F")


    def lambda_2B55():
        OP_8E(0xFE, 0x3016, 0x1388, 0xFFFFC720, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2B55)
    Sleep(2500)

    def lambda_2B75():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2B75)

    def lambda_2B83():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2B83)

    def lambda_2B91():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2B91)

    def lambda_2B9F():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2B9F)

    def lambda_2BAD():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2BAD)
    OP_6D(35010, 0, -7430, 2000)

    ChrTalk(    #60
        0xE,
        (
            "#102F#6PWell, that means we're counting\x01",
            "on you to handle the scouting.\x02\x03",

            "Just to be on the safe side, I've\x01",
            "prepared a complete set of tools.\x01",
            "Should have everything you need.\x02\x03",

            "If you need to modify any\x01",
            "orbments, just let me know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        "#006FOkay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x102,
        "#012FWe'll be off, then.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x667)
    OP_28(0x4F, 0x1, 0x1)
    OP_28(0x4F, 0x1, 0x2)
    OP_28(0x4F, 0x1, 0x4)
    SetChrFlags(0xF, 0x80)
    OP_4B(0xE, 255)
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    OP_4B(0xA, 255)
    OP_4B(0xB, 255)
    OP_4B(0xC, 255)
    OP_4B(0xD, 255)
    OP_43(0xE, 0x0, 0x0, 0x2)
    OP_43(0xA, 0x0, 0x0, 0x2)
    EventEnd(0x0)
    Return()

    # Function_16_1B8D end

    def Function_17_2D24(): pass

    label("Function_17_2D24")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D35")
    RemoveParty(0x2, 0xFF)

    label("loc_2D35")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D46")
    RemoveParty(0x3, 0xFF)

    label("loc_2D46")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D57")
    RemoveParty(0x5, 0xFF)

    label("loc_2D57")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D68")
    RemoveParty(0x4, 0xFF)

    label("loc_2D68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D79")
    RemoveParty(0x6, 0xFF)

    label("loc_2D79")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D8A")
    RemoveParty(0x7, 0xFF)

    label("loc_2D8A")

    Fade(1000)
    SetChrPos(0x101, 34210, 0, -9750, 350)
    SetChrPos(0x102, 33060, 0, -8430, 45)
    SetChrPos(0xE, 34700, 0, -7770, 222)
    Call(0, 18)
    OP_6D(35570, 0, -7090, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    AnonymousTalk(    #63
        "\x07\x05Choose two members other than Estelle and Joshua.\x02",
    )


    label("loc_2E57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32B6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EB9")

    Menu(
        0,
        10,
        106,
        1,
        (
            " *[Schera]\x01",       # 0
            "  [Olivier]\x01",      # 1
            "  [Agate]\x01",        # 2
            "  [Tita]\x01",         # 3
            "  [Zin]\x01",          # 4
            "  [Kloe]\x01",         # 5
        )
    )

    Jump("loc_30A7")

    label("loc_2EB9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F0E")

    Menu(
        0,
        10,
        106,
        1,
        (
            "  [Schera]\x01",       # 0
            " *[Olivier]\x01",      # 1
            "  [Agate]\x01",        # 2
            "  [Tita]\x01",         # 3
            "  [Zin]\x01",          # 4
            "  [Kloe]\x01",         # 5
        )
    )

    Jump("loc_30A7")

    label("loc_2F0E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F63")

    Menu(
        0,
        10,
        106,
        1,
        (
            "  [Schera]\x01",       # 0
            "  [Olivier]\x01",      # 1
            " *[Agate]\x01",        # 2
            "  [Tita]\x01",         # 3
            "  [Zin]\x01",          # 4
            "  [Kloe]\x01",         # 5
        )
    )

    Jump("loc_30A7")

    label("loc_2F63")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FB8")

    Menu(
        0,
        10,
        106,
        1,
        (
            "  [Schera]\x01",       # 0
            "  [Olivier]\x01",      # 1
            "  [Agate]\x01",        # 2
            " *[Tita]\x01",         # 3
            "  [Zin]\x01",          # 4
            "  [Kloe]\x01",         # 5
        )
    )

    Jump("loc_30A7")

    label("loc_2FB8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_300D")

    Menu(
        0,
        10,
        106,
        1,
        (
            "  [Schera]\x01",       # 0
            "  [Olivier]\x01",      # 1
            "  [Agate]\x01",        # 2
            "  [Tita]\x01",         # 3
            " *[Zin]\x01",          # 4
            "  [Kloe]\x01",         # 5
        )
    )

    Jump("loc_30A7")

    label("loc_300D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3063")

    Menu(
        0,
        10,
        106,
        1,
        (
            "  [Schera]\x01",       # 0
            "  [Olivier]\x01",      # 1
            "  [Agate]\x01",        # 2
            "  [Tita]\x01",         # 3
            "  [Zin] \x01",         # 4
            " *[Kloe]\x01",         # 5
        )
    )

    Jump("loc_30A7")

    label("loc_3063")


    Menu(
        0,
        10,
        106,
        0,
        (
            "  [Schera]\x01",       # 0
            "  [Olivier]\x01",      # 1
            "  [Agate]\x01",        # 2
            "  [Tita]\x01",         # 3
            "  [Zin]\x01",          # 4
            "  [Kloe]\x01",         # 5
        )
    )


    label("loc_30A7")

    MenuEnd(0x0)
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_30CE"),
        (1, "loc_30E8"),
        (2, "loc_3102"),
        (3, "loc_311C"),
        (4, "loc_3136"),
        (5, "loc_3150"),
        (SWITCH_DEFAULT, "loc_316A"),
    )


    label("loc_30CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30E2")
    AddParty(0x2, 0xFF)
    Jump("loc_30E5")

    label("loc_30E2")

    RemoveParty(0x2, 0xFF)

    label("loc_30E5")

    Jump("loc_31E2")

    label("loc_30E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30FC")
    AddParty(0x3, 0xFF)
    Jump("loc_30FF")

    label("loc_30FC")

    RemoveParty(0x3, 0xFF)

    label("loc_30FF")

    Jump("loc_31E2")

    label("loc_3102")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3116")
    AddParty(0x5, 0xFF)
    Jump("loc_3119")

    label("loc_3116")

    RemoveParty(0x5, 0xFF)

    label("loc_3119")

    Jump("loc_31E2")

    label("loc_311C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3130")
    AddParty(0x6, 0xFF)
    Jump("loc_3133")

    label("loc_3130")

    RemoveParty(0x6, 0xFF)

    label("loc_3133")

    Jump("loc_31E2")

    label("loc_3136")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_314A")
    AddParty(0x7, 0xFF)
    Jump("loc_314D")

    label("loc_314A")

    RemoveParty(0x7, 0xFF)

    label("loc_314D")

    Jump("loc_31E2")

    label("loc_3150")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3164")
    AddParty(0x4, 0xFF)
    Jump("loc_3167")

    label("loc_3164")

    RemoveParty(0x4, 0xFF)

    label("loc_3167")

    Jump("loc_31E2")

    label("loc_316A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_317E")
    RemoveParty(0x2, 0xFF)
    Jump("loc_31DF")

    label("loc_317E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3192")
    RemoveParty(0x3, 0xFF)
    Jump("loc_31DF")

    label("loc_3192")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31A6")
    RemoveParty(0x5, 0xFF)
    Jump("loc_31DF")

    label("loc_31A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31BA")
    RemoveParty(0x4, 0xFF)
    Jump("loc_31DF")

    label("loc_31BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31CE")
    RemoveParty(0x6, 0xFF)
    Jump("loc_31DF")

    label("loc_31CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31DF")
    RemoveParty(0x7, 0xFF)

    label("loc_31DF")

    Jump("loc_31E2")

    label("loc_31E2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3205")
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x2, 0x80)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3291")

    label("loc_3205")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_324A")

    AnonymousTalk(    #64
        "\x07\x05Choose two members other than Estelle and Joshua.\x02",
    )

    Jump("loc_3291")

    label("loc_324A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3291")
    SetChrFlags(0x2, 0x80)

    AnonymousTalk(    #65
        "\x07\x05Choose two members other than Estelle and Joshua.\x02",
    )


    label("loc_3291")

    SetChrPos(0x101, 34210, 0, -9750, 350)
    SetChrPos(0x102, 33060, 0, -8430, 45)
    Jump("loc_2E57")

    label("loc_32B6")

    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(300, 0)
    Fade(1000)
    SetChrPos(0x101, 34210, 0, -9750, 350)
    SetChrPos(0x102, 33060, 0, -8430, 45)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    SetChrPos(0x2, 32130, 0, -9730, 45)
    SetChrPos(0x3, 33020, 0, -10520, 45)
    Call(0, 18)
    OP_6D(35570, 0, -7090, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Return()

    # Function_17_2D24 end

    def Function_18_3362(): pass

    label("Function_18_3362")

    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 34700, 0, -7770, 225)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_339F")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 35690, 0, -4120, 180)
    Jump("loc_33A4")

    label("loc_339F")

    SetChrFlags(0xB, 0x80)

    label("loc_33A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33CB")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 34740, 0, -6560, 180)
    Jump("loc_33D0")

    label("loc_33CB")

    SetChrFlags(0xC, 0x80)

    label("loc_33D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33F7")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 37870, 0, -7040, 225)
    Jump("loc_33FC")

    label("loc_33F7")

    SetChrFlags(0x9, 0x80)

    label("loc_33FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3423")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 37210, 0, -5860, 225)
    Jump("loc_3428")

    label("loc_3423")

    SetChrFlags(0x8, 0x80)

    label("loc_3428")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_344F")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 39350, 0, -8220, 270)
    Jump("loc_3454")

    label("loc_344F")

    SetChrFlags(0xD, 0x80)

    label("loc_3454")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_347B")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 36420, 0, -7530, 225)
    Jump("loc_3480")

    label("loc_347B")

    SetChrFlags(0xA, 0x80)

    label("loc_3480")

    Return()

    # Function_18_3362 end

    def Function_19_3481(): pass

    label("Function_19_3481")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #66
        "\x07\x05There is an orbment charging station here.\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_363F")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_72(0x10, 0x20)
    OP_6F(0x10, 300)
    OP_70(0x10, 0x1F4)
    OP_73(0x10)
    OP_6F(0x10, 500)
    OP_70(0x10, 0x2BC)
    OP_71(0x10, 0x20)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x6, 0x2)
    LoadEffect(0x5, "map\\\\mp027_01.eff")
    PlayEffect(0x5, 0x6, 0xFF, 38290, 1200, -3310, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1500, 0, -1)
    Sleep(1500)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    Sleep(3500)
    OP_82(0x6, 0x0)
    LoadEffect(0x5, "map\\\\mp027_00.eff")
    PlayEffect(0x5, 0x0, 0xFF, 38290, 1200, -3310, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x10, 0)
    OP_70(0x10, 0xFA)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_363F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3659")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_3659")

    Return()

    # Function_19_3481 end

    SaveToFile()

Try(main)
