from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2132   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2132.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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
        'Ernest',                               # 9
        'Nial',                                 # 10
        'Duke Dunan',                           # 11
        'Butler Phillip',                       # 12
        'Rutherford',                           # 13
        'Randall',                              # 14
        'Muriel',                               # 15
        'Seagaro',                              # 16
        'Edel',                                 # 17
        'Simon',                                # 18
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
        'ED6_DT07/CH02470 ._CH',             # 00
        'ED6_DT07/CH01570 ._CH',             # 01
        'ED6_DT07/CH02140 ._CH',             # 02
        'ED6_DT07/CH02060 ._CH',             # 03
        'ED6_DT07/CH01140 ._CH',             # 04
        'ED6_DT06/CH20086 ._CH',             # 05
        'ED6_DT07/CH01020 ._CH',             # 06
        'ED6_DT07/CH01000 ._CH',             # 07
        'ED6_DT07/CH01050 ._CH',             # 08
        'ED6_DT07/CH01040 ._CH',             # 09
        'ED6_DT07/CH01210 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH02470P._CP',             # 00
        'ED6_DT07/CH01570P._CP',             # 01
        'ED6_DT07/CH02140P._CP',             # 02
        'ED6_DT07/CH02060P._CP',             # 03
        'ED6_DT07/CH01140P._CP',             # 04
        'ED6_DT06/CH20086P._CP',             # 05
        'ED6_DT07/CH01020P._CP',             # 06
        'ED6_DT07/CH01000P._CP',             # 07
        'ED6_DT07/CH01050P._CP',             # 08
        'ED6_DT07/CH01040P._CP',             # 09
        'ED6_DT07/CH01210P._CP',             # 0A
        'ED6_DT07/CH01140P._CP',             # 0B
    )

    DeclNpc(
        X                   = -1900,
        Z                   = 0,
        Y                   = 11500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 24500,
        Z                   = 0,
        Y                   = 6100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 24500,
        Z                   = 0,
        Y                   = 6100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 24500,
        Z                   = 0,
        Y                   = 6100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -42540,
        Z                   = 0,
        Y                   = 1360,
        Direction           = 286,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -47700,
        Z                   = 0,
        Y                   = 1570,
        Direction           = 265,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -45810,
        Z                   = 0,
        Y                   = 3660,
        Direction           = 275,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -43270,
        Z                   = 0,
        Y                   = 28470,
        Direction           = 79,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -45290,
        Z                   = 0,
        Y                   = 26250,
        Direction           = 269,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 27950,
        Z                   = 0,
        Y                   = 49500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )


    DeclActor(
        TriggerX            = -2020,
        TriggerZ            = 0,
        TriggerY            = 10280,
        TriggerRange        = 400,
        ActorX              = -1900,
        ActorZ              = 1500,
        ActorY              = 11500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_26A",          # 00, 0
        "Function_1_38E",          # 01, 1
        "Function_2_3CA",          # 02, 2
        "Function_3_3E0",          # 03, 3
        "Function_4_3E5",          # 04, 4
        "Function_5_1453",         # 05, 5
        "Function_6_1454",         # 06, 6
        "Function_7_15DA",         # 07, 7
        "Function_8_163B",         # 08, 8
        "Function_9_169B",         # 09, 9
        "Function_10_16C7",        # 0A, 10
        "Function_11_1708",        # 0B, 11
        "Function_12_1744",        # 0C, 12
        "Function_13_179E",        # 0D, 13
        "Function_14_1894",        # 0E, 14
        "Function_15_1B48",        # 0F, 15
        "Function_16_1B76",        # 10, 16
        "Function_17_395E",        # 11, 17
        "Function_18_4813",        # 12, 18
    )


    def Function_0_26A(): pass

    label("Function_0_26A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_274")
    Jump("loc_2DE")

    label("loc_274")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_283")
    ClearChrFlags(0x11, 0x80)
    Jump("loc_2DE")

    label("loc_283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_28D")
    Jump("loc_2DE")

    label("loc_28D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 2)), scpexpr(EXPR_END)), "loc_2DE")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -5790, 0, 84500, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -8410, 0, 83450, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)

    label("loc_2DE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FB")
    SetChrPos(0x0, -8880, 0, 930, 45)

    label("loc_2FB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x77), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_318")
    SetChrPos(0x0, -12970, 0, 4970, 45)

    label("loc_318")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_335")
    SetChrPos(0x0, -11310, 0, 41790, 45)

    label("loc_335")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_351")
    SetMapFlags(0x10000000)
    OP_A3(0x3FA)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 16)

    label("loc_351")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (112, "loc_361"),
        (115, "loc_377"),
        (SWITCH_DEFAULT, "loc_38D"),
    )


    label("loc_361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_374")
    OP_A2(0x41A)
    Event(0, 14)

    label("loc_374")

    Jump("loc_38D")

    label("loc_377")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_38A")
    OP_A2(0x41B)
    Event(0, 17)

    label("loc_38A")

    Jump("loc_38D")

    label("loc_38D")

    Return()

    # Function_0_26A end

    def Function_1_38E(): pass

    label("Function_1_38E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3AF")
    OP_B1("t2132_y")
    Jump("loc_3B8")

    label("loc_3AF")

    OP_B1("t2132_n")

    label("loc_3B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C9")
    OP_1B(0x0, 0x0, 0x12)

    label("loc_3C9")

    Return()

    # Function_1_38E end

    def Function_2_3CA(): pass

    label("Function_2_3CA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3DF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3CA")

    label("loc_3DF")

    Return()

    # Function_2_3CA end

    def Function_3_3E0(): pass

    label("Function_3_3E0")

    Call(0, 4)
    Return()

    # Function_3_3E0 end

    def Function_4_3E5(): pass

    label("Function_4_3E5")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Rest\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_445")
    OP_0D()
    OP_A9(0x21)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_445")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_456")
    TalkEnd(0x8)
    Return()

    label("loc_456")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4F3")

    ChrTalk(    #0
        0x8,
        (
            "The arrest of the mayor is\x01",
            "going to cause some big trouble\x01",
            "for government proceedings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "I figure it'll also have\x01",
            "a big impact on tourism.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_144F")

    label("loc_4F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_59B")

    ChrTalk(    #2
        0x8,
        (
            "The current owner of the hotel\x01",
            "is named Norman. He lives in a\x01",
            "house on the southern block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "He's put a lot of work into\x01",
            "expanding the tourist trade.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_144F")

    label("loc_59B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_670")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62B")
    OP_A2(0x0)

    ChrTalk(    #4
        0x8,
        (
            "It seems that Duke Dunan\x01",
            "is also visiting Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "By all appearances, he really\x01",
            "likes it around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        "Phew...\x02",
    )

    CloseMessageWindow()
    Jump("loc_66D")

    label("loc_62B")


    ChrTalk(    #7
        0x8,
        (
            "It seems that Duke Dunan\x01",
            "is also visiting Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        "Phew...\x02",
    )

    CloseMessageWindow()

    label("loc_66D")

    Jump("loc_144F")

    label("loc_670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_74A")

    ChrTalk(    #9
        0x8,
        (
            "It'll soon be time\x01",
            "for the royal academy's\x01",
            "campus festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "I think they invite back all\x01",
            "their alumni every year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "The hotels nearby will be\x01",
            "flooded with them, as well\x01",
            "as celebrities, no doubt.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_144F")

    label("loc_74A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_8BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_812")
    OP_A2(0x0)

    ChrTalk(    #12
        0x8,
        (
            "The duke had planned to go out\x01",
            "on the water, but I think the\x01",
            "boat is in for repairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "I suggested that perhaps\x01",
            "he should go up to see\x01",
            "the waterfall, instead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        "*sigh*\x02",
    )

    CloseMessageWindow()
    Jump("loc_8B9")

    label("loc_812")


    ChrTalk(    #15
        0x8,
        (
            "The duke had planned to go out\x01",
            "on the water, but I think the\x01",
            "boat is in for repairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "I suggested that perhaps\x01",
            "he should go up to see\x01",
            "the waterfall, instead.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B9")

    Jump("loc_144F")

    label("loc_8BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 2)), scpexpr(EXPR_END)), "loc_A3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EE")
    OP_A2(0x0)

    ChrTalk(    #17
        0x8,
        (
            "You sure seem to be in a big\x01",
            "hurry, for whatever reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        "Did you need something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x136,
        (
            "#043FPardon us, Mr. Manager.\x02\x03",

            "You rent out a boat;\x01",
            "is that correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "Yes, just go down these\x01",
            "stairs and take a right\x01",
            "to get to where it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        (
            "#005FDownstairs, to the right.\x02\x03",

            "Thanks!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A3C")

    label("loc_9EE")


    ChrTalk(    #22
        0x8,
        (
            "If you want the rental boat,\x01",
            "it's downstairs, out the door\x01",
            "to the right.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3C")

    Jump("loc_144F")

    label("loc_A3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_B44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD6")
    OP_A2(0x0)

    ChrTalk(    #23
        0x8,
        (
            "I'm truly sorry for the trouble\x01",
            "yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "I can only promise you that\x01",
            "it will not happen again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        "I have no excuse.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B41")

    label("loc_AD6")


    ChrTalk(    #26
        0x8,
        (
            "I'm truly sorry for the trouble\x01",
            "yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "I can only promise you that\x01",
            "it will not happen again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B41")

    Jump("loc_144F")

    label("loc_B44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 2)), scpexpr(EXPR_END)), "loc_CA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C73")
    OP_A2(0x4CD)

    ChrTalk(    #28
        0x8,
        (
            "I deeply regret any trouble my\x01",
            "ineptitude has caused you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "Please, have a drink.\x01",
            "On the house.\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x1A2, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #30
        "\x07\x00Received \x07\x02Fresh Juice\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #31
        0x8,
        (
            "It's the least I can do,\x01",
            "by way of apology.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "I merely wanted to serve\x01",
            "you. I am sorry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA2")

    label("loc_C73")


    ChrTalk(    #33
        0x8,
        (
            "I merely wanted to serve\x01",
            "you. I am sorry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA2")

    Jump("loc_144F")

    label("loc_CA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 1)), scpexpr(EXPR_END)), "loc_D24")

    ChrTalk(    #34
        0x8,
        (
            "Your room is on\x01",
            "the topmost floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "I believe you will be\x01",
            "quite pleased with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        "Have a pleasant stay.\x02",
    )

    CloseMessageWindow()
    Jump("loc_144F")

    label("loc_D24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_1318")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1286")
    EventBegin(0x0)
    Fade(1000)
    OP_69(0x8, 0x0)
    OP_6B(2800, 0)
    OP_8C(0x8, 180, 0)
    SetChrPos(0x101, -1830, 0, 9580, 354)
    SetChrPos(0x102, -2920, 0, 9310, 354)
    SetChrPos(0x136, -2370, 0, 8090, 354)
    OP_0D()

    ChrTalk(    #37
        0x8,
        (
            "Hello...\x01",
            "Welcome to the Hotel Blanche.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        "Do you have a reservation with us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        "#000FNo, but we were hoping that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x102,
        "#010FDo you have any rooms available?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        "Impeccable timing, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "We just had a cancellation for\x01",
            "the room on the top floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x8,
        (
            "If it pleases you, I can\x01",
            "show it to you now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#008FA penthouse, huh?\x01",
            "That could be nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x102,
        (
            "#014FBut isn't that going\x01",
            "to be expensive?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        (
            "Since it's empty due to a\x01",
            "cancellation, I'd be happy to\x01",
            "charge you the standard rate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "Not to mention, you appear\x01",
            "to be bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "I'd consider it an honor to serve\x01",
            "you, for all the hard work you\x01",
            "do in protecting our citizens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#001FHee hee... Well, when you put it\x01",
            "like that, how can we refuse?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x102,
        "#010FSo, yes, we would like the room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        "As you wish, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x136,
        (
            "#041FHa ha... Well, that was a \x01",
            "stroke of luck, wasn't it?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10DB():
        OP_69(0x101, 0x4B0)
        ExitThread()

    QueueWorkItem(0x136, 2, lambda_10DB)
    TurnDirection(0x101, 0x136, 400)
    TurnDirection(0x102, 0x136, 400)
    WaitChrThread(0x136, 0x2)

    ChrTalk(    #53
        0x136,
        (
            "#040FAnyway, I think I'll go back to\x01",
            "campus for the time being.\x02\x03",

            "I won't make it back before\x01",
            "the dorms are locked up, if\x01",
            "I don't hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        (
            "#000F#6POh, right. You said you could\x01",
            "only stay until evening.\x02\x03",

            "#007FHmmm... Well, I hate to see\x01",
            "you go, but I understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x102,
        (
            "#010F#3PWould you like us to\x01",
            "escort you back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x136,
        (
            "#041FHa ha... It's all right.\x01",
            "I know the way.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x419)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T2100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1315")

    label("loc_1286")


    ChrTalk(    #57
        0x8,
        (
            "We see many tourists pass through,\x01",
            "around this time of year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x8,
        (
            "If you'd like to get a room,\x01",
            "I recommend reserving one well\x01",
            "in advance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1315")

    Jump("loc_144F")

    label("loc_1318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_144F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13D4")
    OP_A2(0x0)

    ChrTalk(    #59
        0x8,
        (
            "Hello...\x01",
            "Welcome to the Hotel Blanche.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x8,
        (
            "All of the rooms here boast a\x01",
            "magnificent view of the ocean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        (
            "Please, feel free to relax and\x01",
            "enjoy our amenities.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_144F")

    label("loc_13D4")


    ChrTalk(    #62
        0x8,
        (
            "All of the rooms here boast a\x01",
            "magnificent view of the ocean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x8,
        (
            "Please, feel free to relax and\x01",
            "enjoy our amenities.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_144F")

    TalkEnd(0x8)
    Return()

    # Function_4_3E5 end

    def Function_5_1453(): pass

    label("Function_5_1453")

    Return()

    # Function_5_1453 end

    def Function_6_1454(): pass

    label("Function_6_1454")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1554")
    OP_A2(0x2)

    ChrTalk(    #64
        0xFE,
        (
            "#221FHa ha ha... Now THAT is\x01",
            "a beautiful landscape.\x02\x03",

            "#220FI like it! It is truly a room\x01",
            "fit for the future king.\x02\x03",

            "Now, if only the casino would open...\x02\x03",

            "#222FIt's utterly outrageous that\x01",
            "they're closed for renovations\x01",
            "while I'm here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15D6")

    label("loc_1554")


    ChrTalk(    #65
        0xFE,
        (
            "#220FNow, if only the casino would open...\x02\x03",

            "#222FIt's utterly outrageous that\x01",
            "they're closed for renovations\x01",
            "while I'm here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15D6")

    TalkEnd(0xA)
    Return()

    # Function_6_1454 end

    def Function_7_15DA(): pass

    label("Function_7_15DA")

    TalkBegin(0xB)

    ChrTalk(    #66
        0xB,
        (
            "#720FI have caused you enough\x01",
            "trouble.\x02\x03",

            "I will not forget what\x01",
            "you have done for me.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_7_15DA end

    def Function_8_163B(): pass

    label("Function_8_163B")

    TalkBegin(0xFE)

    ChrTalk(    #67
        0xFE,
        "...So, uh, where do I sleep?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "Guess I'll have to ask the concierge\x01",
            "for a cot...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_163B end

    def Function_9_169B(): pass

    label("Function_9_169B")

    TalkBegin(0xFE)

    ChrTalk(    #69
        0xFE,
        (
            "Well, well...\x01",
            "Isn't this comfy?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_169B end

    def Function_10_16C7(): pass

    label("Function_10_16C7")

    TalkBegin(0xFE)

    ChrTalk(    #70
        0xFE,
        "This is niiiiice. ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "I can handle staying here.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_16C7 end

    def Function_11_1708(): pass

    label("Function_11_1708")

    TalkBegin(0xFE)

    ChrTalk(    #72
        0xFE,
        (
            "It's a gorgeous room, but\x01",
            "I just can't relax...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_1708 end

    def Function_12_1744(): pass

    label("Function_12_1744")

    TalkBegin(0xFE)

    ChrTalk(    #73
        0xFE,
        "Oh, what a lovely room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "But it's hard to see the\x01",
            "water from this side...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_1744 end

    def Function_13_179E(): pass

    label("Function_13_179E")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_183C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1804")
    OP_A2(0x1)

    ChrTalk(    #75
        0xFE,
        "Hmm... Let's see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "We have to get packed to\x01",
            "go back to Bose, soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1839")

    label("loc_1804")


    ChrTalk(    #77
        0xFE,
        (
            "We have to get packed to\x01",
            "go back to Bose, soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1839")

    Jump("loc_1890")

    label("loc_183C")


    ChrTalk(    #78
        0xFE,
        (
            "Ms. Mirano certainly wasn't\x01",
            "kidding about knowing the\x01",
            "manager at a nice hotel.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1890")

    TalkEnd(0x11)
    Return()

    # Function_13_179E end

    def Function_14_1894(): pass

    label("Function_14_1894")

    EventBegin(0x0)
    OP_6D(-2330, 0, 81840, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    SetChrPos(0x102, -1600, 0, 75980, 270)
    SetChrPos(0x101, -1210, 0, 76950, 270)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #79
        0x101,
        "#501F#1PWow... It's enormous!\x02",
    )

    CloseMessageWindow()
    OP_8E(0x101, 0xFFFFF68C, 0x0, 0x13074, 0x1388, 0x0)

    def lambda_1958():
        OP_8E(0xFE, 0xFFFFF272, 0x0, 0x1375E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1958)
    OP_8E(0x101, 0xFFFFFBE6, 0x0, 0x13C2C, 0x1388, 0x0)
    OP_8E(0x101, 0x5D2, 0x0, 0x14320, 0x1388, 0x0)
    OP_8C(0x101, 90, 400)
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 45, 400)
    Sleep(1000)
    ClearMapFlags(0x1)

    def lambda_19CF():
        OP_6D(-13470, 0, 74920, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_19CF)

    def lambda_19E7():
        OP_6C(0, 4500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_19E7)

    def lambda_19F7():
        OP_8E(0xFE, 0xFFFFE660, 0x0, 0x142B2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19F7)
    Sleep(500)
    OP_8C(0x102, 315, 400)
    OP_43(0x102, 0x1, 0x0, 0xF)
    WaitChrThread(0x101, 0x1)
    OP_8E(0x101, 0xFFFFD094, 0x0, 0x12AE8, 0x1388, 0x0)
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #80
        0x101,
        "#000FAnd this is just the bedroom...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #81
        0x102,
        (
            "#010FNot only the top floor, but an\x01",
            "all-out suite...\x02\x03",

            "I would have been just fine\x01",
            "with a regular room, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        (
            "#001FWell, I think we should enjoy\x01",
            "it while we can.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T2100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_1894 end

    def Function_15_1B48(): pass

    label("Function_15_1B48")

    Sleep(1000)
    OP_8E(0xFE, 0xFFFFE53E, 0x0, 0x13826, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFD616, 0x0, 0x128C2, 0x7D0, 0x0)
    Return()

    # Function_15_1B48 end

    def Function_16_1B76(): pass

    label("Function_16_1B76")

    EventBegin(0x0)
    OP_6D(-13860, 0, 75700, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0xA, -12490, 0, 76470, 225)
    SetChrPos(0xB, -11080, 0, 76600, 225)
    SetChrPos(0x101, -6200, 0, 83040, 225)
    SetChrPos(0x102, -5190, 0, 82770, 225)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(    #83
        0xA,
        "Nobleman",
        (
            "#220F#6PIt's spacious and well-appointed.\x02\x03",

            "Hmm...yes, I like it.\x01",
            "I'll take the room.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #84
        0xB,
        "Old Man In Black",
        (
            "#722F#4PPlease wait a moment,\x01",
            "Your Grace.\x02\x03",

            "I'm afraid that this room is not\x01",
            "vacant.\x02\x03",

            "Perhaps you can stay at the mayor's\x01",
            "estate, as originally planned?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 400)

    NpcTalk(    #85
        0xA,
        "Nobleman",
        (
            "#224F#6PHush, Phillip! I can't even see\x01",
            "the water from there!\x02\x03",

            "#225FThis hotel has a much better view,\x01",
            "and I can smell the sea air, as\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_8C(0xA, 45, 400)

    def lambda_1DF9():

        label("loc_1DF9")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_1DF9")

    QueueWorkItem2(0xB, 1, lambda_1DF9)

    def lambda_1E0A():
        OP_6D(-7270, 0, 83010, 2000)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1E0A)
    OP_8E(0xA, 0xFFFFE2D2, 0x0, 0x13D62, 0xBB8, 0x0)
    WaitChrThread(0xB, 0x2)

    NpcTalk(    #86
        0xA,
        "Nobleman",
        "#221F#1PI can even go out on the balcony...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 0x2)
    OP_44(0xB, 0xFF)
    OP_63(0x101)
    OP_63(0x102)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_95(0xA, 0x0, 0x0, 0x0, 0x320, 0x1770)
    OP_8F(0xA, 0xFFFFE020, 0x0, 0x13B6E, 0x1388, 0x0)

    NpcTalk(    #87
        0xA,
        "Nobleman",
        (
            "#226FWh-Who are you people?!\x02\x03",

            "Are you thieves?! Or are you here\x01",
            "to kill me?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        (
            "#007F#4PThat's a horrible thing to assume\x01",
            "about someone.\x02\x03",

            "#009FBesides, who are you, old man?\x01",
            "You have no right to be in here.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #89
        0xA,
        "Nobleman",
        (
            "#224FHow DARE you call me 'old man'?!\x02\x03",

            "#220FHmph. Very well. So you are the\x01",
            "ones renting this suite?\x02\x03",

            "I'm going to be using it as a private\x01",
            "room during my stay in Ruan.\x02\x03",

            "I suggest you leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        (
            "#009F#4PSay what? I don't know what\x01",
            "you're talking about...\x02\x03",

            "...but I don't see any reason\x01",
            "we should have to leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x102,
        "#012F#4PI think we deserve to hear an explanation.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #92
        0xA,
        "Nobleman",
        (
            "#225FBah... I shouldn't have to deal\x01",
            "with you ignorant commoners.\x02\x03",

            "Do you not realize who I am?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#007F#4PNope, no clue.\x02\x03",

            "All I see is an old man with a\x01",
            "weird-looking head.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #94
        0xA,
        "Nobleman",
        "#226FW-Weird...?!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x102,
        (
            "#010F#4PThere's no reason to be rude, Estelle.\x02\x03",

            "At least say 'unique' or something a little\x01",
            "more positive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        "#001F#4POh, I get it. It's all in HOW we say it. ♪\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #97
        0xA,
        "Nobleman",
        (
            "#222FGrrrrrr...\x02\x03",

            "#225FHmph! Fine. Clean out your ears\x01",
            "and listen well.\x02\x03",

            "#224FMy name is Dunan von Auslese!\x02\x03",

            "I am nephew to Queen Alicia II,\x01",
            "granted the title of duke by Her\x01",
            "Majesty herself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        "#004F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x102,
        "#014F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xA,
        (
            "#225FHmm-hmm-hmm...\x01",
            "I see your astonishment has robbed\x01",
            "you of the ability to speak.\x02\x03",

            "But that's to be expected.\x01",
            "What more reason do you\x01",
            "need to give up the room?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        "#008F#4PBuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x102,
        "#019F#4PHa ha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        "#001F#4P#5SHA HA HA HA HA HA!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#001F#4PYou're hilarious, old man!\x01",
            "I'm dying here!\x02\x03",

            "You're supposed to be the\x01",
            "queen's nephew?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x102,
        (
            "#011F#4PAh ha ha... Estelle...it's not\x01",
            "nice to laugh like that.\x02\x03",

            "Maybe he was just telling a joke,\x01",
            "you know, to ease the tension.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xA,
        "#226FYou... You...\x02",
    )

    CloseMessageWindow()
    OP_8E(0xB, 0xFFFFE16A, 0x0, 0x1372C, 0xBB8, 0x0)

    NpcTalk(    #107
        0xB,
        "Old Man In Black",
        (
            "#722FPlease pardon my interruption, but His\x01",
            "Grace speaks the truth.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 400)
    TurnDirection(0x102, 0xB, 400)

    ChrTalk(    #108
        0x101,
        "#004F#4PHuh...?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #109
        0xB,
        "Old Man In Black",
        (
            "#720FPerhaps I should have been quicker\x01",
            "to speak.\x02\x03",

            "I am the duke's personal butler,\x01",
            "Phillip.\x02\x03",

            "He has been under my care since\x01",
            "the time of his birth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        "#008F#4PHuh... Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xB,
        (
            "#721FI assure you that all of this is\x01",
            "true, on my honor.\x02\x03",

            "The man before you is, indeed, Duke\x01",
            "Dunan...nephew of Her Majesty the\x01",
            "Queen.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 135, 400)

    ChrTalk(    #112
        0x101,
        (
            "#002F#6P(I can't believe it, but...)\x02\x03",

            "(Never mind the weird, rich-looking\x01",
            "guy...but the butler seems legit.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x102,
        (
            "#013F#4P(I'm suddenly reminded of something\x01",
            "Jean told us...)\x02\x03",

            "(He said that royalty would be\x01",
            "arriving in Ruan to inspect the\x01",
            "city.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xA,
        (
            "#221FHa ha ha! Will you submit now?\x02\x03",

            "I am next in line to succeed the\x01",
            "throne, and you should be honored\x01",
            "to give me your room.\x02\x03",

            "Such an opportunity is afforded\x01",
            "to commoners quite rarely!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 225, 400)

    ChrTalk(    #115
        0x101,
        (
            "#005F#4PYou... You've got to be kidding!\x02\x03",

            "You may be royalty, but to me, you're\x01",
            "just acting like an arrogant old man!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xB, 0xFFFFE7F0, 0x0, 0x14050, 0xFA0, 0x0)
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #116
        0xB,
        "#723F#6PMiss! Please, you must wait!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 400)
    TurnDirection(0x102, 0xB, 400)

    ChrTalk(    #117
        0x101,
        "#004F#6PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xB,
        (
            "#720F#6PPlease, hear me out for\x01",
            "a moment.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2AC2():
        OP_6D(-5790, 0, 84490, 1000)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2AC2)

    def lambda_2ADA():

        label("loc_2ADA")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_2ADA")

    QueueWorkItem2(0x101, 1, lambda_2ADA)

    def lambda_2AEB():

        label("loc_2AEB")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_2AEB")

    QueueWorkItem2(0x102, 1, lambda_2AEB)
    SetChrFlags(0x101, 0x4)

    def lambda_2B01():
        OP_8E(0xFE, 0xFFFFE962, 0x0, 0x148AC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2B01)

    def lambda_2B1C():
        OP_8E(0xFE, 0xFFFFEC14, 0x0, 0x14924, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2B1C)
    OP_8E(0xB, 0xFFFFEA7A, 0x0, 0x1442E, 0x7D0, 0x0)
    OP_8C(0xB, 0, 400)
    ClearChrFlags(0x101, 0x4)

    ChrTalk(    #119
        0xB,
        (
            "#720F#6PPardon my impertinence, but\x01",
            "I would ask you for a favor.\x02\x03",

            "Could I persuade you to relinquish\x01",
            "the room?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #120
        (
            "\x07\x05The elderly butler produced a large sum of mira from his breast pocket and\x01",
            "presented it.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #121
        0x101,
        "#004F#6PM-Mister Phillip...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x102,
        "#014F#6PYou'd do that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xB,
        (
            "#722F#6PHis Grace is the type of man\x01",
            "who will not be swayed once he\x01",
            "has begun speaking.\x02\x03",

            "I fear this trait may even be due\x01",
            "to negligence on my part...\x02\x03",

            "So, please... Please...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #124
        "\x07\x05The old butler bowed his head before Estelle and Joshua.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x101)
    OP_63(0x102)

    ChrTalk(    #125
        0x101,
        (
            "#007F#6P*sigh* Well, I guess that's that.\x02\x03",

            "I don't want to cause the butler\x01",
            "any trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x102,
        (
            "#010F#6PYou can have the room.\x02\x03",

            "And you don't need to pay us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xB,
        "#721F#6PB-But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x101,
        (
            "#006F#6PIt's fine, really!♪\x02\x03",

            "It really is a little too fancy\x01",
            "for us.\x02\x03",

            "#001FI'll bet looking after that guy is a\x01",
            "hassle, but hang in there, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xB,
        (
            "#722F#6PM-Madame...\x02\x03",

            "You have my deepest gratitude.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0xA, 0xFFFFE552, 0x0, 0x14064, 0x7D0, 0x0)

    ChrTalk(    #130
        0xA,
        (
            "#224FHey, what are you whispering\x01",
            "about?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2F94():
        OP_8E(0xFE, 0xFFFFEC1E, 0x0, 0x1419A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2F94)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0xA, 400)
    TurnDirection(0x101, 0xA, 400)
    WaitChrThread(0xB, 0x1)
    TurnDirection(0xB, 0xA, 400)

    ChrTalk(    #131
        0x101,
        "#006F#4POhhh...nothing important.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x102,
        (
            "#010F#4PPlease pardon our intrusion.\x02\x03",

            "We will give the room over to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xA,
        (
            "#220FAhh, you will...?\x02\x03",

            "#221FHa ha ha! If only you'd been so\x01",
            "humble to begin with.\x02\x03",

            "You'd do well to retain that\x01",
            "mindset in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x101,
        "#007F#4POh, what a total je--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x102,
        "#019F#4PNow, if you'll excuse us.\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_69(0x8, 0x0)
    OP_6B(2600, 0)
    OP_6C(35000, 0)
    SetChrPos(0x101, -1830, 0, 9580, 354)
    SetChrPos(0x102, -2920, 0, 9310, 354)
    OP_4A(0x8, 255)
    Sleep(500)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_21()
    OP_1E()
    OP_0D()

    ChrTalk(    #136
        0x8,
        "Really...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x8,
        (
            "Even if you'd explained your situation\x01",
            "to the duke, he probably still wouldn't\x01",
            "have taken 'no' for an answer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x8,
        (
            "I'm really sorry that you had to\x01",
            "deal with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        (
            "#000FIt's really no big deal.\x02\x03",

            "If there's anyone to blame,\x01",
            "it's that selfish duke guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x102,
        (
            "#010FThat said...do you have any\x01",
            "other rooms?\x02\x03",

            "A regular room would be\x01",
            "just fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x8,
        "W-Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x8,
        (
            "I'm afraid we just booked our\x01",
            "last room a short while ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x101,
        "#004FAck...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x102,
        (
            "#013FI think we just got played for\x01",
            "suckers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x8,
        (
            "No need to fret.\x01",
            "We are at fault here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x8,
        (
            "I will see to it that arrangements\x01",
            "are made for you elsewhere.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2230, 0, 3110, 0)

    NpcTalk(    #147
        0x9,
        "Man's Voice",
        "#1PYo, what's the deal here?\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_346F():
        OP_6D(-2200, 0, 9820, 1200)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_346F)

    def lambda_3487():
        OP_8E(0xFE, 0xFFFFF66E, 0x0, 0x1D42, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3487)
    OP_8C(0x101, 225, 400)
    OP_8C(0x102, 180, 400)
    WaitChrThread(0x9, 0x1)
    TurnDirection(0x9, 0x8, 0)

    ChrTalk(    #148
        0x9,
        (
            "#141F#2PHey, guys. I haven't seen you\x01",
            "since the sky bandit hideout.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x101,
        "#004F#6PNial?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x102,
        (
            "#010F#3PGood evening. I wouldn't have\x01",
            "expected to see you here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x9,
        (
            "#140F#2PLook who's talking.\x02\x03",

            "I didn't think you two would show\x01",
            "up in Ruan.\x02\x03",

            "Anyway, what's up?\x01",
            "You got problems?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x101,
        "#007F#6PWell...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #153
        "\x07\x05Estelle and Joshua explained the recent turn of events.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #154
        0x9,
        (
            "#147F#2PHa ha ha!\x02\x03",

            "You two get into the damnedest\x01",
            "situations!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x101,
        (
            "#009F#6PAhem! This is not a laughing\x01",
            "matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x9,
        (
            "#141F#2PYeah, yeah, don't get your knickers\x01",
            "in a twist. You can stay in my room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x101,
        "#004F#6PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x9,
        (
            "#141F#2PMy room has some extra beds.\x02\x03",

            "Hey, clerk or concierge or whatever.\x01",
            "You don't mind, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x8,
        (
            "Not at all. In fact, you'd be\x01",
            "helping me immensely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x9,
        (
            "#141F#2PSounds like a plan, then.\x02\x03",

            "The room's on the basement floor.\x01",
            "Follow me.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 400)
    OP_8E(0x9, 0xFFFFF83A, 0x0, 0x15AE, 0xBB8, 0x1)
    OP_8E(0x9, 0x8B6, 0x0, 0x816, 0xBB8, 0x0)
    SetChrFlags(0x9, 0x80)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #161
        0x101,
        "#000F#4PUmm... Are we okay with this?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #162
        0x102,
        (
            "#010F#3PWell, he offered, so it should\x01",
            "be all right.\x02\x03",

            "He may want something in return\x01",
            "for this, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x101,
        (
            "#007F#4PProbably something way out of\x01",
            "proportion, I'll bet.\x02\x03",

            "#006FBut I guess we're kind of stuck...\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    OP_4B(0x8, 255)
    Return()

    # Function_16_1B76 end

    def Function_17_395E(): pass

    label("Function_17_395E")

    EventBegin(0x0)
    OP_6D(-43860, 0, 53790, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(1236, 0)
    OP_6C(72000, 0)
    OP_6E(627, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x4)
    OP_44(0x9, 0xFF)
    SetChrChipByIndex(0x9, 5)
    SetChrSubChip(0x9, 1)
    SetChrPos(0x9, -47650, 200, 55350, 197)
    SetChrPos(0x101, -43080, 0, 53380, 290)
    SetChrPos(0x102, -42750, -200, 52630, 296)
    OP_6F(0x7, 30)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #164
        0x9,
        (
            "#141FAh, good. You're here.\x02\x03",

            "Grab one of the unused beds and\x01",
            "make yourselves at home.\x02",
        )
    )

    CloseMessageWindow()
    OP_72(0x7, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x7, 0x0)
    OP_66(0x0)

    def lambda_3A6E():
        OP_6D(-46290, 0, 55390, 2000)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3A6E)

    def lambda_3A86():
        OP_6B(1100, 2000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3A86)

    def lambda_3A96():
        OP_8E(0xFE, 0xFFFF42FA, 0x0, 0xD20A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A96)
    Sleep(500)

    def lambda_3AB6():
        OP_8E(0xFE, 0xFFFF46E2, 0x0, 0xD070, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3AB6)
    WaitChrThread(0x101, 0x1)
    SetChrSubChip(0x9, 0)

    def lambda_3ADB():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3ADB)
    WaitChrThread(0x102, 0x1)

    def lambda_3AEE():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3AEE)

    ChrTalk(    #165
        0x101,
        (
            "#006F#2PI appreciate you giving us a\x01",
            "place to stay and all...\x02\x03",

            "But the gracious host thing\x01",
            "is a little much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x9,
        (
            "#143F#3POops. Sorry if I'm acting suspicious.\x02\x03",

            "I'm just grateful that you guys\x01",
            "helped me nail a great story\x01",
            "earlier.\x02\x03",

            "I just wanted to pay you back,\x01",
            "is all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x102,
        (
            "#010FYou mean the sky bandit article,\x01",
            "right?\x02\x03",

            "Did it get much of a reaction?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x9,
        (
            "#141F#3POh yeah, it was a big hit!\x02\x03",

            "Our readers loved that article on Colonel\x01",
            "Richard and the Intelligence Division.\x02\x03",

            "I get the feeling that we sold more copies\x01",
            "because of him than the sky bandit incident,\x01",
            "to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x101,
        (
            "#004F#2PHuh...\x01",
            "Is he really that popular?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x9,
        (
            "#141F#3PRumor has it that he's about to\x01",
            "get a big medal from Her Majesty.\x02\x03",

            "It's getting to be just about all\x01",
            "people will talk about.\x02\x03",

            "I'm actually going to have an\x01",
            "exclusive interview with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x102,
        "#014FThat's impressive...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x9,
        (
            "#140F#3PWell, he's got the looks AND\x01",
            "brains to his credit.\x02\x03",

            "He puts people at ease.\x02\x03",

            "#145FThat's all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x101,
        "#505F#2PWhat's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x9,
        (
            "#142F#3PEh, it's nothing to worry about.\x02\x03",

            "#147FThat story netted me a tidy little bonus.\x01",
            "Let's hear it for finally getting rid of my\x01",
            "bad luck charm.\x02\x03",

            "The colonel's one heck of a guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x101,
        (
            "#501F#2PBy 'bad luck charm,' do you\x01",
            "mean Dorothy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x102,
        "#010FSpeaking of whom...she's not with you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x9,
        (
            "#141F#3PI was only looking after her while\x01",
            "she was learning the ropes.\x02\x03",

            "That big story meant the end of\x01",
            "our mighty team.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        (
            "#000F#2PHmmmm...\x02\x03",

            "#506FStill, it worries me to think she's\x01",
            "gone off on her own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x9,
        (
            "#145F#3PI'm kind of trying not to think\x01",
            "about that.\x02\x03",

            "#141FI just want to enjoy a nice vacation\x01",
            "with the bonus I got.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x101,
        (
            "#007F#2PShouldn't you be chasing the\x01",
            "next big scoop?\x02\x03",

            "#006FOr are you checking on that\x01",
            "duke guy who kicked us out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x9,
        (
            "#140F#3PAh, Duke Dunan. Our own\x01",
            "walking catastrophe.\x02\x03",

            "From everything I've heard, he's a\x01",
            "real hedonist. More so than most\x01",
            "royalty, anyway.\x02\x03",

            "Rumor has it that he even drives\x01",
            "Her Majesty up the wall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x102,
        (
            "#010FSounds perfectly believable to me.\x02\x03",

            "But he said he was next in line\x01",
            "to succeed the throne...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x101,
        (
            "#509F#2PSeriously...?\x02\x03",

            "I don't want to have to call\x01",
            "that fat jerk my king.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x9,
        (
            "#140F#3PWell, given Her Majesty's age,\x01",
            "it's not unreasonable.\x02\x03",

            "Plus, there's the fact that her\x01",
            "son died some time ago.\x02\x03",

            "A lot of people would be opposed\x01",
            "to it, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x102,
        (
            "#010FI'm guessing you don't know\x01",
            "much more than we do.\x02\x03",

            "Which would mean...you're chasing\x01",
            "a different story, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x9,
        "#143F#3P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x101,
        "#001F#2PHa! Bull's-eye!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x9,
        (
            "#145F#3PMan...I can't sneak ANYTHING\x01",
            "past you kids.\x02\x03",

            "#141FYes, you're right, but that's\x01",
            "all I'm saying.\x02\x03",

            "This one's just too big.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x101,
        (
            "#501F#2PYou don't think you're overstating\x01",
            "things a little?\x02\x03",

            "But hey, whatever. It's not like we'd\x01",
            "go shouting it from the rooftops.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x102,
        (
            "#010FI look forward to reading it for\x01",
            "myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x9,
        (
            "#147F#3POh, yeah. Just leave it to me.\x02\x03",

            "#141FBy the way...have you two had\x01",
            "dinner yet?\x02\x03",

            "Let me take you out and treat\x01",
            "you both.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        "#001F#2PSeriously?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x102,
        (
            "#010FThank you very much for\x01",
            "your generosity.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_21()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #194
        (
            "\x07\x05That night, Nial bought dinner for Estelle and Joshua at the casino & bar\x01",
            "called Lavantar.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #195
        (
            "\x07\x05After a meal consisting of some of the best seafood from Azelia Bay (and\x01",
            "drink, in Nial's case)...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #196
        (
            "\x07\x05...the two brought the now-unconscious Nial to the hotel, and set him in his\x01",
            "bed to sleep it off.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T2403   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_395E end

    def Function_18_4813(): pass

    label("Function_18_4813")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48DA")
    OP_A2(0x3)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4836")
    TurnDirection(0x102, 0x1, 400)
    Jump("loc_483D")

    label("loc_4836")

    TurnDirection(0x102, 0x0, 400)

    label("loc_483D")


    ChrTalk(    #197
        0x102,
        (
            "#010FLet's go to Nial's room.\x02\x03",

            "After his generous offer,\x01",
            "I don't want to make him wait.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #198
        0x101,
        (
            "#000FI think he said it's on the\x01",
            "basement floor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4941")

    label("loc_48DA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48F0")
    TurnDirection(0x102, 0x1, 400)
    Jump("loc_48F7")

    label("loc_48F0")

    TurnDirection(0x102, 0x0, 400)

    label("loc_48F7")


    ChrTalk(    #199
        0x102,
        (
            "#010FLet's go to Nial's room.\x02\x03",

            "He said it was on the basement floor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4941")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_18_4813 end

    SaveToFile()

Try(main)
