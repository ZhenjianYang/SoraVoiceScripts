from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C1306   ._SN',
        MapName             = 'Bose',
        Location            = 'C1306.x',
        MapIndex            = 52,
        MapDefaultBGM       = "ed60089",
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
        '投发烟筒的人',                         # 9
        '接发烟筒的人',                         # 10
        '',                                     # 11
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
        'ED6_DT09/CH10380 ._CH',             # 00
        'ED6_DT09/CH10381 ._CH',             # 01
        'ED6_DT09/CH10390 ._CH',             # 02
        'ED6_DT09/CH10391 ._CH',             # 03
        'ED6_DT09/CH10250 ._CH',             # 04
        'ED6_DT09/CH10251 ._CH',             # 05
        'ED6_DT07/CH00330 ._CH',             # 06
        'ED6_DT07/CH00331 ._CH',             # 07
        'ED6_DT06/CH20020 ._CH',             # 08
        'ED6_DT27/CH03015 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT09/CH10380P._CP',             # 00
        'ED6_DT09/CH10381P._CP',             # 01
        'ED6_DT09/CH10390P._CP',             # 02
        'ED6_DT09/CH10391P._CP',             # 03
        'ED6_DT09/CH10250P._CP',             # 04
        'ED6_DT09/CH10251P._CP',             # 05
        'ED6_DT07/CH00330P._CP',             # 06
        'ED6_DT07/CH00331P._CP',             # 07
        'ED6_DT06/CH20020P._CP',             # 08
        'ED6_DT27/CH03015P._CP',             # 09
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1310724,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1310724,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -57220,
        Z                   = 0,
        Y                   = -50730,
        Unknown_0C          = 179,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xA2,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -142790,
        TriggerZ            = 0,
        TriggerY            = 58560,
        TriggerRange        = 1000,
        ActorX              = -142760,
        ActorZ              = 1500,
        ActorY              = 59200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -55470,
        TriggerZ            = 0,
        TriggerY            = -105270,
        TriggerRange        = 1000,
        ActorX              = -54920,
        ActorZ              = 1500,
        ActorY              = -105280,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -102030,
        TriggerZ            = 0,
        TriggerY            = -40370,
        TriggerRange        = 1000,
        ActorX              = -101990,
        ActorZ              = 0,
        ActorY              = -39700,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -990,
        TriggerZ            = 0,
        TriggerY            = -145880,
        TriggerRange        = 800,
        ActorX              = -990,
        ActorZ              = 800,
        ActorY              = -145880,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1E6",          # 00, 0
        "Function_1_1F9",          # 01, 1
        "Function_2_25D",          # 02, 2
        "Function_3_374",          # 03, 3
        "Function_4_48B",          # 04, 4
        "Function_5_5A2",          # 05, 5
        "Function_6_5B1",          # 06, 6
    )


    def Function_0_1E6(): pass

    label("Function_0_1E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_1F8")
    OP_64(0x3, 0x1)
    OP_A3(0x10F0)
    Event(0, 6)

    label("loc_1F8")

    Return()

    # Function_0_1E6 end

    def Function_1_1F9(): pass

    label("Function_1_1F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x320, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20B")
    OP_6F(0x2, 0)
    Jump("loc_212")

    label("loc_20B")

    OP_6F(0x2, 60)

    label("loc_212")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x320, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_224")
    OP_6F(0x3, 0)
    Jump("loc_22B")

    label("loc_224")

    OP_6F(0x3, 60)

    label("loc_22B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x320, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23D")
    OP_6F(0x4, 0)
    Jump("loc_244")

    label("loc_23D")

    OP_6F(0x4, 60)

    label("loc_244")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 2)), scpexpr(EXPR_END)), "loc_252")
    OP_64(0x3, 0x1)
    Jump("loc_257")

    label("loc_252")

    OP_72(0x0, 0x10)

    label("loc_257")

    OP_71(0x1, 0x4)
    Return()

    # Function_1_1F9 end

    def Function_2_25D(): pass

    label("Function_2_25D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x320, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_335")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_2CC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xF6\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1901)
    Jump("loc_332")

    label("loc_2CC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xF6\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF6\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_332")

    Jump("loc_366")

    label("loc_335")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_366")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_25D end

    def Function_3_374(): pass

    label("Function_3_374")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x320, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_3E3")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xFE\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1902)
    Jump("loc_449")

    label("loc_3E3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xFE\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFE\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_449")

    Jump("loc_47D")

    label("loc_44C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_47D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_374 end

    def Function_4_48B(): pass

    label("Function_4_48B")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x320, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_563")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_4FA")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\xFB\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1903)
    Jump("loc_560")

    label("loc_4FA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\xFB\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFB\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_560")

    Jump("loc_594")

    label("loc_563")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_594")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_48B end

    def Function_5_5A2(): pass

    label("Function_5_5A2")

    EventBegin(0x0)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C1304   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_5_5A2 end

    def Function_6_5B1(): pass

    label("Function_6_5B1")

    EventBegin(0x0)
    OP_6D(-970, 0, -146920, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x102, -1280, 0, -146530, 0)
    SetChrPos(0x146, -2570, 0, -147040, 90)
    SetChrPos(0x129, -320, 0, -147490, 0)
    SetChrPos(0x12A, -1440, 0, -147850, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #9
        0x129,
        "#190F（喂……怎么样？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x102,
        "#1033F#5P（不妙啊……）\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 180, 500)
    Sleep(300)

    ChrTalk(    #11
        0x102,
        (
            "#1030F#5P（吉尔，能给一个\x01",
            "我给你的Ｓ２弾吗？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x12A,
        "#201F（哦，哦哦……）\x02",
    )

    CloseMessageWindow()
    OP_8E(0x12A, 0xFFFFFA74, 0x0, 0xFFFDC038, 0x7D0, 0x0)
    Sleep(1000)
    OP_8F(0x12A, 0xFFFFFA6A, 0x0, 0xFFFDBE76, 0x7D0, 0x0)
    OP_8C(0x102, 0, 400)
    Fade(500)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 9)
    OP_0D()
    OP_22(0x6, 0x0, 0x64)
    OP_72(0x0, 0x800)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x6)
    Sleep(1000)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/C1304   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_6_5B1 end

    SaveToFile()

Try(main)
