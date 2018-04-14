from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        "Function_2_61A",          # 02, 2
        "Function_3_C19",          # 03, 3
        "Function_4_D30",          # 04, 4
        "Function_5_E47",          # 05, 5
        "Function_6_F5E",          # 06, 6
        "Function_7_1075",         # 07, 7
        "Function_8_118C",         # 08, 8
        "Function_9_12A3",         # 09, 9
        "Function_10_13BA",        # 0A, 10
        "Function_11_14D1",        # 0B, 11
        "Function_12_15DE",        # 0C, 12
        "Function_13_165F",        # 0D, 13
        "Function_14_175A",        # 0E, 14
        "Function_15_17D2",        # 0F, 15
        "Function_16_18C5",        # 10, 16
        "Function_17_19B8",        # 11, 17
        "Function_18_1A06",        # 12, 18
        "Function_19_1A54",        # 13, 19
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D5, 7)), scpexpr(EXPR_END)), "loc_41D")
    SetChrFlags(0x8, 0x80)

    label("loc_41D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D6, 0)), scpexpr(EXPR_END)), "loc_429")
    SetChrFlags(0x9, 0x80)

    label("loc_429")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D6, 1)), scpexpr(EXPR_END)), "loc_435")
    SetChrFlags(0xA, 0x80)

    label("loc_435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D6, 2)), scpexpr(EXPR_END)), "loc_441")
    SetChrFlags(0xB, 0x80)

    label("loc_441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D6, 3)), scpexpr(EXPR_END)), "loc_44D")
    SetChrFlags(0xC, 0x80)

    label("loc_44D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D6, 4)), scpexpr(EXPR_END)), "loc_459")
    SetChrFlags(0xD, 0x80)

    label("loc_459")

    OP_10(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C4, 2)), scpexpr(EXPR_END)), "loc_4FF")
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
    Jump("loc_598")

    label("loc_4FF")

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

    label("loc_598")

    OP_1B(0x0, 0x0, 0xC)
    OP_1B(0x1, 0x0, 0xE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60D")
    LoadEffect(0x2, "map\\\\mp027_00.eff")
    PlayEffect(0x2, 0x2, 0xFF, -3990, 5600, 147040, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_71(0x13, 0x20)
    OP_6F(0x13, 0)
    OP_70(0x13, 0xFA)
    Jump("loc_619")

    label("loc_60D")

    OP_72(0x13, 0x20)
    OP_6F(0x13, 250)

    label("loc_619")

    Return()

    # Function_1_349 end

    def Function_2_61A(): pass

    label("Function_2_61A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F1")
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
            "\x07\x05#1S『关于‘环’的封印（４／４）』\x01",
            "　\x01",
            "从设施■■■的光，\x01",
            "经过长城『■■■』■内■折■\x01",
            "■■■，并■■到了浮在■中的■■■。\x01",
            "　\x01",
            "■是，■环■\x01",
            "■从我们■■消■■，\x01",
            "『■■■梅拉■』■■■了运■。\x01",
            "这样，『■■■■』\x01",
            "的成功■行便被确认■。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #1
        (
            "\x07\x05#1S■环■是■■至宝■中\x01",
            "■■空间的■■。\x01",
            "■了让拥有对空间■■■■■力量■■■■无■■\x01",
            "■■■■事就是■■\x01",
            "■绝掉■■■对空间\x01",
            "■至对时间的■■■■。\x01",
            "　\x01",
            "我们绞■■汁研■出的■■■■构』\x01",
            "将■■■连同城■■■■进了■■元，\x01",
            "成功地■■■■时■■结■。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #2
        "\x07\x00得到了\x1F\x08\x04\x07\x00。\x02",
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
    Jump("loc_C15")

    label("loc_9F1")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #3
        (
            "\x07\x05#1S『关于‘环’的封印（４／４）』\x01",
            "　\x01",
            "从设施■■■的光，\x01",
            "经过长城『■■■』■内■折■\x01",
            "■■■，并■■到了浮在■中的■■■。\x01",
            "　\x01",
            "■是，■环■\x01",
            "■从我们■■消■■，\x01",
            "『■■■梅拉■』■■■了运■。\x01",
            "这样，『■■■■』\x01",
            "的成功■行便被确认■。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #4
        (
            "\x07\x05#1S■环■是■■至宝■中\x01",
            "■■空间的■■。\x01",
            "■了让拥有对空间■■■■■力量■■■■无■■\x01",
            "■■■■事就是■■\x01",
            "■绝掉■■■对空间\x01",
            "■至对时间的■■■■。\x01",
            "　\x01",
            "我们绞■■汁研■出的■■■■构』\x01",
            "将■■■连同城■■■■进了■■元，\x01",
            "成功地■■■■时■■结■。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_C15")

    TalkEnd(0xFF)
    Return()

    # Function_2_61A end

    def Function_3_C19(): pass

    label("Function_3_C19")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF1")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xA, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_C88")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x00得到了\x1F\xFC\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F82)
    Jump("loc_CEE")

    label("loc_C88")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "宝箱里装有\x1F\xFC\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFC\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xA, 60)
    OP_70(0xA, 0x0)

    label("loc_CEE")

    Jump("loc_D22")

    label("loc_CF1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_D22")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_C19 end

    def Function_4_D30(): pass

    label("Function_4_D30")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E08")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xB, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x142, 1)"), scpexpr(EXPR_END)), "loc_D9F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x00得到了\x1F\x42\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F83)
    Jump("loc_E05")

    label("loc_D9F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "宝箱里装有\x1F\x42\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x42\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xB, 60)
    OP_70(0xB, 0x0)

    label("loc_E05")

    Jump("loc_E39")

    label("loc_E08")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_E39")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_D30 end

    def Function_5_E47(): pass

    label("Function_5_E47")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F1F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xC, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x201, 1)"), scpexpr(EXPR_END)), "loc_EB6")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x00得到了\x1F\x01\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F84)
    Jump("loc_F1C")

    label("loc_EB6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "宝箱里装有\x1F\x01\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x01\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xC, 60)
    OP_70(0xC, 0x0)

    label("loc_F1C")

    Jump("loc_F50")

    label("loc_F1F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_F50")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_E47 end

    def Function_6_F5E(): pass

    label("Function_6_F5E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1036")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xD, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_FCD")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x00得到了\x1F\xF9\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F85)
    Jump("loc_1033")

    label("loc_FCD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "宝箱里装有\x1F\xF9\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF9\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xD, 60)
    OP_70(0xD, 0x0)

    label("loc_1033")

    Jump("loc_1067")

    label("loc_1036")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1067")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_F5E end

    def Function_7_1075(): pass

    label("Function_7_1075")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_114D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xE, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x187, 1)"), scpexpr(EXPR_END)), "loc_10E4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x00得到了\x1F\x87\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F86)
    Jump("loc_114A")

    label("loc_10E4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "宝箱里装有\x1F\x87\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x87\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xE, 60)
    OP_70(0xE, 0x0)

    label("loc_114A")

    Jump("loc_117E")

    label("loc_114D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_117E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1075 end

    def Function_8_118C(): pass

    label("Function_8_118C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1264")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xF, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_11FB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x00得到了\x1F\xF7\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F88)
    Jump("loc_1261")

    label("loc_11FB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "宝箱里装有\x1F\xF7\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF7\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xF, 60)
    OP_70(0xF, 0x0)

    label("loc_1261")

    Jump("loc_1295")

    label("loc_1264")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1295")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_118C end

    def Function_9_12A3(): pass

    label("Function_9_12A3")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_137B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x11, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x157, 1)"), scpexpr(EXPR_END)), "loc_1312")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #23
        "\x07\x00得到了\x1F\x57\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F89)
    Jump("loc_1378")

    label("loc_1312")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #24
        (
            "宝箱里装有\x1F\x57\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x57\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x11, 60)
    OP_70(0x11, 0x0)

    label("loc_1378")

    Jump("loc_13AC")

    label("loc_137B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #25
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_13AC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_12A3 end

    def Function_10_13BA(): pass

    label("Function_10_13BA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1492")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x12, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x299, 1)"), scpexpr(EXPR_END)), "loc_1429")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #26
        "\x07\x00得到了\x1F\x99\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F8A)
    Jump("loc_148F")

    label("loc_1429")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #27
        (
            "宝箱里装有\x1F\x99\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x99\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x12, 60)
    OP_70(0x12, 0x0)

    label("loc_148F")

    Jump("loc_14C3")

    label("loc_1492")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #28
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_14C3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_13BA end

    def Function_11_14D1(): pass

    label("Function_11_14D1")

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

    # Function_11_14D1 end

    def Function_12_15DE(): pass

    label("Function_12_15DE")

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

    # Function_12_15DE end

    def Function_13_165F(): pass

    label("Function_13_165F")

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

    # Function_13_165F end

    def Function_14_175A(): pass

    label("Function_14_175A")

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

    # Function_14_175A end

    def Function_15_17D2(): pass

    label("Function_15_17D2")

    LoadEffect(0x0, "map\\\\mp049_21.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_15_17D2 end

    def Function_16_18C5(): pass

    label("Function_16_18C5")

    LoadEffect(0x0, "map\\\\mp049_22.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_16_18C5 end

    def Function_17_19B8(): pass

    label("Function_17_19B8")


    def lambda_19BE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_19BE)

    def lambda_19D0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_19D0)

    def lambda_19E2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_19E2)

    def lambda_19F4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_19F4)
    Sleep(2500)
    Return()

    # Function_17_19B8 end

    def Function_18_1A06(): pass

    label("Function_18_1A06")


    def lambda_1A0C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1A0C)

    def lambda_1A1E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1A1E)

    def lambda_1A30():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1A30)

    def lambda_1A42():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1A42)
    Sleep(2000)
    Return()

    # Function_18_1A06 end

    def Function_19_1A54(): pass

    label("Function_19_1A54")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AA5")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #29
        "\x07\x05导力好像停止了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_1C4A")

    label("loc_1AA5")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #30
        "\x07\x05这是一台可供旅行者回复体力的导力器装置。\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "在这里休息\x01",      # 0
            "离开\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C2F")
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

    label("loc_1C2F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C49")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_1C49")

    Return()

    label("loc_1C4A")

    Return()

    # Function_19_1A54 end

    SaveToFile()

Try(main)
