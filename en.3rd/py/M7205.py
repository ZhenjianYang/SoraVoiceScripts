from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7205   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7205.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60223",
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
        'ED6_DT29/CH14470 ._CH',             # 00
        'ED6_DT29/CH14471 ._CH',             # 01
        'ED6_DT29/CH15050 ._CH',             # 02
        'ED6_DT29/CH15051 ._CH',             # 03
        'ED6_DT29/CH15060 ._CH',             # 04
        'ED6_DT29/CH15061 ._CH',             # 05
        'ED6_DT29/CH14480 ._CH',             # 06
        'ED6_DT29/CH14481 ._CH',             # 07
        'ED6_DT29/CH14490 ._CH',             # 08
        'ED6_DT29/CH14491 ._CH',             # 09
        'ED6_DT29/CH14560 ._CH',             # 0A
        'ED6_DT29/CH14561 ._CH',             # 0B
        'ED6_DT29/CH14010 ._CH',             # 0C
        'ED6_DT29/CH14011 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT29/CH14470P._CP',             # 00
        'ED6_DT29/CH14471P._CP',             # 01
        'ED6_DT29/CH15050P._CP',             # 02
        'ED6_DT29/CH15051P._CP',             # 03
        'ED6_DT29/CH15060P._CP',             # 04
        'ED6_DT29/CH15061P._CP',             # 05
        'ED6_DT29/CH14480P._CP',             # 06
        'ED6_DT29/CH14481P._CP',             # 07
        'ED6_DT29/CH14490P._CP',             # 08
        'ED6_DT29/CH14491P._CP',             # 09
        'ED6_DT29/CH14560P._CP',             # 0A
        'ED6_DT29/CH14561P._CP',             # 0B
        'ED6_DT29/CH14010P._CP',             # 0C
        'ED6_DT29/CH14011P._CP',             # 0D
    )

    DeclMonster(
        X                   = -400,
        Z                   = -10450,
        Y                   = -43830,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 23540,
        Z                   = -18450,
        Y                   = -55220,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 38040,
        Z                   = -22650,
        Y                   = 5800,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1FA,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -37510,
        Z                   = -22650,
        Y                   = 5330,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -6940,
        Z                   = -6200,
        Y                   = 47340,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 6940,
        Z                   = 13800,
        Y                   = 46980,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 0,
        TriggerZ            = -10400,
        TriggerY            = -44000,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = -9400,
        ActorY              = -44000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 25000,
        TriggerZ            = -18400,
        TriggerY            = -54000,
        TriggerRange        = 1000,
        ActorX              = 25000,
        ActorZ              = -17400,
        ActorY              = -54000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 38000,
        TriggerZ            = -22650,
        TriggerY            = 5000,
        TriggerRange        = 1000,
        ActorX              = 38000,
        ActorZ              = -21650,
        ActorY              = 5000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -38000,
        TriggerZ            = -22650,
        TriggerY            = 5000,
        TriggerRange        = 1000,
        ActorX              = -38000,
        ActorZ              = -21650,
        ActorY              = 5000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5680,
        TriggerZ            = 25800,
        TriggerY            = 48000,
        TriggerRange        = 1000,
        ActorX              = 5680,
        ActorZ              = 26800,
        ActorY              = 48000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_276",          # 00, 0
        "Function_1_2CD",          # 01, 1
        "Function_2_386",          # 02, 2
        "Function_3_4A3",          # 03, 3
        "Function_4_5F1",          # 04, 4
        "Function_5_7D0",          # 05, 5
        "Function_6_8A4",          # 06, 6
        "Function_7_A6B",          # 07, 7
        "Function_8_B49",          # 08, 8
        "Function_9_C27",          # 09, 9
        "Function_10_D05",         # 0A, 10
        "Function_11_DE3",         # 0B, 11
        "Function_12_EC1",         # 0C, 12
        "Function_13_F9F",         # 0D, 13
        "Function_14_105B",        # 0E, 14
        "Function_15_1117",        # 0F, 15
        "Function_16_11D3",        # 10, 16
        "Function_17_128F",        # 11, 17
        "Function_18_134B",        # 12, 18
        "Function_19_1407",        # 13, 19
        "Function_20_151D",        # 14, 20
    )


    def Function_0_276(): pass

    label("Function_0_276")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CC")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_2A2"),
        (101, "loc_2A9"),
        (102, "loc_2B0"),
        (103, "loc_2B7"),
        (104, "loc_2BE"),
        (105, "loc_2C5"),
        (SWITCH_DEFAULT, "loc_2CC"),
    )


    label("loc_2A2")

    Event(0, 7)
    Jump("loc_2CC")

    label("loc_2A9")

    Event(0, 8)
    Jump("loc_2CC")

    label("loc_2B0")

    Event(0, 10)
    Jump("loc_2CC")

    label("loc_2B7")

    Event(0, 11)
    Jump("loc_2CC")

    label("loc_2BE")

    Event(0, 12)
    Jump("loc_2CC")

    label("loc_2C5")

    Event(0, 9)
    Jump("loc_2CC")

    label("loc_2CC")

    Return()

    # Function_0_276 end

    def Function_1_2CD(): pass

    label("Function_1_2CD")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE5638, 0x230090)
    OP_1B(0x0, 0x0, 0xD)
    OP_1B(0x1, 0x0, 0xE)
    OP_1B(0x2, 0x0, 0x10)
    OP_1B(0x3, 0x0, 0x11)
    OP_1B(0x4, 0x0, 0x12)
    OP_1B(0x5, 0x0, 0xF)
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x554, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31A")
    OP_6F(0x2, 0)
    Jump("loc_321")

    label("loc_31A")

    OP_6F(0x2, 60)

    label("loc_321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x554, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_333")
    OP_6F(0x3, 0)
    Jump("loc_33A")

    label("loc_333")

    OP_6F(0x3, 60)

    label("loc_33A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x554, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34C")
    OP_6F(0x4, 0)
    Jump("loc_353")

    label("loc_34C")

    OP_6F(0x4, 60)

    label("loc_353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x554, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_365")
    OP_6F(0x5, 0)
    Jump("loc_36C")

    label("loc_365")

    OP_6F(0x5, 60)

    label("loc_36C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x554, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37E")
    OP_6F(0x6, 0)
    Jump("loc_385")

    label("loc_37E")

    OP_6F(0x6, 60)

    label("loc_385")

    Return()

    # Function_1_2CD end

    def Function_2_386(): pass

    label("Function_2_386")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x554, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_3F4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\xFD\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2AA0)
    Jump("loc_45C")

    label("loc_3F4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\xFD\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xFD\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_45C")

    Jump("loc_495")

    label("loc_45F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05We are both empty.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xDD, 0x0)

    label("loc_495")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_386 end

    def Function_3_4A3(): pass

    label("Function_3_4A3")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x554, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x18D, 1)"), scpexpr(EXPR_END)), "loc_511")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Found \x1F\x8D\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2AA1)
    Jump("loc_579")

    label("loc_511")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Found \x1F\x8D\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x8D\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_579")

    Jump("loc_5E3")

    label("loc_57C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05You're the sister here. Does 'Thou shall not steal' ring any bells?\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xDE, 0x0)

    label("loc_5E3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_4A3 end

    def Function_4_5F1(): pass

    label("Function_4_5F1")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x554, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x5B3, 1)"), scpexpr(EXPR_END)), "loc_65F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05Found \x1F\xB3\x05\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2AA2)
    Jump("loc_6C7")

    label("loc_65F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x05Found \x1F\xB3\x05\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xB3\x05\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_6C7")

    Jump("loc_7C2")

    label("loc_6CA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "\x07\x05[26/36] She sighed in a way that was half frustrated, half disappointed.\x01",
            "She never cared about money. Why would he try to win an argument with\x01",
            "it? She could only say quietly in her mind, 'My husband is an idiot.'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xDF, 0x0)

    label("loc_7C2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_5F1 end

    def Function_5_7D0(): pass

    label("Function_5_7D0")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x554, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x1E)
    OP_73(0x5)
    OP_6F(0x5, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(3000)

    AnonymousTalk(    #9
        "\x07\x05Received \x07\x023,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2AA3)
    Jump("loc_88D")

    label("loc_83D")


    AnonymousTalk(    #10
        "\x07\x05Empty. Someone must have taken the chest phrase that used to be in here.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_88D")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0xE0, 0x0)
    Return()

    # Function_5_7D0 end

    def Function_6_8A4(): pass

    label("Function_6_8A4")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x554, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B4")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x1E)
    OP_73(0x6)
    OP_6F(0x6, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 0xC8)
    AddSepith(0x1, 0xC8)
    AddSepith(0x2, 0xC8)
    AddSepith(0x3, 0xC8)
    AddSepith(0x4, 0xC8)
    AddSepith(0x5, 0xC8)
    AddSepith(0x6, 0xC8)

    AnonymousTalk(    #11
        (
            "\x07\x02Obtained:\x01",
            "#56IEarth Sepith x200\x01",
            "#57IWater Sepith x200\x01",
            "#58IFire Sepith x200\x01",
            "#59IWind Sepith x200\x01",
            "#62ITime Sepith x200\x01",
            "#60ISpace Sepith x200\x01",
            "#61IMirage Sepith x200.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2AA4)
    Jump("loc_A54")

    label("loc_9B4")


    AnonymousTalk(    #12
        (
            "\x07\x05(5/12) 'Certainly! Come on in.' Hideko would listen to anything Sato had\x01",
            "to say. But no one could know the horrible fate that awaited Hideko this\x01",
            "day...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_A54")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0xE1, 0x0)
    Return()

    # Function_6_8A4 end

    def Function_7_A6B(): pass

    label("Function_7_A6B")

    OP_DE(0x0, 0x0, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 36020, -10450, -25020, 225)
    SetChrPos(0x1, 36020, -10450, -25020, 225)
    SetChrPos(0x2, 36020, -10450, -25020, 225)
    SetChrPos(0x3, 36020, -10450, -25020, 225)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 36020, -10450, -25020, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 19)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x150), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_7_A6B end

    def Function_8_B49(): pass

    label("Function_8_B49")

    OP_DE(0x0, 0x1, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -35910, -10450, -25140, 135)
    SetChrPos(0x1, -35910, -10450, -25140, 135)
    SetChrPos(0x2, -35910, -10450, -25140, 135)
    SetChrPos(0x3, -35910, -10450, -25140, 135)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -35910, -10450, -25140, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 19)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x150), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_8_B49 end

    def Function_9_C27(): pass

    label("Function_9_C27")

    OP_DE(0x0, 0x5, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -24550, -18360, -54510, 135)
    SetChrPos(0x1, -24550, -18360, -54510, 135)
    SetChrPos(0x2, -24550, -18360, -54510, 135)
    SetChrPos(0x3, -24550, -18360, -54510, 135)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -24550, -17360, -54510, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 19)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x150), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_9_C27 end

    def Function_10_D05(): pass

    label("Function_10_D05")

    OP_DE(0x0, 0x2, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 37890, -18560, 44930, 180)
    SetChrPos(0x1, 37890, -18560, 44930, 180)
    SetChrPos(0x2, 37890, -18560, 44930, 180)
    SetChrPos(0x3, 37890, -18560, 44930, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 37890, -18560, 44930, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 19)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x150), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_10_D05 end

    def Function_11_DE3(): pass

    label("Function_11_DE3")

    OP_DE(0x0, 0x3, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -38070, -18560, 44870, 180)
    SetChrPos(0x1, -38070, -18560, 44870, 180)
    SetChrPos(0x2, -38070, -18560, 44870, 180)
    SetChrPos(0x3, -38070, -18560, 44870, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -38070, -18560, 44870, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 19)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x150), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_11_DE3 end

    def Function_12_EC1(): pass

    label("Function_12_EC1")

    OP_DE(0x0, 0x4, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -10, -14110, -11990, 0)
    SetChrPos(0x1, -10, -14110, -11990, 0)
    SetChrPos(0x2, -10, -14110, -11990, 0)
    SetChrPos(0x3, -10, -14110, -11990, 0)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -10, -14110, -11990, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 19)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x150), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_12_EC1 end

    def Function_13_F9F(): pass

    label("Function_13_F9F")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 36020, -10450, -25020, 45)
    SetChrPos(0x2, 36020, -10450, -25020, 45)
    SetChrPos(0x1, 36020, -10450, -25020, 45)
    SetChrPos(0x0, 36020, -10450, -25020, 45)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 36020, -10450, -25020, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 20)
    NewScene("ED6_DT21/M7204   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_13_F9F end

    def Function_14_105B(): pass

    label("Function_14_105B")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -35910, -10450, -25140, 315)
    SetChrPos(0x2, -35910, -10450, -25140, 315)
    SetChrPos(0x1, -35910, -10450, -25140, 315)
    SetChrPos(0x0, -35910, -10450, -25140, 315)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -35910, -10450, -25140, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 20)
    NewScene("ED6_DT21/M7204   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_14_105B end

    def Function_15_1117(): pass

    label("Function_15_1117")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -24550, -18360, -54510, 315)
    SetChrPos(0x2, -24550, -18360, -54510, 315)
    SetChrPos(0x1, -24550, -18360, -54510, 315)
    SetChrPos(0x0, -24550, -18360, -54510, 315)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -24550, -17360, -54510, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 20)
    NewScene("ED6_DT21/M7204   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_15_1117 end

    def Function_16_11D3(): pass

    label("Function_16_11D3")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 37890, -18560, 44930, 0)
    SetChrPos(0x2, 37890, -18560, 44930, 0)
    SetChrPos(0x1, 37890, -18560, 44930, 0)
    SetChrPos(0x0, 37890, -18560, 44930, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 37890, -18560, 44930, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 20)
    NewScene("ED6_DT21/M7204   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_16_11D3 end

    def Function_17_128F(): pass

    label("Function_17_128F")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -38070, -18560, 44870, 0)
    SetChrPos(0x2, -38070, -18560, 44870, 0)
    SetChrPos(0x1, -38070, -18560, 44870, 0)
    SetChrPos(0x0, -38070, -18560, 44870, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -38070, -18560, 44870, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 20)
    NewScene("ED6_DT21/M7205   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_17_128F end

    def Function_18_134B(): pass

    label("Function_18_134B")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -10, -14110, -11990, 180)
    SetChrPos(0x2, -10, -14110, -11990, 180)
    SetChrPos(0x1, -10, -14110, -11990, 180)
    SetChrPos(0x0, -10, -14110, -11990, 180)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -10, -14110, -11990, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 20)
    NewScene("ED6_DT21/M7205   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_18_134B end

    def Function_19_1407(): pass

    label("Function_19_1407")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1430")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1424():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1424)

    label("loc_1430")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1459")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_144D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_144D)

    label("loc_1459")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1482")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1476():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1476)

    label("loc_1482")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14AB")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_149F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_149F)

    label("loc_14AB")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14D7")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_14D7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14EE")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_14EE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1505")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1505")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_151C")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_151C")

    Return()

    # Function_19_1407 end

    def Function_20_151D(): pass

    label("Function_20_151D")


    def lambda_1523():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1523)

    def lambda_1535():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1535)

    def lambda_1547():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1547)

    def lambda_1559():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1559)
    Sleep(1000)
    Return()

    # Function_20_151D end

    SaveToFile()

Try(main)
