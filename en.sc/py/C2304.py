from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'C2304   ._SN',
        MapName             = 'Ruan',
        Location            = 'C2304.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60060",
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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
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
        'ED6_DT29/CH12730 ._CH',             # 00
        'ED6_DT29/CH12731 ._CH',             # 01
        'ED6_DT29/CH12740 ._CH',             # 02
        'ED6_DT29/CH12741 ._CH',             # 03
        'ED6_DT29/CH12750 ._CH',             # 04
        'ED6_DT29/CH12751 ._CH',             # 05
        'ED6_DT29/CH12760 ._CH',             # 06
        'ED6_DT29/CH12761 ._CH',             # 07
        'ED6_DT29/CH12770 ._CH',             # 08
        'ED6_DT29/CH12771 ._CH',             # 09
        'ED6_DT29/CH12780 ._CH',             # 0A
        'ED6_DT29/CH12781 ._CH',             # 0B
        'ED6_DT29/CH12790 ._CH',             # 0C
        'ED6_DT29/CH12791 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT29/CH12730P._CP',             # 00
        'ED6_DT29/CH12731P._CP',             # 01
        'ED6_DT29/CH12740P._CP',             # 02
        'ED6_DT29/CH12741P._CP',             # 03
        'ED6_DT29/CH12750P._CP',             # 04
        'ED6_DT29/CH12751P._CP',             # 05
        'ED6_DT29/CH12760P._CP',             # 06
        'ED6_DT29/CH12761P._CP',             # 07
        'ED6_DT29/CH12770P._CP',             # 08
        'ED6_DT29/CH12771P._CP',             # 09
        'ED6_DT29/CH12780P._CP',             # 0A
        'ED6_DT29/CH12781P._CP',             # 0B
        'ED6_DT29/CH12790P._CP',             # 0C
        'ED6_DT29/CH12791P._CP',             # 0D
    )

    DeclMonster(
        X                   = 290,
        Z                   = 0,
        Y                   = -40120,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x400,
        Unknown_18          = 7855,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -5500,
        Z                   = 400,
        Y                   = -9000,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x401,
        Unknown_18          = 7856,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 5500,
        Z                   = 400,
        Y                   = -9000,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x404,
        Unknown_18          = 7857,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 5500,
        Z                   = 400,
        Y                   = 11000,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x404,
        Unknown_18          = 7858,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -5500,
        Z                   = 400,
        Y                   = 11000,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x401,
        Unknown_18          = 7859,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 140,
        Z                   = 0,
        Y                   = 660,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x400,
        Unknown_18          = 7860,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -4870,
        TriggerZ            = -3200,
        TriggerY            = 64360,
        TriggerRange        = 1000,
        ActorX              = -5330,
        ActorZ              = -3200,
        ActorY              = 63890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -7290,
        TriggerZ            = -3200,
        TriggerY            = 69820,
        TriggerRange        = 1000,
        ActorX              = -7980,
        ActorZ              = -3200,
        ActorY              = 70010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4990,
        TriggerZ            = -3200,
        TriggerY            = 75520,
        TriggerRange        = 1000,
        ActorX              = -5420,
        ActorZ              = -3200,
        ActorY              = 75960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5070,
        TriggerZ            = -3200,
        TriggerY            = 75430,
        TriggerRange        = 1000,
        ActorX              = 5540,
        ActorZ              = -3200,
        ActorY              = 75890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7290,
        TriggerZ            = -3200,
        TriggerY            = 70200,
        TriggerRange        = 1000,
        ActorX              = 8070,
        ActorZ              = -3200,
        ActorY              = 70040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5010,
        TriggerZ            = -3200,
        TriggerY            = 64510,
        TriggerRange        = 1000,
        ActorX              = 5540,
        ActorZ              = -3200,
        ActorY              = 64120,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 4400,
        TriggerY            = 162290,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = 4400,
        ActorY              = 162970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 400,
        TriggerY            = -74270,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = 400,
        ActorY              = -74900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 50,
        TriggerZ            = 0,
        TriggerY            = 39430,
        TriggerRange        = 1000,
        ActorX              = 50,
        ActorZ              = 0,
        ActorY              = 39430,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -3990,
        TriggerZ            = 4400,
        TriggerY            = 147040,
        TriggerRange        = 1200,
        ActorX              = -3990,
        ActorZ              = 5600,
        ActorY              = 147040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_32A",          # 00, 0
        "Function_1_349",          # 01, 1
        "Function_2_642",          # 02, 2
        "Function_3_1038",         # 03, 3
        "Function_4_1174",         # 04, 4
        "Function_5_12E8",         # 05, 5
        "Function_6_1431",         # 06, 6
        "Function_7_1578",         # 07, 7
        "Function_8_1703",         # 08, 8
        "Function_9_185C",         # 09, 9
        "Function_10_1996",        # 0A, 10
        "Function_11_1B1C",        # 0B, 11
        "Function_12_1C29",        # 0C, 12
        "Function_13_1CAA",        # 0D, 13
        "Function_14_1DA5",        # 0E, 14
        "Function_15_1E1D",        # 0F, 15
        "Function_16_1EFC",        # 10, 16
        "Function_17_1FDB",        # 11, 17
        "Function_18_2029",        # 12, 18
        "Function_19_2077",        # 13, 19
    )


    def Function_0_32A(): pass

    label("Function_0_32A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_33A"),
        (101, "loc_341"),
        (SWITCH_DEFAULT, "loc_348"),
    )


    label("loc_33A")

    Event(0, 11)
    Jump("loc_348")

    label("loc_341")

    Event(0, 13)
    Jump("loc_348")

    label("loc_348")

    Return()

    # Function_0_32A end

    def Function_1_349(): pass

    label("Function_1_349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35B")
    OP_6F(0xA, 0)
    Jump("loc_362")

    label("loc_35B")

    OP_6F(0xA, 60)

    label("loc_362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_374")
    OP_6F(0xB, 0)
    Jump("loc_37B")

    label("loc_374")

    OP_6F(0xB, 60)

    label("loc_37B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38D")
    OP_6F(0xC, 0)
    Jump("loc_394")

    label("loc_38D")

    OP_6F(0xC, 60)

    label("loc_394")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A6")
    OP_6F(0xD, 0)
    Jump("loc_3AD")

    label("loc_3A6")

    OP_6F(0xD, 60)

    label("loc_3AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BF")
    OP_6F(0xE, 0)
    Jump("loc_3C6")

    label("loc_3BF")

    OP_6F(0xE, 60)

    label("loc_3C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D8")
    OP_6F(0xF, 0)
    Jump("loc_3DF")

    label("loc_3D8")

    OP_6F(0xF, 60)

    label("loc_3DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F1")
    OP_6F(0x11, 0)
    Jump("loc_3F8")

    label("loc_3F1")

    OP_6F(0x11, 60)

    label("loc_3F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40A")
    OP_6F(0x12, 0)
    Jump("loc_411")

    label("loc_40A")

    OP_6F(0x12, 60)

    label("loc_411")

    LoadEffect(0x0, "map\\\\mp049_21.eff")
    LoadEffect(0x1, "map\\\\mp049_22.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D5, 7)), scpexpr(EXPR_END)), "loc_445")
    SetChrFlags(0x8, 0x80)

    label("loc_445")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D6, 0)), scpexpr(EXPR_END)), "loc_451")
    SetChrFlags(0x9, 0x80)

    label("loc_451")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D6, 1)), scpexpr(EXPR_END)), "loc_45D")
    SetChrFlags(0xA, 0x80)

    label("loc_45D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D6, 2)), scpexpr(EXPR_END)), "loc_469")
    SetChrFlags(0xB, 0x80)

    label("loc_469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D6, 3)), scpexpr(EXPR_END)), "loc_475")
    SetChrFlags(0xC, 0x80)

    label("loc_475")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D6, 4)), scpexpr(EXPR_END)), "loc_481")
    SetChrFlags(0xD, 0x80)

    label("loc_481")

    OP_10(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C4, 2)), scpexpr(EXPR_END)), "loc_527")
    OP_72(0x0, 0x20)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    OP_72(0x4, 0x20)
    OP_72(0x5, 0x20)
    OP_72(0x6, 0x20)
    OP_72(0x8, 0x20)
    OP_72(0x9, 0x20)
    OP_72(0x0, 0x8)
    OP_72(0x1, 0x8)
    OP_72(0x2, 0x8)
    OP_72(0x3, 0x8)
    OP_72(0x4, 0x8)
    OP_72(0x5, 0x8)
    OP_72(0x6, 0x8)
    OP_72(0x8, 0x8)
    OP_72(0x9, 0x8)
    OP_6F(0x0, 360)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_6F(0x5, 0)
    OP_6F(0x6, 0)
    OP_6F(0x8, 0)
    OP_6F(0x9, 0)
    Jump("loc_5C0")

    label("loc_527")

    OP_72(0x0, 0x20)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    OP_72(0x4, 0x20)
    OP_72(0x5, 0x20)
    OP_72(0x6, 0x20)
    OP_72(0x8, 0x20)
    OP_72(0x9, 0x20)
    OP_72(0x0, 0x8)
    OP_72(0x1, 0x8)
    OP_72(0x2, 0x8)
    OP_72(0x3, 0x8)
    OP_72(0x4, 0x8)
    OP_72(0x5, 0x8)
    OP_72(0x6, 0x8)
    OP_72(0x8, 0x8)
    OP_72(0x9, 0x8)
    OP_6F(0x0, 0)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_6F(0x5, 0)
    OP_6F(0x6, 0)
    OP_6F(0x8, 0)
    OP_6F(0x9, 0)

    label("loc_5C0")

    OP_1B(0x0, 0x0, 0xC)
    OP_1B(0x1, 0x0, 0xE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_635")
    LoadEffect(0x2, "map\\\\mp027_00.eff")
    PlayEffect(0x2, 0x2, 0xFF, -3990, 5600, 147040, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_71(0x13, 0x20)
    OP_6F(0x13, 0)
    OP_70(0x13, 0xFA)
    Jump("loc_641")

    label("loc_635")

    OP_72(0x13, 0x20)
    OP_6F(0x13, 250)

    label("loc_641")

    Return()

    # Function_1_349 end

    def Function_2_642(): pass

    label("Function_2_642")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C16")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    OP_B0(0x0, 0x78)
    OP_70(0x0, 0x168)
    Sleep(2500)
    OP_22(0x9D, 0x0, 0x64)
    OP_B0(0x4, 0x64)
    OP_B0(0x5, 0x64)
    OP_B0(0x6, 0x64)
    OP_B0(0x7, 0x64)
    OP_B0(0x8, 0x64)
    OP_70(0x4, 0xF0)
    Sleep(100)
    OP_70(0x5, 0xF0)
    Sleep(100)
    OP_70(0x6, 0xF0)
    Sleep(100)
    OP_70(0x7, 0xF0)
    Sleep(100)
    OP_70(0x8, 0xF0)
    Sleep(100)
    OP_22(0xB9, 0x0, 0x64)
    OP_B0(0x1, 0x64)
    OP_B0(0x2, 0x64)
    OP_B0(0x3, 0x64)
    OP_70(0x1, 0x168)
    OP_70(0x2, 0x168)
    OP_70(0x3, 0x168)
    OP_73(0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #0
        (
            "\x07\x05#1S[About the Aureole's Seal (4/4)] ■ light ■■■■■\x01",
            "fr■m ■■■ facility, ■■■■ected off ■■■ ■■■■■ wall\x01",
            "of the ■■ne■b■■g, ca■■ht the ■■■■■■■ ■■oat■■g ■■\x01",
            "■■■ sky. In ■■■■ mo■■■■, ■■■ Aureole ■■■■■■■■■■■\x01",
            "■■■■ us, ■■■ ■■■ ■■■erie stopped ■nt■■ely.\x01",
            "Through ■■■s, we k■■w that the ■■■■■ ■■■■■■■ was\x01",
            "successful.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #1
        (
            "\x07\x05#1S■■■ Aureole ■■, of ■■■ ■■■■■■■■■■■, the tre■■■re\x01",
            "gov■■■■■■ the power ■■ Space. ■■■■ was ■■eded to\x01",
            "nul■■■■ ■■■ Aureole, ■■■■ held abs■■■te dom■■■■■\x01",
            "■■■■ space itself, ■■■ to utterly sever ■■■\x01",
            "■■■■■ctions ■■ space, ■■■ ■■■■■■ ■■■■ ■■ ■■■■\x01",
            "■■■■■■. ■■■ Seal ■■■■■■■■■, ■■■■ ■■ ■■■ hard\x01",
            "■■■■, had sent ■■■ ■■■■■■■, ■■■■■ ■■■■ ■■■\x01",
            "■■■■■■ city, into ■■■■■■■ ■■■■■■■■■ a■d\x01",
            "■■■■essfully te■■■■■■■■ froze ■■.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #2
        "\x07\x00Received #1032i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x408, 1)
    OP_A2(0x1E22)
    Sleep(100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x0, 360)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_6F(0x5, 0)
    OP_6F(0x6, 0)
    OP_6F(0x7, 0)
    OP_6F(0x8, 0)
    OP_6D(520, 200, 36750, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 520, 200, 36750, 0)
    SetChrPos(0x1, 520, 200, 36750, 0)
    SetChrPos(0x2, 520, 200, 36750, 0)
    SetChrPos(0x3, 520, 200, 36750, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Jump("loc_1034")

    label("loc_C16")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #3
        (
            "\x07\x05#1S[About the Aureole's Seal (4/4)] ■ light ■■■■■\x01",
            "fr■m ■■■ facility, ■■■■ected off ■■■ ■■■■■ wall\x01",
            "of the ■■ne■b■■g, ca■■ht the ■■■■■■■ ■■oat■■g ■■\x01",
            "■■■ sky. In ■■■■ mo■■■■, ■■■ Aureole ■■■■■■■■■■■\x01",
            "■■■■ us, ■■■ ■■■ ■■■erie stopped ■nt■■ely.\x01",
            "Through ■■■s, we k■■w that the ■■■■■ ■■■■■■■ was\x01",
            "successful.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #4
        (
            "\x07\x05#1S■■■ Aureole ■■, of ■■■ ■■■■■■■■■■■, the tre■■■re\x01",
            "gov■■■■■■ the power ■■ Space. ■■■■ was ■■eded to\x01",
            "nul■■■■ ■■■ Aureole, ■■■■ held abs■■■te dom■■■■■\x01",
            "■■■■ space itself, ■■■ to utterly sever ■■■\x01",
            "■■■■■ctions ■■ space, ■■■ ■■■■■■ ■■■■ ■■ ■■■■\x01",
            "■■■■■■. ■■■ Seal ■■■■■■■■■, ■■■■ ■■ ■■■ hard\x01",
            "■■■■, had sent ■■■ ■■■■■■■, ■■■■■ ■■■■ ■■■\x01",
            "■■■■■■ city, into ■■■■■■■ ■■■■■■■■■ a■d\x01",
            "■■■■essfully te■■■■■■■■ froze ■■.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1034")

    TalkEnd(0xFF)
    Return()

    # Function_2_642 end

    def Function_3_1038(): pass

    label("Function_3_1038")

    OP_EA(0x2, 0x9C, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1110")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xA, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_10A9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "Found \x1F\xFC\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F82)
    Jump("loc_110D")

    label("loc_10A9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "Found \x1F\xFC\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFC\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xA, 60)
    OP_70(0xA, 0x0)

    label("loc_110D")

    Jump("loc_1166")

    label("loc_1110")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x05There's this great story I want to Estell you\x01",
            "sometime.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1166")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_1038 end

    def Function_4_1174(): pass

    label("Function_4_1174")

    OP_EA(0x2, 0x9D, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_124C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xB, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x142, 1)"), scpexpr(EXPR_END)), "loc_11E5")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "Found \x1F\x42\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F83)
    Jump("loc_1249")

    label("loc_11E5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "Found \x1F\x42\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x42\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xB, 60)
    OP_70(0xB, 0x0)

    label("loc_1249")

    Jump("loc_12DA")

    label("loc_124C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "\x07\x05Lamenting the lack of items in the chest, you\x01",
            "ponder the merits of wearing the chest itself as\x01",
            "makeshift armor.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_12DA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_1174 end

    def Function_5_12E8(): pass

    label("Function_5_12E8")

    OP_EA(0x2, 0x9E, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13C0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xC, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x201, 1)"), scpexpr(EXPR_END)), "loc_1359")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #11
        "Found \x1F\x01\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F84)
    Jump("loc_13BD")

    label("loc_1359")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "Found \x1F\x01\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x01\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xC, 60)
    OP_70(0xC, 0x0)

    label("loc_13BD")

    Jump("loc_1423")

    label("loc_13C0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "\x07\x05This chest is as empty as that promise you\x01",
            "made. You know which one.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1423")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_12E8 end

    def Function_6_1431(): pass

    label("Function_6_1431")

    OP_EA(0x2, 0x9F, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1509")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xD, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_14A2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #14
        "Found \x1F\xF9\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F85)
    Jump("loc_1506")

    label("loc_14A2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "Found \x1F\xF9\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF9\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xD, 60)
    OP_70(0xD, 0x0)

    label("loc_1506")

    Jump("loc_156A")

    label("loc_1509")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "\x07\x05Dogi the Wall Crusher's got nothing on Estelle\x01",
            "the Treasure Taker.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_156A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1431 end

    def Function_7_1578(): pass

    label("Function_7_1578")

    OP_EA(0x2, 0xA0, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1650")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xE, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x187, 1)"), scpexpr(EXPR_END)), "loc_15E9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #17
        "Found \x1F\x87\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F86)
    Jump("loc_164D")

    label("loc_15E9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "Found \x1F\x87\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x87\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xE, 60)
    OP_70(0xE, 0x0)

    label("loc_164D")

    Jump("loc_16F5")

    label("loc_1650")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        (
            "\x07\x05Once you notice that this treasure chest is\x01",
            "slowly protruding its sharp fangs from the edges\x01",
            "of its lid, you back away slowly and run.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_16F5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1578 end

    def Function_8_1703(): pass

    label("Function_8_1703")

    OP_EA(0x2, 0xA1, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17DB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xF, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_1774")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #20
        "Found \x1F\xF7\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F88)
    Jump("loc_17D8")

    label("loc_1774")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "Found \x1F\xF7\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF7\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xF, 60)
    OP_70(0xF, 0x0)

    label("loc_17D8")

    Jump("loc_184E")

    label("loc_17DB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #22
        (
            "\x07\x05A cube has six faces, but none of them look as\x01",
            "disappointed as yours does right now.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_184E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_1703 end

    def Function_9_185C(): pass

    label("Function_9_185C")

    OP_EA(0x2, 0xA2, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1934")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x11, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x157, 1)"), scpexpr(EXPR_END)), "loc_18CD")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #23
        "Found \x1F\x57\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F89)
    Jump("loc_1931")

    label("loc_18CD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #24
        (
            "Found \x1F\x57\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x57\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x11, 60)
    OP_70(0x11, 0x0)

    label("loc_1931")

    Jump("loc_1988")

    label("loc_1934")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #25
        (
            "\x07\x05Life is what happens between opening treasure\x01",
            "chests.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1988")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_185C end

    def Function_10_1996(): pass

    label("Function_10_1996")

    OP_EA(0x2, 0xA3, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A6E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x12, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x299, 1)"), scpexpr(EXPR_END)), "loc_1A07")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #26
        "Found \x1F\x99\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F8A)
    Jump("loc_1A6B")

    label("loc_1A07")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #27
        (
            "Found \x1F\x99\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x99\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x12, 60)
    OP_70(0x12, 0x0)

    label("loc_1A6B")

    Jump("loc_1B0E")

    label("loc_1A6E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #28
        (
            "\x07\x05Pawing around at the bottom of the chest,\x01",
            "you find a small door. Opening it, you see...\x01",
            "the ground. Well, that was underwhelming.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1B0E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_1996 end

    def Function_11_1B1C(): pass

    label("Function_11_1B1C")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 250, -66500, 0)
    OP_6C(225000, 0)
    SetChrPos(0x101, -500, 250, -66000, 0)
    SetChrPos(0x102, 500, 250, -66000, 0)
    SetChrPos(0xF8, -500, 250, -67000, 0)
    SetChrPos(0xF9, 500, 250, -67000, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 15)
    Call(0, 17)
    Fade(500)
    OP_6D(-110, 250, -64580, 0)
    OP_6C(315000, 0)
    SetChrPos(0x0, -110, 250, -64580, 0)
    SetChrPos(0x1, -110, 250, -64580, 0)
    SetChrPos(0x2, -110, 250, -64580, 0)
    SetChrPos(0x3, -110, 250, -64580, 0)
    EventEnd(0x0)
    Return()

    # Function_11_1B1C end

    def Function_12_1C29(): pass

    label("Function_12_1C29")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 250, -66500, 0)
    OP_6C(225000, 0)
    SetChrPos(0x101, 500, 250, -67000, 180)
    SetChrPos(0x102, -500, 250, -67000, 180)
    SetChrPos(0xF8, 500, 250, -66000, 180)
    SetChrPos(0xF9, -500, 250, -66000, 180)
    OP_0D()
    Call(0, 15)
    Call(0, 18)
    NewScene("ED6_DT21/C2303   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1C29 end

    def Function_13_1CAA(): pass

    label("Function_13_1CAA")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 5050, 154000, 0)
    SetChrPos(0x101, 500, 5050, 153500, 180)
    SetChrPos(0x102, -500, 5050, 153500, 180)
    SetChrPos(0xF8, 500, 5050, 154500, 180)
    SetChrPos(0xF9, -500, 5050, 154500, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 15)
    Call(0, 17)
    Fade(500)
    OP_6D(0, 4700, 151670, 0)
    SetChrPos(0x0, 0, 4700, 151670, 180)
    SetChrPos(0x1, 0, 4700, 151670, 180)
    SetChrPos(0x2, 0, 4700, 151670, 180)
    SetChrPos(0x3, 0, 4700, 151670, 180)
    EventEnd(0x0)
    Return()

    # Function_13_1CAA end

    def Function_14_1DA5(): pass

    label("Function_14_1DA5")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 5050, 154000, 0)
    SetChrPos(0x101, -500, 5050, 154500, 0)
    SetChrPos(0x102, 500, 5050, 154500, 0)
    SetChrPos(0xF8, -500, 5050, 153500, 0)
    SetChrPos(0xF9, 500, 5050, 153500, 0)
    OP_0D()
    Call(0, 15)
    Call(0, 18)
    NewScene("ED6_DT21/C2305   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_1DA5 end

    def Function_15_1E1D(): pass

    label("Function_15_1E1D")

    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_15_1E1D end

    def Function_16_1EFC(): pass

    label("Function_16_1EFC")

    PlayEffect(0x1, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_16_1EFC end

    def Function_17_1FDB(): pass

    label("Function_17_1FDB")


    def lambda_1FE1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1FE1)

    def lambda_1FF3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1FF3)

    def lambda_2005():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2005)

    def lambda_2017():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2017)
    Sleep(2500)
    Return()

    # Function_17_1FDB end

    def Function_18_2029(): pass

    label("Function_18_2029")


    def lambda_202F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_202F)

    def lambda_2041():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2041)

    def lambda_2053():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2053)

    def lambda_2065():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2065)
    Sleep(2000)
    Return()

    # Function_18_2029 end

    def Function_19_2077(): pass

    label("Function_19_2077")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20DD")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #29
        "\x07\x05Orbal energy appears to be shut down.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_227F")

    label("loc_20DD")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #30
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2264")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_72(0x13, 0x20)
    OP_6F(0x13, 300)
    OP_70(0x13, 0x1F4)
    OP_73(0x13)
    OP_6F(0x13, 500)
    OP_70(0x13, 0x2BC)
    OP_71(0x13, 0x20)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x2, 0x2)
    LoadEffect(0x3, "map\\\\mp027_01.eff")
    PlayEffect(0x3, 0x3, 0xFF, -3990, 5600, 147040, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1500, 0, -1)
    Sleep(1500)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x3, 0x2)
    PlayEffect(0x2, 0x2, 0xFF, -3990, 5600, 147040, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x13, 0)
    OP_70(0x13, 0xFA)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_2264")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_227E")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_227E")

    Return()

    label("loc_227F")

    Return()

    # Function_19_2077 end

    SaveToFile()

Try(main)
