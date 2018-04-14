from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4133   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4133.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        '管事福利兹',                           # 9
        '提妲',                                 # 10
        '玲',                                   # 11
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
        'ED6_DT07/CH01220 ._CH',             # 00
        'ED6_DT07/CH00060 ._CH',             # 01
        'ED6_DT27/CH03510 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01220P._CP',             # 00
        'ED6_DT07/CH00060P._CP',             # 01
        'ED6_DT27/CH03510P._CP',             # 02
    )

    DeclNpc(
        X                   = 7410,
        Z                   = 0,
        Y                   = 3300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 7200,
        TriggerZ            = 0,
        TriggerY            = 1690,
        TriggerRange        = 800,
        ActorX              = 7410,
        ActorZ              = 1500,
        ActorY              = 3300,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7000,
        TriggerZ            = 0,
        TriggerY            = 4890,
        TriggerRange        = 800,
        ActorX              = 7000,
        ActorZ              = 1000,
        ActorY              = 4890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_16A",          # 00, 0
        "Function_1_17E",          # 01, 1
        "Function_2_17F",          # 02, 2
        "Function_3_2FC",          # 03, 3
        "Function_4_301",          # 04, 4
        "Function_5_31A",          # 05, 5
        "Function_6_15D1",         # 06, 6
        "Function_7_166A",         # 07, 7
    )


    def Function_0_16A(): pass

    label("Function_0_16A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_17D")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_17D")

    Return()

    # Function_0_16A end

    def Function_1_17E(): pass

    label("Function_1_17E")

    Return()

    # Function_1_17E end

    def Function_2_17F(): pass

    label("Function_2_17F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A4")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_2E6")

    label("loc_1A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BD")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_2E6")

    label("loc_1BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D6")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_2E6")

    label("loc_1D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EF")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_2E6")

    label("loc_1EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_208")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_2E6")

    label("loc_208")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_221")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_2E6")

    label("loc_221")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23A")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_2E6")

    label("loc_23A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_253")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_2E6")

    label("loc_253")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26C")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_2E6")

    label("loc_26C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_285")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_2E6")

    label("loc_285")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29E")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_2E6")

    label("loc_29E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B7")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_2E6")

    label("loc_2B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D0")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_2E6")

    label("loc_2D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E6")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_2E6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2FB")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_2E6")

    label("loc_2FB")

    Return()

    # Function_2_17F end

    def Function_3_2FC(): pass

    label("Function_3_2FC")

    Call(0, 4)
    Return()

    # Function_3_2FC end

    def Function_4_301(): pass

    label("Function_4_301")

    TalkBegin(0x8)

    ChrTalk(    #0
        0x8,
        "◆没有台词。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Return()

    # Function_4_301 end

    def Function_5_31A(): pass

    label("Function_5_31A")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32D")
    Call(0, 6)

    label("loc_32D")

    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x101, 6950, 0, 1690, 0)
    SetChrPos(0xF7, 8109, 0, 1700, 0)
    SetChrPos(0xA, 7130, 0, 450, 0)
    SetChrPos(0x9, 8039, 0, 590, 0)
    OP_6D(7310, 0, 2300, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(309000, 0)
    OP_6E(262, 0)
    OP_4A(0x8, 255)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #1
        0x8,
        (
            "你们是游击士协会的吧？\x01",
            "我已经收到联络了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "不巧，没有\x01",
            "４人房了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "能不能请你们分住\x01",
            "两间双人房？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4BC")

    ChrTalk(    #4
        0x101,
        "#1004F#6P哦，这样啊。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)
    Sleep(500)

    ChrTalk(    #5
        0x101,
        (
            "#1015F#5P阿加特。\x01",
            "那么怎么分呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #6
        0x106,
        (
            "#051F#4P我无所谓。\x02\x03",

            "你们来\x01",
            "决定吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53D")

    label("loc_4BC")


    ChrTalk(    #7
        0x101,
        "#1004F#6P哦，这样啊。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)
    Sleep(500)

    ChrTalk(    #8
        0x101,
        (
            "#1015F#5P雪拉姐。\x01",
            "那么怎么分呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #9
        0x103,
        (
            "#027F#4P我怎么住都行。\x02\x03",

            "你们来\x01",
            "决定吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53D")


    ChrTalk(    #10
        0xA,
        (
            "#265F#6P那玲就和姐姐\x01",
            "一起吧。\x02\x03",

            "姐姐成天工作，\x01",
            "也没办法好好聊聊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_589():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_589)

    def lambda_597():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_597)
    TurnDirection(0x101, 0xA, 400)
    OP_62(0x9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(300)

    ChrTalk(    #11
        0x9,
        (
            "#065F#6P啊，小玲好狡猾。\x02\x03",

            "我也想和姐姐\x01",
            "一个房间……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 400)

    ChrTalk(    #12
        0xA,
        (
            "#263F#5P哼哼，先到先得哦。\x02\x03",

            "#260F那么你跟我\x01",
            "挤一张床？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x9,
        (
            "#061F#6P嘿嘿，我逗你的。\x02\x03",

            "今晚就把姐姐\x01",
            "让给小玲了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xA,
        (
            "#261F#5P呵呵。\x01",
            "谢谢你，提妲。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #15
        0x101,
        (
            "#1016F#5P嗯……\x01",
            "我被让出去了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_75D")

    ChrTalk(    #16
        0x106,
        (
            "#051F#2P那么我和\x01",
            "小不点一起。\x02\x03",

            "哈哈，让我想起和老爷子\x01",
            "还有你潜伏时的情景。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)

    ChrTalk(    #17
        0x9,
        (
            "#560F#6P啊……\x02\x03",

            "#067F嘿嘿，是啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D9")

    label("loc_75D")


    ChrTalk(    #18
        0x103,
        (
            "#021F#2P呵呵，你还真受欢迎。\x02\x03",

            "#027F那么我就和\x01",
            "提妲一起。\x02\x03",

            "我们在睡前\x01",
            "用塔罗牌做游戏吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)

    ChrTalk(    #19
        0x9,
        "#061F#6P嗯，好啊！\x02",
    )

    CloseMessageWindow()

    label("loc_7D9")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrPos(0x101, 35000, 0, 106370, 0)
    SetChrPos(0xA, 35000, 0, 106370, 0)
    OP_6D(35000, 0, 113130, 0)
    OP_67(0, 6110, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(239, 0)
    OP_6B(1890, 0)
    OP_6C(315000, 0)
    OP_6E(437, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    ClearChrFlags(0xA, 0x80)

    def lambda_8A7():
        OP_6D(34540, 0, 115470, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8A7)

    def lambda_8BF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_8BF)

    def lambda_8D1():
        OP_8E(0xFE, 0x8674, 0x0, 0x1BD5A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_8D1)
    Sleep(600)
    ClearChrFlags(0x101, 0x80)

    def lambda_8F6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8F6)

    def lambda_908():
        OP_8E(0xFE, 0x8BBA, 0x0, 0x1BDAA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_908)
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #20
        0xA,
        (
            "#265F#5P哇，这跟我和爸爸妈妈\x01",
            "一起住的房间不一样呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 45, 400)
    Sleep(500)
    OP_8C(0xA, 0, 400)
    OP_8C(0xA, 270, 400)
    Sleep(500)
    OP_8C(0xA, 0, 400)

    ChrTalk(    #21
        0xA,
        (
            "#261F#5P从前面的窗户还能\x01",
            "看见高大的建筑物……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        "#1026F#6P啊……\x02",
    )

    CloseMessageWindow()
    OP_AD(0x2400C2, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    Sleep(2000)
    OP_AE(0x1F4)
    Sleep(1500)
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #23
        0xA,
        "#264F#5P怎么了？姐姐？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(    #24
        0x101,
        (
            "#1016F#6P啊，嗯，有点出神了\x02\x03",

            "#1025F话说回来……\x01",
            "小玲，对不起。\x02\x03",

            "一直没能找到\x01",
            "你的爸爸妈妈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xA,
        (
            "#260F#5P不，没关系的。\x02\x03",

            "因为爸爸妈妈\x01",
            "说好一定会\x01",
            "来接玲的。\x02\x03",

            "姐姐你们不用\x01",
            "勉强找他们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        "#1026F#6P可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xA,
        (
            "#263F#5P玲的爸爸妈妈\x01",
            "捉迷藏很拿手的。\x02\x03",

            "虽然比不上玲那样擅长。\x02\x03",

            "所以没那么容易\x01",
            "找到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#1016F#6P哈哈，是吗。\x02\x03",

            "#1006F那我们就不勉强了，\x01",
            "仔细地慢慢找吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xA,
        (
            "#261F#5P嗯，这就对了。\x02\x03",

            "#260F不过……\x01",
            "玲有两个愿望\x01",
            "要姐姐满足。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        "#1004F#6P愿望？　是什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xA,
        (
            "#1306F#5P哎呀，不可以。\x02\x03",

            "在说好答应我\x01",
            "之前我不能说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#1016F#6P给我来这一手……\x02\x03",

            "#1006F只要我办得到就都\x01",
            "满足你，行了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xA,
        (
            "#261F#5P真的？　太好了！\x02\x03",

            "#260F第一个愿望是……\x01",
            "叫我玲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#1015F#6P？？？\x02\x03",

            "#1004F啊……！\x01",
            "不再叫你小玲？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xA,
        (
            "#260F#5P嗯，没错。\x02\x03",

            "#266F你明明对提妲直呼其名，\x01",
            "却总是叫我『小玲』，\x01",
            "这可有点不公平。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#1016F#6P哈哈……是吗？\x02\x03",

            "#1011F嗯，这个不难……\x02\x03",

            "那么你能不能也\x01",
            "叫我艾丝蒂尔？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xA,
        (
            "#264F#5P叫姐姐你？\x02\x03",

            "#267F艾丝蒂尔……艾丝蒂尔……\x02\x03",

            "#261F嗯，好像也不坏⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        (
            "#1016F#6P啊哈哈……\x01",
            "那就这么定了。\x02\x03",

            "#1006F今后请多关照，玲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xA,
        (
            "#265F#5P彼此彼此，艾丝蒂尔。\x02\x03",

            "#261F呵呵……真开心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#1017F#6P呵呵，那就好那就好。\x02\x03",

            "那么玲的\x01",
            "另一个愿望是？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xA,
        (
            "#267F#5P嗯，是这样的……\x02\x03",

            "能不能告诉我，你刚才\x01",
            "进房间时为什么会感到吃惊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        "#1026F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xA,
        (
            "#268F#5P艾丝蒂尔那时有一种\x01",
            "悲伤的表情。\x02\x03",

            "所以我挺在意的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#1003F#6P……是这个啊。\x02\x03",

            "#1025F以前，我曾和一个人\x01",
            "同住过这间房间。\x02\x03",

            "刚才有点回忆起\x01",
            "那个人了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xA,
        (
            "#265F#5P哇！\x01",
            "肯定是恋人吧！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#1017F#6P呵呵……\x01",
            "很遗憾，不是这样的。\x02\x03",

            "他和我在一个家庭中长大，\x01",
            "像我的兄弟一样。\x02\x03",

            "虽然现在不在\x01",
            "我身边……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xA,
        (
            "#264F#5P这样啊……\x02\x03",

            "#265F那个哥哥是个\x01",
            "什么样的人呢？\x02\x03",

            "名字叫什么？　长相如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#1025F#6P啊，嗯……\x01",
            "他叫约修亚。\x02\x03",

            "黑发、琥珀色的眼睛，\x01",
            "应该算相当英俊吧。\x02\x03",

            "#1015F嗯～比起英俊这种形容法，\x01",
            "可能更应该说他是个美人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xA,
        "#264F#5P美人？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        (
            "#1016F#6P呵呵，因为他还在戏里\x01",
            "演过公主呢。\x02\x03",

            "而且我跟你说，那叫\x01",
            "一个像啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xA,
        (
            "#261F#5P哇，好厉害～\x02\x03",

            "玲也好想\x01",
            "见到他。\x02\x03",

            "我说我说，什么时候能见他？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        (
            "#1025F#6P啊，嗯……\x01",
            "这就不好说了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xA,
        (
            "#267F#5P…………………………\x02\x03",

            "你是不是因为不知道\x01",
            "什么时候能见到他才感到悲伤？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        (
            "#1006F#6P……不，这倒没有。\x02\x03",

            "因为不管用多少年的时间，\x01",
            "我都要带他回家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xA,
        "#264F#5P那么是因为什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        (
            "#1025F#6P因为我想约修亚\x01",
            "现在一定在勉强自己……\x02\x03",

            "#1003F可是……\x01",
            "可我却不能在他身边支持他，\x01",
            "……就有点悲伤。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xA,
        "#262F#5P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        (
            "#1016F#6P哈哈，抱歉抱歉\x02\x03",

            "#1025F这些对不了解情况的玲来说\x01",
            "一定是很没意思吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xA,
        (
            "#263F#5P不，完全没有。\x02\x03",

            "#260F那个叫约修亚的\x01",
            "哥哥一定是个很棒的人吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        (
            "#1007F#6P很棒的人吗……\x01",
            "我倒是觉得他很过分。\x02\x03",

            "#1013F用了那样自说自话的道别方式，\x01",
            "……我、我的第一次就那么……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xA,
        "#264F#5P？　第一次？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1004F#6P啊，没什么的！\x02\x03",

            "#1016F今天我们都累了，\x01",
            "准备睡觉吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xA,
        (
            "#1301F#5P啊，不许蒙混过关！\x02\x03",

            "#266F讨厌，在你全部招供之前\x01",
            "我绝对不睡！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        "#1015F#6P呜呜，糟糕了……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #65
        (
            "\x07\x05后来，艾丝蒂尔她们在上床以后\x01",
            "又聊了很多无关紧要的内容。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #66
        (
            "\x07\x05玲逐渐地在恍惚间\x01",
            "发出了平稳的鼾声……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #67
        (
            "\x07\x05劳累的艾丝蒂尔也很快\x01",
            "失去了意识。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(200)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/R1504   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_31A end

    def Function_6_15D1(): pass

    label("Function_6_15D1")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_164B"),
        (1, "loc_1651"),
        (SWITCH_DEFAULT, "loc_1657"),
    )


    label("loc_164B")

    OP_A2(0x1200)
    Jump("loc_1657")

    label("loc_1651")

    OP_A2(0x1201)
    Jump("loc_1657")

    label("loc_1657")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1665")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_1669")

    label("loc_1665")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_1669")

    Return()

    # Function_6_15D1 end

    def Function_7_166A(): pass

    label("Function_7_166A")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #68
        (
            "\x07\x05　　　　　　　事务室\x01",
            "※无关人员请勿入内\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_166A end

    SaveToFile()

Try(main)
