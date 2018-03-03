from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7104   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7104.x',
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
        'ED6_DT29/CH14460 ._CH',             # 00
        'ED6_DT29/CH14461 ._CH',             # 01
        'ED6_DT29/CH14910 ._CH',             # 02
        'ED6_DT29/CH14911 ._CH',             # 03
        'ED6_DT29/CH14920 ._CH',             # 04
        'ED6_DT29/CH14921 ._CH',             # 05
        'ED6_DT29/CH14930 ._CH',             # 06
        'ED6_DT29/CH14931 ._CH',             # 07
        'ED6_DT29/CH15040 ._CH',             # 08
        'ED6_DT29/CH15040 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT29/CH14460P._CP',             # 00
        'ED6_DT29/CH14461P._CP',             # 01
        'ED6_DT29/CH14910P._CP',             # 02
        'ED6_DT29/CH14911P._CP',             # 03
        'ED6_DT29/CH14920P._CP',             # 04
        'ED6_DT29/CH14921P._CP',             # 05
        'ED6_DT29/CH14930P._CP',             # 06
        'ED6_DT29/CH14931P._CP',             # 07
        'ED6_DT29/CH15040P._CP',             # 08
        'ED6_DT29/CH15040P._CP',             # 09
    )

    DeclMonster(
        X                   = -150,
        Z                   = -4000,
        Y                   = -28070,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -36030,
        Z                   = 0,
        Y                   = -33160,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -35860,
        Z                   = 0,
        Y                   = -12590,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x130,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -35750,
        Z                   = 0,
        Y                   = 7680,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 36710,
        Z                   = 8000,
        Y                   = -3330,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 36110,
        Z                   = 8000,
        Y                   = 17240,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 36110,
        Z                   = 8000,
        Y                   = 37800,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12F,
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
        TriggerY            = 32000,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = 14000,
        ActorY              = 32000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -36050,
        TriggerZ            = 0,
        TriggerY            = -4240,
        TriggerRange        = 1000,
        ActorX              = -36050,
        ActorZ              = 1000,
        ActorY              = -4240,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 36000,
        TriggerZ            = 8000,
        TriggerY            = 25870,
        TriggerRange        = 1000,
        ActorX              = 36000,
        ActorZ              = 9000,
        ActorY              = 25870,
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
        "Function_2_372",          # 02, 2
        "Function_3_7E9",          # 03, 3
        "Function_4_9C0",          # 04, 4
        "Function_5_C47",          # 05, 5
        "Function_6_D25",          # 06, 6
        "Function_7_DE1",          # 07, 7
        "Function_8_EF7",          # 08, 8
        "Function_9_F45",          # 09, 9
        "Function_10_1097",        # 0A, 10
        "Function_11_1226",        # 0B, 11
        "Function_12_137E",        # 0C, 12
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

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE0C00, 0x230087)
    OP_1B(0x0, 0x0, 0x6)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DE")
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x85, 0x0)

    label("loc_2DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x510, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F0")
    OP_6F(0x17, 0)
    Jump("loc_2F7")

    label("loc_2F0")

    OP_6F(0x17, 60)

    label("loc_2F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x515, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_309")
    OP_6F(0x19, 0)
    Jump("loc_310")

    label("loc_309")

    OP_6F(0x19, 60)

    label("loc_310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x515, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_322")
    OP_6F(0x1A, 0)
    Jump("loc_329")

    label("loc_322")

    OP_6F(0x1A, 60)

    label("loc_329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x515, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33B")
    OP_6F(0x1B, 0)
    Jump("loc_342")

    label("loc_33B")

    OP_6F(0x1B, 60)

    label("loc_342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x515, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_354")
    OP_6F(0x1C, 0)
    Jump("loc_35B")

    label("loc_354")

    OP_6F(0x1C, 60)

    label("loc_35B")

    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_2B6 end

    def Function_2_372(): pass

    label("Function_2_372")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DD")
    EventBegin(0x0)
    Fade(500)
    OP_6D(-240, 4000, 2620, 0)
    OP_67(-1000, 6950, -10000, 0)
    OP_6B(3490, 0)
    OP_6C(45000, 0)
    OP_6E(240, 0)
    SetChrPos(0x109, -1060, 4000, 1910, 90)
    SetChrPos(0xEF, -2810, 4000, 1800, 90)
    SetChrPos(0xF0, -3400, 4000, 600, 90)
    SetChrPos(0xF1, -3660, 4000, 2430, 90)
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
        "\x07\x05Found \x1F\x55\x05\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x555, 1)
    OP_A2(0x2880)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #1
        0x109,
        (
            "#1079F#6PWha...?!\x02\x03",

            "#1063F(What's this doing here...?)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_55A")
    OP_A2(0x0)
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #2
        0x107,
        "#064F#6PWhat's wrong, Kevin?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6AE")

    label("loc_55A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5AD")
    OP_A2(0x3)
    OP_62(0x10B, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #3
        0x10B,
        "#213F#6PHmm? Something wrong?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6AE")

    label("loc_5AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F5")
    OP_A2(0x4)
    OP_62(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #4
        0x102,
        "#1504F#6P...Kevin?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6AE")

    label("loc_5F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_653")
    OP_A2(0x5)
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #5
        0x105,
        "#1164F#6PUmm... Is something the matter?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6AE")

    label("loc_653")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6AE")
    OP_A2(0x1)
    OP_62(0x10E, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #6
        0x10E,
        "#173F#6PIs something the matter, Father?\x02",
    )

    CloseMessageWindow()

    label("loc_6AE")

    OP_63(0x109)
    Sleep(100)
    OP_8C(0x109, 270, 400)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_74D")

    ChrTalk(    #7
        0x109,
        (
            "#1075F#11POh, no. I was just impressed at how nice\x01",
            "this bowgun is.\x02\x03",

            "#1840FI'm gonna get some good use out of this\x01",
            "baby.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CA")

    label("loc_74D")


    ChrTalk(    #8
        0x109,
        (
            "#1075F#11POh, no. I was just impressed at how nice\x01",
            "this bowgun is.\x02\x03",

            "#1840FI'm gonna get some good use out of this\x01",
            "baby.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CA")

    OP_A2(0x2806)
    OP_28(0x30, 0x1, 0x4)
    Sleep(500)
    EventEnd(0x0)
    Jump("loc_7E1")

    label("loc_7DD")

    Call(0, 3)

    label("loc_7E1")

    Jump("loc_7E8")

    label("loc_7E4")

    Call(0, 3)

    label("loc_7E8")

    Return()

    # Function_2_372 end

    def Function_3_7E9(): pass

    label("Function_3_7E9")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x510, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x17, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x555, 1)"), scpexpr(EXPR_END)), "loc_857")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05Found \x1F\x55\x05\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2880)
    Jump("loc_8BF")

    label("loc_857")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "\x07\x05Found \x1F\x55\x05\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x55\x05\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x17, 60)
    OP_70(0x17, 0x0)

    label("loc_8BF")

    Jump("loc_9B2")

    label("loc_8C2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "\x07\x05[29/36] The son scoffed upon hearing Jubilee's name. His wife always\x01",
            "had a habit of biting her lip before playing her ace in the hole, and there\x01",
            "was no finer ace against him than their daughter's opinion.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xC5, 0x0)

    label("loc_9B2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_7E9 end

    def Function_4_9C0(): pass

    label("Function_4_9C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A94")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(2048)
    Sleep(500)
    OP_AA(65282)
    Jump("loc_A97")

    label("loc_A94")

    TalkBegin(0xFF)

    label("loc_A97")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #12
        "\x07\x05Select an Option\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AD3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C16")

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
        (0, "loc_B2F"),
        (1, "loc_BAA"),
        (2, "loc_BD8"),
        (SWITCH_DEFAULT, "loc_C06"),
    )


    label("loc_B2F")

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
    Jump("loc_C13")

    label("loc_BAA")

    OP_A9(0x1A)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #13
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_C13")

    label("loc_BD8")

    OP_A9(0x5)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #14
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_C13")

    label("loc_C06")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C13")

    label("loc_C13")

    Jump("loc_AD3")

    label("loc_C16")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C43")
    OP_A2(0x258B)
    EventEnd(0x1)
    Jump("loc_C46")

    label("loc_C43")

    TalkEnd(0xFF)

    label("loc_C46")

    Return()

    # Function_4_9C0 end

    def Function_5_C47(): pass

    label("Function_5_C47")

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
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_5_C47 end

    def Function_6_D25(): pass

    label("Function_6_D25")

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
    NewScene("ED6_DT21/M7102   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_6_D25 end

    def Function_7_DE1(): pass

    label("Function_7_DE1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E0A")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_DFE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_DFE)

    label("loc_E0A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E33")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_E27():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_E27)

    label("loc_E33")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E5C")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_E50():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_E50)

    label("loc_E5C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E85")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_E79():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_E79)

    label("loc_E85")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EB1")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_EB1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EC8")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_EC8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EDF")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_EDF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EF6")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_EF6")

    Return()

    # Function_7_DE1 end

    def Function_8_EF7(): pass

    label("Function_8_EF7")


    def lambda_EFD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_EFD)

    def lambda_F0F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_F0F)

    def lambda_F21():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_F21)

    def lambda_F33():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_F33)
    Sleep(1000)
    Return()

    # Function_8_EF7 end

    def Function_9_F45(): pass

    label("Function_9_F45")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x515, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_101E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x19, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_FB3")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x05Found \x1F\xFB\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x28A8)
    Jump("loc_101B")

    label("loc_FB3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "\x07\x05Found \x1F\xFB\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xFB\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x19, 60)
    OP_70(0x19, 0x0)

    label("loc_101B")

    Jump("loc_1089")

    label("loc_101E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "\x07\x05*lid creaks* TEN THOUSAND YEARS WILL GIVE YOU SUCH A CRICK IN\x01",
            "THE NECK.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xC6, 0x0)

    label("loc_1089")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_F45 end

    def Function_10_1097(): pass

    label("Function_10_1097")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x515, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A4")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1A, 0x1E)
    OP_73(0x1A)
    OP_6F(0x1A, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 0x64)
    AddSepith(0x1, 0x64)
    AddSepith(0x2, 0x64)
    AddSepith(0x3, 0x64)
    AddSepith(0x4, 0x32)
    AddSepith(0x5, 0x32)
    AddSepith(0x6, 0x32)

    AnonymousTalk(    #18
        (
            "\x07\x02Obtained:\x01",
            "#56IEarth Sepith x100\x01",
            "#57IWater Sepith x100\x01",
            "#58IFire Sepith x100\x01",
            "#59IWind Sepith x100\x01",
            "#62ITime Sepith x50\x01",
            "#60ISpace Sepith x50\x01",
            "#61IMirage Sepith x50.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x28A9)
    Jump("loc_120F")

    label("loc_11A4")


    AnonymousTalk(    #19
        (
            "\x07\x05If this empty chest were filled to the brim with food, it still wouldn't be\x01",
            "enough to satisfy Ries.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_120F")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0xC7, 0x0)
    Return()

    # Function_10_1097 end

    def Function_11_1226(): pass

    label("Function_11_1226")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x515, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12FF")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1B, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x69, 1)"), scpexpr(EXPR_END)), "loc_1294")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x05Found \x1F\x69\x00\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x28AA)
    Jump("loc_12FC")

    label("loc_1294")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "\x07\x05Found \x1F\x69\x00\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x69\x00\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1B, 60)
    OP_70(0x1B, 0x0)

    label("loc_12FC")

    Jump("loc_1370")

    label("loc_12FF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x05Bet you 50 mira that item is still in your inventory during the final battle.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xC8, 0x0)

    label("loc_1370")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_1226 end

    def Function_12_137E(): pass

    label("Function_12_137E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x515, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1457")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1C, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x170, 1)"), scpexpr(EXPR_END)), "loc_13EC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #23
        "\x07\x05Found \x1F\x70\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x28AE)
    Jump("loc_1454")

    label("loc_13EC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #24
        (
            "\x07\x05Found \x1F\x70\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x70\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1C, 60)
    OP_70(0x1C, 0x0)

    label("loc_1454")

    Jump("loc_14C6")

    label("loc_1457")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #25
        "\x07\x05It's a shining pom! Wait. That's a lie...like the promise of more treasure.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xC9, 0x0)

    label("loc_14C6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_137E end

    SaveToFile()

Try(main)
