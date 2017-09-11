from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'C4100   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60021",
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
        'Royal Avenue',                         # 9
        'Erbe Royal Villa',                     # 10
        'プラント3',                            # 11
        'ワニ4',                                # 12
        'ダイン・ワニ3',                        # 13
        'バット6',                              # 14
        'プリメーラ3',                          # 15
        'ヘルマーズ3',                          # 16
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
        'ED6_DT09/CH10780 ._CH',             # 00
        'ED6_DT09/CH10781 ._CH',             # 01
        'ED6_DT09/CH10790 ._CH',             # 02
        'ED6_DT09/CH10791 ._CH',             # 03
        'ED6_DT09/CH10050 ._CH',             # 04
        'ED6_DT09/CH10051 ._CH',             # 05
        'ED6_DT09/CH10800 ._CH',             # 06
        'ED6_DT09/CH10801 ._CH',             # 07
        'ED6_DT09/CH10810 ._CH',             # 08
        'ED6_DT09/CH10811 ._CH',             # 09
        'ED6_DT09/CH10820 ._CH',             # 0A
        'ED6_DT09/CH10821 ._CH',             # 0B
        'ED6_DT09/CH11220 ._CH',             # 0C
        'ED6_DT09/CH11221 ._CH',             # 0D
        'ED6_DT09/CH11230 ._CH',             # 0E
        'ED6_DT09/CH11231 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT09/CH10780P._CP',             # 00
        'ED6_DT09/CH10781P._CP',             # 01
        'ED6_DT09/CH10790P._CP',             # 02
        'ED6_DT09/CH10791P._CP',             # 03
        'ED6_DT09/CH10050P._CP',             # 04
        'ED6_DT09/CH10051P._CP',             # 05
        'ED6_DT09/CH10800P._CP',             # 06
        'ED6_DT09/CH10801P._CP',             # 07
        'ED6_DT09/CH10810P._CP',             # 08
        'ED6_DT09/CH10811P._CP',             # 09
        'ED6_DT09/CH10820P._CP',             # 0A
        'ED6_DT09/CH10821P._CP',             # 0B
        'ED6_DT09/CH11220P._CP',             # 0C
        'ED6_DT09/CH11221P._CP',             # 0D
        'ED6_DT09/CH11230P._CP',             # 0E
        'ED6_DT09/CH11231P._CP',             # 0F
    )

    DeclNpc(
        X                   = 980,
        Z                   = 0,
        Y                   = 71400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -43080,
        Z                   = 0,
        Y                   = -63930,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 11100,
        Z                   = -20,
        Y                   = 24620,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x262,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -6780,
        Z                   = 40,
        Y                   = 21320,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x265,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -2830,
        Z                   = 0,
        Y                   = -29020,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x264,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -50760,
        Z                   = 0,
        Y                   = 12800,
        Unknown_0C          = 0,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x266,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -44310,
        Z                   = 30,
        Y                   = -2880,
        Unknown_0C          = 0,
        Unknown_0E          = 14,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x268,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -34560,
        Z                   = 170,
        Y                   = 8670,
        Unknown_0C          = 0,
        Unknown_0E          = 12,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x267,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -34880,
        TriggerZ            = 80,
        TriggerY            = 3840,
        TriggerRange        = 1000,
        ActorX              = -34320,
        ActorZ              = 1590,
        ActorY              = 3790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -11000,
        TriggerZ            = 0,
        TriggerY            = -39890,
        TriggerRange        = 1000,
        ActorX              = -11070,
        ActorZ              = 0,
        ActorY              = -40530,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -44400,
        TriggerZ            = 500,
        TriggerY            = 7650,
        TriggerRange        = 1500,
        ActorX              = -44400,
        ActorZ              = 4000,
        ActorY              = 7650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_27E",          # 00, 0
        "Function_1_2A1",          # 01, 1
        "Function_2_2E6",          # 02, 2
        "Function_3_5EF",          # 03, 3
        "Function_4_739",          # 04, 4
        "Function_5_86D",          # 05, 5
    )


    def Function_0_27E(): pass

    label("Function_0_27E")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_28A"),
        (SWITCH_DEFAULT, "loc_2A0"),
    )


    label("loc_28A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29D")
    OP_A2(0x615)
    Event(0, 2)

    label("loc_29D")

    Jump("loc_2A0")

    label("loc_2A0")

    Return()

    # Function_0_27E end

    def Function_1_2A1(): pass

    label("Function_1_2A1")

    OP_16(0x2, 0xFA0, 0xFFFDE4F0, 0xFFFE0C00, 0x30063)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C5")
    OP_6F(0x3, 0)
    Jump("loc_2CC")

    label("loc_2C5")

    OP_6F(0x3, 60)

    label("loc_2CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DE")
    OP_6F(0x4, 0)
    Jump("loc_2E5")

    label("loc_2DE")

    OP_6F(0x4, 60)

    label("loc_2E5")

    Return()

    # Function_1_2A1 end

    def Function_2_2E6(): pass

    label("Function_2_2E6")

    EventBegin(0x0)
    OP_6D(750, 0, 48230, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -90, 0, 52000, 270)
    SetChrPos(0x102, 1380, 0, 52150, 270)

    def lambda_34D():
        OP_6D(750, 0, 45230, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_34D)

    def lambda_365():
        OP_8E(0xFE, 0x118, 0x0, 0xB504, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_365)

    def lambda_380():
        OP_8E(0xFE, 0x672, 0x0, 0xB676, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_380)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #0
        0x101,
        (
            "#501FThe Erbe Scenic Route...\x02\x03",

            "I like the paved road through\x01",
            "the forest. Neat stuff.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #1
        0x102,
        (
            "#010FI imagine that Grancelites have\x01",
            "come here to stretch out and\x01",
            "relax for a long time.\x02\x03",

            "I wonder just how long it's\x01",
            "been here...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #2
        0x101,
        (
            "#000FHmm... Well, I guess it should\x01",
            "come as no surprise that the\x01",
            "queen's land is so gorgeous.\x02\x03",

            "#505FStill, I can't help feeling like we've\x01",
            "got monsters lurking around...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x102,
        (
            "#015FNicely done.\x02\x03",

            "#012FThe monsters here seem to be stronger than\x01",
            "those we fought on the way here.\x02\x03",

            "We're here to look for Zin, but don't let\x01",
            "your guard down.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_2_2E6 end

    def Function_3_5EF(): pass

    label("Function_3_5EF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E4")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x287, 1)"), scpexpr(EXPR_END)), "loc_667")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x00Found \x07\x02Deathblow 2\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x682)
    Jump("loc_6E1")

    label("loc_667")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x00Found \x07\x02Deathblow 2\x07\x00 in chest.\x01",
            "Inventory full so gave up \x07\x02Deathblow 2\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_6E1")

    Jump("loc_72B")

    label("loc_6E4")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #6
        "\x07\x05What more do you want from me...BLOOD?!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x3B)

    label("loc_72B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_5EF end

    def Function_4_739(): pass

    label("Function_4_739")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_7B0")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x00Found \x07\x02Teara Balm\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x683)
    Jump("loc_828")

    label("loc_7B0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "\x07\x00Found \x07\x02Teara Balm\x07\x00 in chest.\x01",
            "Inventory full so gave up \x07\x02Teara Balm\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_828")

    Jump("loc_85F")

    label("loc_82B")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #9
        "\x07\x05<Silent Disapproval>\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x3C)

    label("loc_85F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_739 end

    def Function_5_86D(): pass

    label("Function_5_86D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05There is an old virescent stone monument.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_5_86D end

    SaveToFile()

Try(main)
