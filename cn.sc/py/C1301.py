from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C1301   ._SN',
        MapName             = 'Bose',
        Location            = 'C1301.x',
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
        '守备队长',                             # 9
        '穆拉',                                 # 10
        '朵洛希',                               # 11
        '士兵',                                 # 12
        '士兵',                                 # 13
        ' ',                                    # 14
        ' ',                                    # 15
        ' ',                                    # 16
        ' ',                                    # 17
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
        'ED6_DT07/CH01600 ._CH',             # 00
        'ED6_DT27/CH03570 ._CH',             # 01
        'ED6_DT07/CH01300 ._CH',             # 02
        'ED6_DT07/CH02070 ._CH',             # 03
        'ED6_DT06/CH20063 ._CH',             # 04
        'ED6_DT06/CH20064 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01600P._CP',             # 00
        'ED6_DT27/CH03570P._CP',             # 01
        'ED6_DT07/CH01300P._CP',             # 02
        'ED6_DT07/CH02070P._CP',             # 03
        'ED6_DT06/CH20063P._CP',             # 04
        'ED6_DT06/CH20064P._CP',             # 05
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -11400,
        TriggerZ            = 4000,
        TriggerY            = -2400,
        TriggerRange        = 1500,
        ActorX              = -8930,
        ActorZ              = 6520,
        ActorY              = -880,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -9150,
        TriggerZ            = 5540,
        TriggerY            = -590,
        TriggerRange        = 1000,
        ActorX              = -10940,
        ActorZ              = 5000,
        ActorY              = -1870,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_242",          # 00, 0
        "Function_1_269",          # 01, 1
        "Function_2_26F",          # 02, 2
        "Function_3_11DA",         # 03, 3
        "Function_4_1220",         # 04, 4
        "Function_5_124B",         # 05, 5
        "Function_6_1267",         # 06, 6
        "Function_7_1297",         # 07, 7
        "Function_8_12EA",         # 08, 8
        "Function_9_1344",         # 09, 9
        "Function_10_139E",        # 0A, 10
        "Function_11_163F",        # 0B, 11
        "Function_12_166A",        # 0C, 12
        "Function_13_1695",        # 0D, 13
        "Function_14_16C0",        # 0E, 14
        "Function_15_16EB",        # 0F, 15
        "Function_16_171B",        # 10, 16
        "Function_17_175F",        # 11, 17
        "Function_18_17A3",        # 12, 18
        "Function_19_17E7",        # 13, 19
        "Function_20_18CB",        # 14, 20
        "Function_21_1923",        # 15, 21
        "Function_22_196D",        # 16, 22
        "Function_23_19A9",        # 17, 23
        "Function_24_19D7",        # 18, 24
        "Function_25_1ABB",        # 19, 25
        "Function_26_1B13",        # 1A, 26
        "Function_27_1B5D",        # 1B, 27
        "Function_28_1B99",        # 1C, 28
    )


    def Function_0_242(): pass

    label("Function_0_242")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_25C")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    Event(0, 2)
    Jump("loc_268")

    label("loc_25C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_268")
    Event(0, 10)

    label("loc_268")

    Return()

    # Function_0_242 end

    def Function_1_269(): pass

    label("Function_1_269")

    SetMapFlags(0x2000000)
    Return()

    # Function_1_269 end

    def Function_2_26F(): pass

    label("Function_2_26F")

    EventBegin(0x0)
    LoadEffect(0x0, "map\\\\mp032_00.eff")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-17010, 4000, -16370, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3150, 0)
    OP_6C(145000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_43(0x8, 0x1, 0x0, 0x3)
    Sleep(1000)
    OP_43(0x9, 0x1, 0x0, 0x4)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x8, 0x1)

    ChrTalk(    #0
        0x8,
        "这边请。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)

    ChrTalk(    #1
        0x9,
        "#273F#2P……哦。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)

    def lambda_334():
        OP_6D(-6100, 4000, -2470, 7000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_334)

    def lambda_34C():
        OP_67(0, 5960, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_34C)

    def lambda_364():
        OP_6E(255, 7000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_364)

    def lambda_374():
        OP_6B(4500, 7000)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_374)
    OP_43(0x8, 0x1, 0x0, 0x5)
    Sleep(300)
    OP_43(0x9, 0x1, 0x0, 0x6)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x8, 0x0)

    ChrTalk(    #2
        0x9,
        (
            "#277F#2P呼……\x01",
            "保养得十分彻底嘛。\x02\x03",

            "王国军方面似乎\x01",
            "整备得非常完善。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#6P哈哈，因为用过几次\x01",
            "作为飞行训练嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        "#6P我也亲自操纵过两三次。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x9,
        (
            "#277F#2P实际操纵的\x01",
            "感觉怎么样呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#6P啊，速度和机动性\x01",
            "都在我们军方警备飞艇以上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "#6P记得是三年前发表的\x01",
            "由莱恩福尔特社制造的\x01",
            "高速飞艇吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "#6P失礼了，凡提到飞艇\x01",
            "就以为是利贝尔制造的，\x01",
            "老实说真令人大吃一惊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x9,
        (
            "#277F#2P和贵国的警备艇相比，\x01",
            "装甲比较薄弱，\x01",
            "也无法搭载太多的武器。\x02\x03",

            "尽管如此，作为侦察机的话，\x01",
            "这制造成本也太高了。\x02\x03",

            "说实话，并不是一艘\x01",
            "适合军用的飞船啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        "#6P哦，是这样吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "#6P唔……明明是艘好飞船，\x01",
            "真觉得有点可惜啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x9,
        (
            "#272F#2P在我国似乎基本都是\x01",
            "作为贵族和资产家的业余爱好\x01",
            "来使用的。\x02\x03",

            "那个空贼团，原本\x01",
            "也是相同状况吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)

    ChrTalk(    #13
        0x8,
        (
            "#6P记得……\x01",
            "是『卡普亚男爵家』的吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)

    ChrTalk(    #14
        0x9,
        (
            "#270F#2P是原男爵家。\x02\x03",

            "由于积欠债务而失去领地，\x01",
            "连爵位也被剥夺了。\x02\x03",

            "其实这艘飞船也是抵押品之一，\x01",
            "债权人正要求交还呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "#6P原，原来如此……\x01",
            "似乎有不少内情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x9,
        (
            "#272F#2P无论如何，原帝国贵族\x01",
            "在贵国犯下罪行是事实。\x02\x03",

            "实在非常抱歉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        "#6P哈哈，不必在意。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "#6P那么何时可以\x01",
            "进行交接呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x9,
        (
            "#277F#2P快的话就这几天吧。\x02\x03",

            "毕竟你们这边似乎\x01",
            "也有很多事情要忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "#6P哈哈……\x01",
            "是政变事件的余党吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "#6P不过是逃亡者在做\x01",
            "最后的挣扎而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "#6P请不必担心，\x01",
            "很快就能逮捕归案的。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xA, -17490, 4000, -5790, 180)
    SetChrChipByIndex(0xA, 4)

    NpcTalk(    #23
        0xA,
        "女孩的声音",
        (
            "#1P呜哇～和之前来的时候相比\x01",
            "气氛有点不同呢～\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrPos(0xA, -17100, 2000, -11000, 180)

    def lambda_924():
        OP_6D(-12350, 4000, -10330, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_924)

    def lambda_93C():
        OP_6B(3830, 3000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_93C)
    OP_43(0xB, 0x1, 0x0, 0x7)
    Sleep(400)
    OP_43(0xA, 0x1, 0x0, 0x8)

    def lambda_95F():

        label("loc_95F")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_95F")

    QueueWorkItem2(0x9, 3, lambda_95F)
    Sleep(100)

    def lambda_975():

        label("loc_975")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_975")

    QueueWorkItem2(0x8, 3, lambda_975)
    Sleep(5000)

    def lambda_98B():
        OP_6D(-10820, 4000, -7210, 2000)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_98B)
    WaitChrThread(0xA, 0x1)
    OP_44(0x9, 0x3)
    OP_44(0x8, 0x3)
    OP_8C(0xA, 45, 400)
    Sleep(100)
    OP_8C(0xB, 45, 400)
    WaitChrThread(0xA, 0x0)

    ChrTalk(    #24
        0xA,
        (
            "#153F啊啊，空贼艇！？\x02\x03",

            "#150F哦～还放在\x01",
            "这个地方啊～\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0xA, 5)
    SetChrSubChip(0xA, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #25
        0xA,
        (
            "#151F嗯～不错呢～\x02\x03",

            "在夜间照明之下的身影\x01",
            "也好可爱呢～\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xA, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xA, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xA, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_8C(0xB, 180, 400)

    ChrTalk(    #26
        0xB,
        "#6P喂喂，这位小姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xB,
        (
            "#6P方便的话请摄影之前\x01",
            "先取得批准吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0xA, 4)
    SetChrSubChip(0xA, 0)
    OP_0D()
    OP_8C(0xA, 180, 600)
    Sleep(500)

    ChrTalk(    #28
        0xA,
        "#153F#6P#3S啊啊～！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_BB9():
        OP_6D(-8500, 4000, -21880, 3000)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_BB9)

    def lambda_BD1():
        OP_67(0, 3170, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_BD1)

    def lambda_BE9():
        OP_6C(169000, 3000)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_BE9)

    def lambda_BF9():
        OP_6B(4090, 3000)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_BF9)

    def lambda_C09():
        OP_6E(262, 3000)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C09)
    OP_8E(0xA, 0xFFFFD5EE, 0xFA0, 0xFFFFCBB2, 0x1388, 0x0)
    OP_8C(0xA, 180, 400)
    WaitChrThread(0x9, 0x1)

    ChrTalk(    #29
        0xA,
        (
            "#150F#5P在月光照耀下\x01",
            "深夜的迷雾峡谷……\x02\x03",

            "#151F嗯～多么梦幻\x01",
            "又可爱啊～\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0xA, 5)
    SetChrSubChip(0xA, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #30
        0xA,
        "#151F#5P来，茄～子㈱\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0xA, 5)
    SetChrSubChip(0xA, 0)
    OP_0D()
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xA, -300, 1300, 1000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xA, -300, 1300, 1000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xA, -300, 1300, 1000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    ChrTalk(    #31
        0xB,
        "#5P我，我说啊～……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(1000)
    OP_6D(-9870, 4000, -5820, 0)
    OP_67(0, 5730, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(145000, 0)
    OP_6E(342, 0)
    OP_8C(0x9, 180, 0)
    OP_0D()

    ChrTalk(    #32
        0x9,
        "#273F#5P……她是？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        "#5P哈哈，媒体的人啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "#5P刚才硬要跑到这个训练场\x01",
            "来采访。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "#5P之前的确是有预约，\x01",
            "不过这个时间过来也实在是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x9,
        "#272F#5P原来如此……\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0xA, 4)
    SetChrSubChip(0xA, 0)
    OP_0D()
    OP_8C(0xA, 0, 600)
    Sleep(500)

    ChrTalk(    #37
        0xA,
        "#153F#3S#6P啊啊啊啊！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_EFB():

        label("loc_EFB")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_EFB")

    QueueWorkItem2(0xB, 0, lambda_EFB)

    def lambda_F0C():
        OP_6D(-10080, 4000, -2580, 2000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_F0C)
    OP_8E(0xA, 0xFFFFD652, 0xFA0, 0xFFFFF0C4, 0x1388, 0x0)
    WaitChrThread(0xA, 0x1)
    OP_44(0xB, 0x0)

    ChrTalk(    #38
        0xA,
        (
            "#150F哦～穿着没见过的\x01",
            "军服呢～\x02\x03",

            "个子也好高～\x02\x03",

            "请问是隶属于\x01",
            "哪个部队的呢～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        "#273F#6P……不，我是………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xA,
        (
            "#151F啊，还没自我介绍呢～\x02\x03",

            "我是『利贝尔通讯』\x01",
            "杂志的摄影师\x01",
            "朵洛希·海娅特～\x02\x03",

            "为了杂志的特辑而来这个训练场\x01",
            "进行拍照的～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x9,
        (
            "#272F#6P……我是隶属于埃雷波尼亚帝国军，\x01",
            "驻利贝尔的武官——穆拉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xA,
        (
            "#153F埃雷波尼亚的军人！？\x02\x03",

            "#151F呜哇～我还是\x01",
            "第一次见到呢～\x02\x03",

            "因为１０年前的战争时\x01",
            "我还住在王都嘛～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x9,
        "#270F#6P是，是吗……\x02",
    )

    CloseMessageWindow()

    def lambda_10F7():
        OP_6D(-12340, 4000, -8660, 2000)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_10F7)
    Sleep(200)
    OP_43(0xC, 0x1, 0x0, 0x9)
    WaitChrThread(0xC, 0x2)
    Sleep(2000)

    def lambda_1125():
        OP_6D(-11560, 4000, -3660, 2000)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1125)
    WaitChrThread(0xC, 0x2)
    WaitChrThread(0xC, 0x1)

    ChrTalk(    #44
        0xC,
        "队长，打扰一下可以吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x8,
        "怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xC,
        "从司令部发来的联络。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xC,
        (
            "关于那些余党的动向\x01",
            "似乎有很大进展。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C1402   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_26F end

    def Function_3_11DA(): pass

    label("Function_3_11DA")

    SetChrPos(0xFE, -16500, 0, -8750, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFBF8C, 0xFA0, 0xFFFFBF8C, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFC4DC, 0xFA0, 0xFFFFBFDC, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_3_11DA end

    def Function_4_1220(): pass

    label("Function_4_1220")

    SetChrPos(0xFE, -17490, 0, -8830, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFBCD0, 0xFA0, 0xFFFFBF8C, 0xBB8, 0x0)
    Return()

    # Function_4_1220 end

    def Function_5_124B(): pass

    label("Function_5_124B")

    OP_8E(0xFE, 0xFFFFD6F2, 0xFA0, 0x1F4, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_5_124B end

    def Function_6_1267(): pass

    label("Function_6_1267")

    OP_8E(0xFE, 0xFFFFC61C, 0xFA0, 0xFFFFC072, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFD6FC, 0xFA0, 0xFFFFFB32, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_6_1267 end

    def Function_7_1297(): pass

    label("Function_7_1297")

    SetChrPos(0xFE, -16500, 0, -8750, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFBF8C, 0xFA0, 0xFFFFBF8C, 0xBB8, 0x0)
    OP_90(0xFE, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFD026, 0xFA0, 0xFFFFE408, 0xBB8, 0x0)
    Return()

    # Function_7_1297 end

    def Function_8_12EA(): pass

    label("Function_8_12EA")

    SetChrPos(0xFE, -17490, 0, -8830, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFBBAE, 0xFA0, 0xFFFFBF8C, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_90(0xFE, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFCF5E, 0xFA0, 0xFFFFDEF4, 0xBB8, 0x0)
    Return()

    # Function_8_12EA end

    def Function_9_1344(): pass

    label("Function_9_1344")

    SetChrPos(0xFE, -16500, 0, -8750, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFBBAE, 0xFA0, 0xFFFFBF8C, 0xFA0, 0x0)
    OP_90(0xFE, 0x9C4, 0x0, 0x0, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFCA7C, 0xFA0, 0xFFFFE70A, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 0)
    Return()

    # Function_9_1344 end

    def Function_10_139E(): pass

    label("Function_10_139E")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-17010, 4000, -16370, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(145000, 0)
    OP_6E(262, 0)
    OP_43(0x129, 0x1, 0x0, 0xB)
    Sleep(500)
    OP_43(0x12A, 0x1, 0x0, 0xC)
    Sleep(500)
    OP_43(0x146, 0x1, 0x0, 0xD)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0xE)
    WaitChrThread(0x129, 0x1)
    OP_8C(0x129, 45, 400)

    ChrTalk(    #48
        0x129,
        "#192F#2P喔喔……！\x02",
    )

    CloseMessageWindow()

    def lambda_1446():
        OP_6D(-7610, 4000, -1690, 7000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1446)

    def lambda_145E():
        OP_67(0, 5790, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_145E)

    def lambda_1476():
        OP_6E(255, 7000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1476)

    def lambda_1486():
        OP_6B(4660, 7000)
        ExitThread()

    QueueWorkItem(0x129, 3, lambda_1486)
    OP_43(0x129, 0x1, 0x0, 0xF)
    Sleep(300)
    OP_43(0x12A, 0x1, 0x0, 0x10)
    Sleep(300)
    OP_43(0x146, 0x1, 0x0, 0x11)
    Sleep(400)
    OP_43(0x102, 0x1, 0x0, 0x12)
    WaitChrThread(0x146, 0x1)

    ChrTalk(    #49
        0x129,
        (
            "#191F#6P可爱的『山猫号』……\x01",
            "真想死你了～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x146,
        (
            "#211F看起来\x01",
            "保养得很好呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x12A,
        (
            "#202F#5P嘿嘿，不愧是利贝尔军。\x01",
            "知道该怎么样好好对待飞船。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x102,
        (
            "#1035F#2P我知道你们很高兴，\x01",
            "不过时间所剩不多了。\x02\x03",

            "#1030F而且启动钥匙\x01",
            "现在还没找到。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x12A, 180, 400)

    ChrTalk(    #53
        0x12A,
        "#200F#6P是是，知道啦。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x129, 180, 400)
    OP_8C(0x146, 180, 400)

    ChrTalk(    #54
        0x129,
        (
            "#198F#6P真是的……\x01",
            "再让我们沉浸一下嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x146,
        (
            "#210F#6P启动钥匙要是\x01",
            "留在船里就好了……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1804)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_10_139E end

    def Function_11_163F(): pass

    label("Function_11_163F")

    SetChrPos(0xFE, -17220, 0, -8680, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFE0C0, 0xBB8, 0x0)
    Return()

    # Function_11_163F end

    def Function_12_166A(): pass

    label("Function_12_166A")

    SetChrPos(0xFE, -17220, 0, -8680, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFE55C, 0xBB8, 0x0)
    Return()

    # Function_12_166A end

    def Function_13_1695(): pass

    label("Function_13_1695")

    SetChrPos(0xFE, -17220, 0, -8680, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFE944, 0xBB8, 0x0)
    Return()

    # Function_13_1695 end

    def Function_14_16C0(): pass

    label("Function_14_16C0")

    SetChrPos(0xFE, -17220, 0, -8680, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFED2C, 0xBB8, 0x0)
    Return()

    # Function_14_16C0 end

    def Function_15_16EB(): pass

    label("Function_15_16EB")

    OP_90(0xFE, 0x9C4, 0x0, 0x0, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFD6FC, 0xFA0, 0x2DA, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_15_16EB end

    def Function_16_171B(): pass

    label("Function_16_171B")

    OP_90(0xFE, 0x0, 0x0, 0xFFFFFC18, 0xBB8, 0x0)
    OP_90(0xFE, 0x9C4, 0x0, 0x0, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFD5EE, 0xFA0, 0xFFFFFE20, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_16_171B end

    def Function_17_175F(): pass

    label("Function_17_175F")

    OP_90(0xFE, 0x0, 0x0, 0xFFFFF830, 0xBB8, 0x0)
    OP_90(0xFE, 0x9C4, 0x0, 0x0, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFD0E4, 0xFA0, 0x2D0, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_17_175F end

    def Function_18_17A3(): pass

    label("Function_18_17A3")

    OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xBB8, 0x0)
    OP_90(0xFE, 0x9C4, 0x0, 0x0, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFD210, 0xFA0, 0xFFFFF9B6, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_18_17A3 end

    def Function_19_17E7(): pass

    label("Function_19_17E7")

    OP_51(0xD, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x0, 0x1, 0x0, 0x17)
    OP_43(0x1, 0x1, 0x0, 0x16)
    OP_43(0x2, 0x1, 0x0, 0x15)
    OP_43(0x3, 0x1, 0x0, 0x14)
    WaitChrThread(0x3, 0x1)
    OP_30(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_19_17E7 end

    def Function_20_18CB(): pass

    label("Function_20_18CB")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0xF, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0xE, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0xD, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 90, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFDD3C, 0x1586, 0xFFFFFD80, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_20_18CB end

    def Function_21_1923(): pass

    label("Function_21_1923")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0xE, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0xD, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 90, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFDD3C, 0x1586, 0xFFFFFD80, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_21_1923 end

    def Function_22_196D(): pass

    label("Function_22_196D")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0xD, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 90, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFDD3C, 0x1586, 0xFFFFFD80, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_22_196D end

    def Function_23_19A9(): pass

    label("Function_23_19A9")

    SetChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 90, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFDD3C, 0x1586, 0xFFFFFD80, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_23_19A9 end

    def Function_24_19D7(): pass

    label("Function_24_19D7")

    OP_51(0xD, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x0, 0x1, 0x0, 0x1C)
    OP_43(0x1, 0x1, 0x0, 0x1B)
    OP_43(0x2, 0x1, 0x0, 0x1A)
    OP_43(0x3, 0x1, 0x0, 0x19)
    WaitChrThread(0x3, 0x1)
    OP_30(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_24_19D7 end

    def Function_25_1ABB(): pass

    label("Function_25_1ABB")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0xF, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0xE, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0xD, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 270, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFD508, 0xFA0, 0xFFFFF83A, 0x1F4, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_25_1ABB end

    def Function_26_1B13(): pass

    label("Function_26_1B13")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0xE, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0xD, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 270, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFD508, 0xFA0, 0xFFFFF83A, 0x1F4, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_26_1B13 end

    def Function_27_1B5D(): pass

    label("Function_27_1B5D")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0xD, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 270, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFD508, 0xFA0, 0xFFFFF83A, 0x1F4, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_27_1B5D end

    def Function_28_1B99(): pass

    label("Function_28_1B99")

    SetChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 270, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFD508, 0xFA0, 0xFFFFF83A, 0x1F4, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_28_1B99 end

    SaveToFile()

Try(main)
