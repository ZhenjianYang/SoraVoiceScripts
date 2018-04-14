from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'R2203   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2203.x',
        MapIndex            = 101,
        MapDefaultBGM       = "ed60029",
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
        '王国军士官',                           # 9
        '王国军士兵',                           # 10
        '王国军士兵',                           # 11
        '玛诺利亚村方向',                       # 12
        '玛西亚孤儿院方向',                     # 13
        '卢安方向',                             # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
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
        'ED6_DT29/CH12100 ._CH',             # 00
        'ED6_DT29/CH12101 ._CH',             # 01
        'ED6_DT29/CH12150 ._CH',             # 02
        'ED6_DT29/CH12151 ._CH',             # 03
        'ED6_DT07/CH01600 ._CH',             # 04
        'ED6_DT07/CH01640 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT29/CH12100P._CP',             # 00
        'ED6_DT29/CH12101P._CP',             # 01
        'ED6_DT29/CH12150P._CP',             # 02
        'ED6_DT29/CH12151P._CP',             # 03
        'ED6_DT07/CH01600P._CP',             # 04
        'ED6_DT07/CH01640P._CP',             # 05
    )

    DeclNpc(
        X                   = -95890,
        Z                   = -5970,
        Y                   = 5490,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = -94000,
        Z                   = -6040,
        Y                   = 4900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -86590,
        Z                   = -2090,
        Y                   = 20010,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -139370,
        Z                   = -2020,
        Y                   = 15120,
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
        X                   = -28630,
        Z                   = -1990,
        Y                   = 79340,
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
        X                   = 7410,
        Z                   = -2000,
        Y                   = 29980,
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
        X                   = -96260,
        Z                   = -1950,
        Y                   = 27960,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x184,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -104740,
        Z                   = -5970,
        Y                   = 11000,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x18F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -81100,
        Z                   = -5870,
        Y                   = 13330,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x18E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -88220,
        Z                   = -5960,
        Y                   = 9810,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x18F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -114230,
        TriggerZ            = -6050,
        TriggerY            = 11770,
        TriggerRange        = 1000,
        ActorX              = -114730,
        ActorZ              = -6040,
        ActorY              = 12270,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -77980,
        TriggerZ            = -6870,
        TriggerY            = -11780,
        TriggerRange        = 1000,
        ActorX              = -77540,
        ActorZ              = -6730,
        ActorY              = -11140,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -21830,
        TriggerZ            = -2000,
        TriggerY            = 37790,
        TriggerRange        = 1500,
        ActorX              = -21830,
        ActorZ              = -800,
        ActorY              = 37790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -18840,
        TriggerZ            = -2000,
        TriggerY            = 33860,
        TriggerRange        = 1500,
        ActorX              = -18840,
        ActorZ              = -500,
        ActorY              = 33860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_29A",          # 00, 0
        "Function_1_30A",          # 01, 1
        "Function_2_35E",          # 02, 2
        "Function_3_55B",          # 03, 3
        "Function_4_6C3",          # 04, 4
        "Function_5_823",          # 05, 5
        "Function_6_93A",          # 06, 6
        "Function_7_A51",          # 07, 7
        "Function_8_A94",          # 08, 8
    )


    def Function_0_29A(): pass

    label("Function_0_29A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_2E4")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x9, -32430, -1940, 54880, 135)
    SetChrPos(0xA, -117980, -2100, 18390, 135)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    Jump("loc_309")

    label("loc_2E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_309")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)

    label("loc_309")

    Return()

    # Function_0_29A end

    def Function_1_30A(): pass

    label("Function_1_30A")

    OP_16(0x2, 0xFA0, 0xFFFD21A0, 0xFFFE5638, 0x230026)
    OP_4F(0x2A, (scpexpr(EXPR_PUSH_LONG, 0x186A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x1C8, 0x1, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x260, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33D")
    OP_6F(0x0, 0)
    Jump("loc_344")

    label("loc_33D")

    OP_6F(0x0, 60)

    label("loc_344")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x260, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_356")
    OP_6F(0x1, 0)
    Jump("loc_35D")

    label("loc_356")

    OP_6F(0x1, 60)

    label("loc_35D")

    Return()

    # Function_1_30A end

    def Function_2_35E(): pass

    label("Function_2_35E")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_47C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_414")

    ChrTalk(    #0
        0xFE,
        (
            "看来王立学院\x01",
            "好像被敌人占领了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "不过还不明白敌人的意图……\x01",
            "说不定什么时候\x01",
            "又会发生同样的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "为了慎重起见，村子和孤儿院\x01",
            "都已经配置了警备人员。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_479")

    label("loc_414")


    ChrTalk(    #3
        0xFE,
        (
            "实在不行\x01",
            "只能让居民\x01",
            "躲在警备艇里面避难……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "就算导力炮不能使用\x01",
            "避避难的用场还是可以起到的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_479")

    Jump("loc_557")

    label("loc_47C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_557")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50B")

    ChrTalk(    #5
        0xFE,
        "唔，你们是游击士吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "相信各位一看就知道，\x01",
            "我们的警备艇是无法飞行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "虽然请求过救援，\x01",
            "但不知道要等多久……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_557")

    label("loc_50B")


    ChrTalk(    #8
        0xFE,
        (
            "救援来之前\x01",
            "我们打算在这边待命。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "我们能保护自己。\x01",
            "各位也不用担心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_557")

    TalkEnd(0x8)
    Return()

    # Function_2_35E end

    def Function_3_55B(): pass

    label("Function_3_55B")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_5D4")

    ChrTalk(    #10
        0xFE,
        (
            "队，队长要我\x01",
            "守卫这个地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "万一有什么情况，让我带着孩子们\x01",
            "到警备艇避难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "唉……责任重大啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6BF")

    label("loc_5D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_6BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_677")

    ChrTalk(    #13
        0xFE,
        (
            "返回要塞途中\x01",
            "又发生了那个现象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "虽然情况危急，\x01",
            "总算还是想办法迫降了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "降落的地方\x01",
            "还好是在沙滩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "因此负伤的人\x01",
            "也都是轻伤。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_6BF")

    label("loc_677")


    ChrTalk(    #17
        0xFE,
        (
            "其中一名伤员\x01",
            "被送去附近的村子了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "还是躺在床上\x01",
            "休息休息好啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BF")

    TalkEnd(0x9)
    Return()

    # Function_3_55B end

    def Function_4_6C3(): pass

    label("Function_4_6C3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_753")

    ChrTalk(    #19
        0xFE,
        (
            "听说那些红色士兵们\x01",
            "在这附近出现了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "而且根据传言，他们在\x01",
            "这种情况下还用了枪不是吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "光靠这种剑\x01",
            "要怎样对抗才好啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81F")

    label("loc_753")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_81F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D5")

    ChrTalk(    #22
        0xFE,
        (
            "哎呀，这种时候\x01",
            "居然还有人通过街道啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "嗯，请确保\x01",
            "自己的安全吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "不好意思，\x01",
            "我也抽不出手来。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_81F")

    label("loc_7D5")


    ChrTalk(    #25
        0xFE,
        (
            "呼，救援部队\x01",
            "还不来吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "没有人会想要待在\x01",
            "有魔兽出没的地方啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81F")

    TalkEnd(0xFE)
    Return()

    # Function_4_6C3 end

    def Function_5_823(): pass

    label("Function_5_823")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x260, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8FB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x3DC, 1)"), scpexpr(EXPR_END)), "loc_892")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #27
        "\x07\x00得到了\x1F\xDC\x03\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1302)
    Jump("loc_8F8")

    label("loc_892")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #28
        (
            "宝箱里装有\x1F\xDC\x03\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xDC\x03\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_8F8")

    Jump("loc_92C")

    label("loc_8FB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #29
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_92C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_823 end

    def Function_6_93A(): pass

    label("Function_6_93A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x260, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A12")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_9A9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #30
        "\x07\x00得到了\x1F\xFC\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1303)
    Jump("loc_A0F")

    label("loc_9A9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #31
        (
            "宝箱里装有\x1F\xFC\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFC\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_A0F")

    Jump("loc_A43")

    label("loc_A12")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #32
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A43")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_93A end

    def Function_7_A51(): pass

    label("Function_7_A51")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #33
        "\x07\x05北　玛西亚孤儿院\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_A51 end

    def Function_8_A94(): pass

    label("Function_8_A94")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #34
        (
            "\x07\x05东　卢安市　　２３８塞尔矩\x01",
            "西　玛诺利亚村　７４塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_A94 end

    SaveToFile()

Try(main)
