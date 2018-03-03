from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7103   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7103.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60222",
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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
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
        'ED6_DT29/CH14070 ._CH',             # 00
        'ED6_DT29/CH14071 ._CH',             # 01
        'ED6_DT29/CH14830 ._CH',             # 02
        'ED6_DT29/CH14831 ._CH',             # 03
        'ED6_DT29/CH14910 ._CH',             # 04
        'ED6_DT29/CH14911 ._CH',             # 05
        'ED6_DT29/CH14920 ._CH',             # 06
        'ED6_DT29/CH14921 ._CH',             # 07
        'ED6_DT29/CH14930 ._CH',             # 08
        'ED6_DT29/CH14931 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT29/CH14070P._CP',             # 00
        'ED6_DT29/CH14071P._CP',             # 01
        'ED6_DT29/CH14830P._CP',             # 02
        'ED6_DT29/CH14831P._CP',             # 03
        'ED6_DT29/CH14910P._CP',             # 04
        'ED6_DT29/CH14911P._CP',             # 05
        'ED6_DT29/CH14920P._CP',             # 06
        'ED6_DT29/CH14921P._CP',             # 07
        'ED6_DT29/CH14930P._CP',             # 08
        'ED6_DT29/CH14931P._CP',             # 09
    )

    DeclMonster(
        X                   = 50,
        Z                   = -4000,
        Y                   = -28190,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x138,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -36310,
        Z                   = 0,
        Y                   = -33290,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x134,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -34580,
        Z                   = 0,
        Y                   = -13200,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x135,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -36160,
        Z                   = 0,
        Y                   = 6770,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x136,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 35310,
        Z                   = 8000,
        Y                   = -3240,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x137,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 37950,
        Z                   = 8000,
        Y                   = 16880,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x138,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 34960,
        Z                   = 8000,
        Y                   = 36270,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x134,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -50,
        TriggerZ            = 4000,
        TriggerY            = 2050,
        TriggerRange        = 1000,
        ActorX              = -50,
        ActorZ              = 5000,
        ActorY              = 2050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 12000,
        TriggerY            = 32060,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = 14000,
        ActorY              = 32060,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -36000,
        TriggerZ            = 0,
        TriggerY            = -4330,
        TriggerRange        = 1000,
        ActorX              = -36000,
        ActorZ              = 1000,
        ActorY              = -4330,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 35990,
        TriggerZ            = 8000,
        TriggerY            = 25790,
        TriggerRange        = 1000,
        ActorX              = 35990,
        ActorZ              = 9000,
        ActorY              = 25790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 36000,
        TriggerZ            = 8000,
        TriggerY            = 8000,
        TriggerRange        = 1000,
        ActorX              = 36000,
        ActorZ              = 9000,
        ActorY              = 8000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -36000,
        TriggerZ            = 0,
        TriggerY            = 12000,
        TriggerRange        = 1000,
        ActorX              = -36000,
        ActorZ              = 1000,
        ActorY              = 12000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_296",          # 00, 0
        "Function_1_2B6",          # 01, 1
        "Function_2_35C",          # 02, 2
        "Function_3_7A3",          # 03, 3
        "Function_4_916",          # 04, 4
        "Function_5_B9D",          # 05, 5
        "Function_6_C7B",          # 06, 6
        "Function_7_D37",          # 07, 7
        "Function_8_E4D",          # 08, 8
        "Function_9_E9B",          # 09, 9
        "Function_10_FF9",         # 0A, 10
        "Function_11_113C",        # 0B, 11
        "Function_12_1284",        # 0C, 12
    )


    def Function_0_296(): pass

    label("Function_0_296")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B5")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_2AE"),
        (SWITCH_DEFAULT, "loc_2B5"),
    )


    label("loc_2AE")

    Event(0, 5)
    Jump("loc_2B5")

    label("loc_2B5")

    Return()

    # Function_0_296 end

    def Function_1_2B6(): pass

    label("Function_1_2B6")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE0C00, 0x230086)
    OP_1B(0x0, 0x0, 0x6)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DE")
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x85, 0x0)

    label("loc_2DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x510, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F0")
    OP_6F(0x17, 0)
    Jump("loc_2F7")

    label("loc_2F0")

    OP_6F(0x17, 60)

    label("loc_2F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x513, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_309")
    OP_6F(0x19, 0)
    Jump("loc_310")

    label("loc_309")

    OP_6F(0x19, 60)

    label("loc_310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x513, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_322")
    OP_6F(0x1A, 0)
    Jump("loc_329")

    label("loc_322")

    OP_6F(0x1A, 60)

    label("loc_329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x513, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33B")
    OP_6F(0x1B, 0)
    Jump("loc_342")

    label("loc_33B")

    OP_6F(0x1B, 60)

    label("loc_342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x515, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_354")
    OP_6F(0x1C, 0)
    Jump("loc_35B")

    label("loc_354")

    OP_6F(0x1C, 60)

    label("loc_35B")

    Return()

    # Function_1_2B6 end

    def Function_2_35C(): pass

    label("Function_2_35C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x501, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_797")
    EventBegin(0x0)
    Fade(500)
    OP_6D(-240, 4000, 2620, 0)
    OP_67(-1000, 6950, -10000, 0)
    OP_6B(3490, 0)
    OP_6C(45000, 0)
    OP_6E(240, 0)
    SetChrPos(0x10F, -1060, 4000, 1910, 90)
    SetChrPos(0xF3, -2810, 4000, 1800, 90)
    SetChrPos(0xF4, -3400, 4000, 600, 90)
    SetChrPos(0xF5, -3660, 4000, 2430, 90)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(1000)
    OP_22(0x2B, 0x0, 0x64)
    OP_6F(0x17, 0)
    OP_70(0x17, 0x3C)
    OP_73(0x17)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Obtained \x1F\xAF\x05\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x5AF, 1)
    OP_A2(0x2881)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #1
        0x10F,
        (
            "#1444F#6P...What?!\x02\x03",

            "(This seems...familiar, somehow.)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54A")
    OP_62(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #2
        0x102,
        "#1504F#6PIs something wrong, Ries?\x02",
    )

    CloseMessageWindow()
    Jump("loc_697")

    label("loc_54A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_598")
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #3
        0x107,
        "#064F#6PIs something wrong?\x02",
    )

    CloseMessageWindow()
    Jump("loc_697")

    label("loc_598")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E6")
    OP_62(0x10B, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #4
        0x10B,
        "#213F#6PIs something wrong?\x02",
    )

    CloseMessageWindow()
    Jump("loc_697")

    label("loc_5E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_641")
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #5
        0x105,
        "#1164F#6PUmm... Is something the matter?\x02",
    )

    CloseMessageWindow()
    Jump("loc_697")

    label("loc_641")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_697")
    OP_62(0x10E, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #6
        0x10E,
        "#173F#6PIs something the matter, Ries?\x02",
    )

    CloseMessageWindow()

    label("loc_697")

    OP_63(0x10F)
    Sleep(100)
    OP_8C(0x10F, 270, 400)
    Sleep(300)

    ChrTalk(    #7
        0x10F,
        (
            "#1446F#11P...Not at all. I thought I may have seen this\x01",
            "weapon somewhere before, but it must have\x01",
            "been my imagination.\x02\x03",

            "#1448FIt certainly seems like a capable one, though...\x01",
            "So I think I'll use it all the same.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2809)
    OP_28(0x31, 0x1, 0x4)
    Sleep(500)
    EventEnd(0x0)
    Jump("loc_79B")

    label("loc_797")

    Call(0, 3)

    label("loc_79B")

    Jump("loc_7A2")

    label("loc_79E")

    Call(0, 3)

    label("loc_7A2")

    Return()

    # Function_2_35C end

    def Function_3_7A3(): pass

    label("Function_3_7A3")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x510, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x17, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x5AF, 1)"), scpexpr(EXPR_END)), "loc_811")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05Found \x1F\xAF\x05\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2881)
    Jump("loc_879")

    label("loc_811")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "\x07\x05Found \x1F\xAF\x05\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xAF\x05\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x17, 60)
    OP_70(0x17, 0x0)

    label("loc_879")

    Jump("loc_908")

    label("loc_87C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "\x07\x05Here's a crossbow for a CROSS BRO... Ahahaha... I don't actually have a\x01",
            "crossbow for you, Father. Sorry.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xC0, 0x0)

    label("loc_908")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_7A3 end

    def Function_4_916(): pass

    label("Function_4_916")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EA")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(2304)
    Sleep(500)
    OP_AA(65282)
    Jump("loc_9ED")

    label("loc_9EA")

    TalkBegin(0xFF)

    label("loc_9ED")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #11
        "\x07\x05Select an Option\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A29")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B6C")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Restore HP/EP\x01",          # 0
            "Shop\x01",                   # 1
            "Synthesize Quartz\x01",      # 2
            "End\x01",                    # 3
        )
    )

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A85"),
        (1, "loc_B00"),
        (2, "loc_B2E"),
        (SWITCH_DEFAULT, "loc_B5C"),
    )


    label("loc_A85")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1D(0xDE)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B69")

    label("loc_B00")

    OP_A9(0x1A)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #12
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_B69")

    label("loc_B2E")

    OP_A9(0x5)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #13
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_B69")

    label("loc_B5C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B69")

    label("loc_B69")

    Jump("loc_A29")

    label("loc_B6C")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B99")
    OP_A2(0x258C)
    EventEnd(0x1)
    Jump("loc_B9C")

    label("loc_B99")

    TalkEnd(0xFF)

    label("loc_B9C")

    Return()

    # Function_4_916 end

    def Function_5_B9D(): pass

    label("Function_5_B9D")

    OP_DE(0x0, 0x0, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -20, -7700, -66010, 0)
    SetChrPos(0x1, -20, -7700, -66010, 0)
    SetChrPos(0x2, -20, -7700, -66010, 0)
    SetChrPos(0x3, -20, -7700, -66010, 0)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -20, -7700, -66010, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 7)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_5_B9D end

    def Function_6_C7B(): pass

    label("Function_6_C7B")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x0, -20, -7700, -66010, 180)
    SetChrPos(0x1, -20, -7700, -66010, 180)
    SetChrPos(0x2, -20, -7700, -66010, 180)
    SetChrPos(0x3, -20, -7700, -66010, 180)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -20, -7700, -66010, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 8)
    NewScene("ED6_DT21/M7101   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_6_C7B end

    def Function_7_D37(): pass

    label("Function_7_D37")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D60")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_D54():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_D54)

    label("loc_D60")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D89")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_D7D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_D7D)

    label("loc_D89")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DB2")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_DA6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_DA6)

    label("loc_DB2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DDB")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_DCF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_DCF)

    label("loc_DDB")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E07")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_E07")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E1E")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_E1E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E35")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_E35")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E4C")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_E4C")

    Return()

    # Function_7_D37 end

    def Function_8_E4D(): pass

    label("Function_8_E4D")


    def lambda_E53():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_E53)

    def lambda_E65():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_E65)

    def lambda_E77():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_E77)

    def lambda_E89():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_E89)
    Sleep(1000)
    Return()

    # Function_8_E4D end

    def Function_9_E9B(): pass

    label("Function_9_E9B")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x513, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FA7")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x19, 0x1E)
    OP_73(0x19)
    OP_6F(0x19, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 0x32)
    AddSepith(0x1, 0x32)
    AddSepith(0x2, 0x32)
    AddSepith(0x3, 0x32)
    AddSepith(0x4, 0x64)
    AddSepith(0x5, 0x64)
    AddSepith(0x6, 0x64)

    AnonymousTalk(    #14
        (
            "\x07\x02Obtained:\x01",
            "#56IEarth Sepith x50\x01",
            "#57IWater Sepith x50\x01",
            "#58IFire Sepith x50\x01",
            "#59IWind Sepith x50\x01",
            "#62ITime Sepith x100\x01",
            "#60ISpace Sepith x100\x01",
            "#61IMirage Sepith x100.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2898)
    Jump("loc_FE2")

    label("loc_FA7")


    AnonymousTalk(    #15
        "\x07\x05You again? At least Phantom Thief B is a gentleman!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_FE2")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0xC1, 0x0)
    Return()

    # Function_9_E9B end

    def Function_10_FF9(): pass

    label("Function_10_FF9")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x513, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10D2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1A, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_1067")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x05Found \x1F\xFC\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2899)
    Jump("loc_10CF")

    label("loc_1067")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "\x07\x05Found \x1F\xFC\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xFC\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1A, 60)
    OP_70(0x1A, 0x0)

    label("loc_10CF")

    Jump("loc_112E")

    label("loc_10D2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "\x07\x05An empty coffer\x01",
            "Devoid of any treasure.\x01",
            "Go seek another.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xC2, 0x0)

    label("loc_112E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_FF9 end

    def Function_11_113C(): pass

    label("Function_11_113C")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x513, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_118D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1B, 0x1E)
    OP_73(0x1B)
    OP_6F(0x1B, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    Call(6, 26)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x289A)
    Jump("loc_126D")

    label("loc_118D")


    AnonymousTalk(    #19
        (
            "\x07\x05[4/36] It is yet to be spoken of in legend, for its mother was a modest\x01",
            "carpenter who carved it with no other purpose than to hold a confession.\x01",
            "It was never meant for a grand display, but for a quiet, sincere love. \x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_126D")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0xC3, 0x0)
    Return()

    # Function_11_113C end

    def Function_12_1284(): pass

    label("Function_12_1284")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x515, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_135D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1C, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x260, 1)"), scpexpr(EXPR_END)), "loc_12F2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x05Found \x1F\x60\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x28AC)
    Jump("loc_135A")

    label("loc_12F2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "\x07\x05Found \x1F\x60\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x60\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1C, 60)
    OP_70(0x1C, 0x0)

    label("loc_135A")

    Jump("loc_142C")

    label("loc_135D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #22
        (
            "\x07\x05(8/12) But that would never have happened. Hideko would never have\x01",
            "denied Sato back then. See, she didn't have much money in those days,\x01",
            "yet she paid cash for the machine.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xC4, 0x0)

    label("loc_142C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_1284 end

    SaveToFile()

Try(main)
