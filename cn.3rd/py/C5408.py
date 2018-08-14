from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5408   ._SN',
        MapName             = 'Other',
        Location            = 'C5408.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60028",
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
        '德尔基昂',                             # 9
        '德尔基昂',                             # 10
        '莱维',                                 # 11
        '怪盗布卢布兰',                         # 12
        '幻惑之铃露茜奥拉',                     # 13
        '瘦狼瓦鲁特',                           # 14
        '目标用照相机',                         # 15
        '',                                     # 16
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
        'ED6_DT26/CH20243 ._CH',             # 00
        'ED6_DT07/CH02040 ._CH',             # 01
        'ED6_DT27/CH03530 ._CH',             # 02
        'ED6_DT27/CH03520 ._CH',             # 03
        'ED6_DT26/CH20280 ._CH',             # 04
        'ED6_DT26/CH20762 ._CH',             # 05
        'ED6_DT26/CH20761 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT26/CH20243P._CP',             # 00
        'ED6_DT07/CH02040P._CP',             # 01
        'ED6_DT27/CH03530P._CP',             # 02
        'ED6_DT27/CH03520P._CP',             # 03
        'ED6_DT26/CH20280P._CP',             # 04
        'ED6_DT26/CH20762P._CP',             # 05
        'ED6_DT26/CH20761P._CP',             # 06
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0xC5,
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

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1C2",          # 00, 0
        "Function_1_1F9",          # 01, 1
        "Function_2_1FA",          # 02, 2
        "Function_3_C37",          # 03, 3
        "Function_4_141B",         # 04, 4
        "Function_5_1E3B",         # 05, 5
        "Function_6_1EE6",         # 06, 6
        "Function_7_1F33",         # 07, 7
        "Function_8_1F4D",         # 08, 8
        "Function_9_1F69",         # 09, 9
    )


    def Function_0_1C2(): pass

    label("Function_0_1C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_1EA")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)

    label("loc_1EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_1F8")
    OP_A3(0x2505)
    Event(0, 4)

    label("loc_1F8")

    Return()

    # Function_0_1C2 end

    def Function_1_1F9(): pass

    label("Function_1_1F9")

    Return()

    # Function_1_1F9 end

    def Function_2_1FA(): pass

    label("Function_2_1FA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EB")
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #0
        (
            "\x07\x00◆Debug用Flag（分支）判定《瓦鲁特篇》\x01",
            "　空之轨迹ＳＣ——终章中枢塔战的状态。\x02",
        )
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇金在队伍中且打倒了瓦鲁特】\x01",        # 0
            "【◇金不在队伍中且打倒了瓦鲁特】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2F7"),
        (1, "loc_2FD"),
        (SWITCH_DEFAULT, "loc_303"),
    )


    label("loc_2F7")

    OP_A2(0x2235)
    Jump("loc_303")

    label("loc_2FD")

    OP_A3(0x2235)
    Jump("loc_303")

    label("loc_303")

    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x00◆Debug用Flag（分支）判定《露茜奥拉篇》\x01",
            "　空之轨迹ＳＣ——终章中枢塔战的状态。\x02",
        )
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇雪拉在队伍中且打倒了露茜奥拉】\x01",        # 0
            "【◇雪拉不在队伍中且打倒了露茜奥拉】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3DD"),
        (1, "loc_3E3"),
        (SWITCH_DEFAULT, "loc_3E9"),
    )


    label("loc_3DD")

    OP_A2(0x2238)
    Jump("loc_3E9")

    label("loc_3E3")

    OP_A3(0x2238)
    Jump("loc_3E9")

    label("loc_3E9")

    OP_56(0x0)

    label("loc_3EB")

    Sleep(500)
    OP_22(0x85, 0x3C, 0x64)
    OP_1D(0x1C)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05『辉之环』崩毁之后――\x02\x03",

            "在云间航行的\x01",
            "巨大船影上――\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_24(0x85, 0x46)
    Sleep(100)
    OP_24(0x85, 0x50)
    Sleep(100)
    OP_24(0x85, 0x5A)
    Sleep(100)
    OP_24(0x85, 0x64)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 5480, 0, -55430, 90)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 3240, 0, -54970, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AA")
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 3630, 0, -56800, 90)

    label("loc_4AA")

    OP_6F(0x1, 0)
    OP_72(0x1001, 0x0)
    ExitThread()
    OP_72(0x801, 0x0)
    ExitThread()
    OP_6D(4710, 0, -11170, 0)
    OP_67(0, 9300, -10000, 0)
    OP_6B(5100, 0)
    OP_6C(45000, 0)
    OP_6E(665, 0)

    def lambda_500():
        OP_6D(4680, 0, -52670, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_500)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x0, 0x0)
    Fade(500)
    OP_6D(5130, 200, -54700, 0)
    OP_67(0, 5010, -10000, 0)
    OP_6B(2820, 0)
    OP_6C(45000, 0)
    OP_6E(345, 0)
    OP_11(0xFF, 0xFF, 0xFF, 0x372D0, 0x69B68, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #3
        0x13,
        (
            "#230F#2P哦哦……诸位，看啊！\x02\x03",

            "我们所追求的梦幻之地，\x01",
            "现在正在崩毁呢！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 5)), scpexpr(EXPR_END)), "loc_618")

    ChrTalk(    #4
        0x15,
        (
            "#250F#6P嘻嘻嘻……\x01",
            "结局很明了嘛。\x02\x03",

            "这场战斗……\x01",
            "是我们输了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_670")

    label("loc_618")


    ChrTalk(    #5
        0x15,
        (
            "#250F#6P嘁……\x01",
            "本该胜利的战斗都输了。\x02\x03",

            "这都是因为教授那家伙\x01",
            "凭兴趣乱来的缘故。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E6")

    ChrTalk(    #6
        0x14,
        (
            "#240F#4P一切都重归于无了吗……\x02\x03",

            "那个都市消失了，\x01",
            "我们的任务也结束了……\x02\x03",

            "……又要暂时告别了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_75C")

    label("loc_6E6")


    ChrTalk(    #7
        0x13,
        (
            "#230F#2P一切都重归于无了……吗。\x02\x03",

            "那个都市消失了，\x01",
            "我们的任务也结束了……\x02\x03",

            "嗯，\x01",
            "要和你们暂时告别了。\x02",
        )
    )

    Jump("loc_75B")

    label("loc_75B")

    CloseMessageWindow()

    label("loc_75C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 5)), scpexpr(EXPR_END)), "loc_8BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C0")

    ChrTalk(    #8
        0x15,
        (
            "#250F#5P………………………………\x02\x03",

            "哼……\x01",
            "不一定有再见的机会了。\x02",
        )
    )

    Jump("loc_7BC")

    label("loc_7BC")

    CloseMessageWindow()
    Jump("loc_812")

    label("loc_7C0")


    ChrTalk(    #9
        0x15,
        (
            "#250F#6P………………………………\x02\x03",

            "哼……\x01",
            "不一定有再见的机会了。\x02",
        )
    )

    Jump("loc_811")

    label("loc_811")

    CloseMessageWindow()

    label("loc_812")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_875")
    OP_8C(0x14, 0, 400)
    Sleep(200)

    ChrTalk(    #10
        0x14,
        (
            "#240F#4P啊……\x02\x03",

            "难道……\x01",
            "你想要脱离『结社』吗？\x02",
        )
    )

    Jump("loc_86A")

    label("loc_86A")

    CloseMessageWindow()
    OP_8C(0x15, 180, 400)
    Jump("loc_8BC")

    label("loc_875")

    OP_8C(0x13, 270, 400)
    Sleep(200)

    ChrTalk(    #11
        0x13,
        (
            "#230F#2P哦？这真奇怪。\x02\x03",

            "难道你……\x01",
            "打算脱离组织？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94A")

    ChrTalk(    #12
        0x15,
        (
            "#250F#5P难说……\x01",
            "我还不知道会怎样。\x02\x03",

            "但是，遵从自己的意志\x01",
            "是我们『执行者』的原则……\x02\x03",

            "在哪里、怎样生活，\x01",
            "都是我的自由。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CD")

    label("loc_94A")


    ChrTalk(    #13
        0x15,
        (
            "#250F#6P难说……\x01",
            "我还不知道会怎样。\x02\x03",

            "但是，遵从自己的意志\x01",
            "是我们『执行者』的原则……\x02\x03",

            "在哪里、怎样生活，\x01",
            "都是我的自由。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9CD")

    OP_8C(0x13, 270, 400)

    ChrTalk(    #14
        0x13,
        (
            "#230F#2P唔……确实。\x02\x03",

            "不过，作为礼节，\x01",
            "现在还是约定再会吧。\x02\x03",

            "希望将来在某处战场上，\x01",
            "还能彼此相见……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A74")
    OP_8C(0x14, 0, 400)

    ChrTalk(    #15
        0x14,
        "#240F#4P呵呵，是啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_A74")

    label("loc_A74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 5)), scpexpr(EXPR_END)), "loc_AE6")

    ChrTalk(    #16
        0x15,
        (
            "#250F#6P哼……\x02\x03",

            "战场……\x01",
            "有什么好约的。\x02\x03",

            "我们要是碰头的话，\x01",
            "那里肯定会化为血海。\x02",
        )
    )

    Jump("loc_AE2")

    label("loc_AE2")

    CloseMessageWindow()
    Jump("loc_C15")

    label("loc_AE6")


    ChrTalk(    #17
        0x15,
        (
            "#250F#6P啊啊，大概吧。\x02\x03",

            "不过，我们的活动\x01",
            "可不止如此而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x13,
        (
            "#230F#2P呵呵，没错。\x02\x03",

            "那么，告别之前，\x01",
            "就遵从礼节约定再会吧。\x02\x03",

            "希望将来在某处战场上，\x01",
            "还能彼此相见……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BDC")

    ChrTalk(    #19
        0x14,
        (
            "#240F#4P嗯，再会了。\x02\x03",

            "循着命运之线的引导……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C15")

    label("loc_BDC")


    ChrTalk(    #20
        0x15,
        (
            "#250F#6P哦……\x02\x03",

            "后会有期，\x01",
            "在同一片血海中相见。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C15")

    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/C5401   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1FA end

    def Function_3_C37(): pass

    label("Function_3_C37")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_72(0x401, 0x0)
    ExitThread()
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_72(0x801, 0x0)
    ExitThread()
    OP_6F(0x1, 0)
    OP_72(0x402, 0x0)
    ExitThread()
    OP_72(0x2002, 0x0)
    ExitThread()
    OP_72(0x802, 0x0)
    ExitThread()
    OP_6F(0x2, 0)
    OP_C4(0x0, 0x10)
    OP_48()
    FadeToBright(1, 0)
    OP_1D(0xD4)
    Sleep(500)
    PlayMovie(0x0, "ED6_DT50.dat", 0x0, 0x1)
    Sleep(1000)
    OP_56(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    Sleep(500)
    OP_C4(0x1, 0x10)
    LoadEffect(0x1, "map\\\\mp303_00.eff")
    OP_22(0x85, 0x1, 0xA)
    Sleep(200)
    OP_24(0x85, 0x14)
    Sleep(200)
    OP_24(0x85, 0x1E)
    Sleep(200)
    OP_24(0x85, 0x28)
    Sleep(200)
    OP_24(0x85, 0x32)
    OP_22(0x131, 0x1, 0x14)
    Sleep(200)
    OP_24(0x85, 0x3C)
    OP_24(0x131, 0x1E)
    Sleep(200)
    OP_24(0x85, 0x46)
    OP_24(0x131, 0x28)
    Sleep(200)
    OP_24(0x85, 0x50)
    OP_24(0x131, 0x32)
    Sleep(200)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 7600, 0, -55320, 87)
    SetChrChipByIndex(0x13, 2)
    SetChrSubChip(0x13, 0)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 7600, 0, -56500, 270)
    SetChrChipByIndex(0x15, 5)
    SetChrSubChip(0x15, 0)
    OP_6F(0x1, 0)
    OP_72(0x1001, 0x0)
    ExitThread()
    OP_72(0x801, 0x0)
    ExitThread()
    OP_6D(0, 200, -21020, 0)
    OP_67(0, 13020, -10000, 0)
    OP_6B(5100, 0)
    OP_6C(0, 0)
    OP_6E(665, 0)

    def lambda_DDB():
        OP_6D(8320, 200, -56180, 9000)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_DDB)

    def lambda_DF3():
        OP_67(0, 7280, -10000, 9000)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_DF3)

    def lambda_E0B():
        OP_6C(58000, 9000)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_E0B)

    def lambda_E1B():
        OP_6E(465, 9000)
        ExitThread()

    QueueWorkItem(0x16, 3, lambda_E1B)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x16, 0x0)
    Fade(500)
    OP_11(0xFF, 0xFF, 0xFF, 0x372D0, 0x69B68, 0x0)
    OP_6D(8500, 200, -55800, 0)
    OP_67(0, 4480, -10000, 0)
    OP_6B(2620, 0)
    OP_6C(68000, 0)
    OP_6E(344, 0)
    OP_8C(0x13, 135, 0)
    OP_0D()

    def lambda_E94():
        OP_6B(2420, 30000)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_E94)
    Sleep(1000)

    ChrTalk(    #21
        0x13,
        "#232F#5P#30W………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x15,
        (
            "#257F#6P#30W………………………………\x02\x03",

            "#255F……喂，布卢布兰。\x02\x03",

            "别一声不吭的，说点什么啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x13,
        (
            "#231F#5P#30W哼，你还不是一样……\x02\x03",

            "#230F在这光景面前……\x01",
            "任何语言都是无力的吧。\x02\x03",

            "只有被畏惧……\x01",
            "完全打倒而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x15,
        "#256F#6P#30W……啧……………………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x15)
    Sleep(500)

    ChrTalk(    #25
        0x15,
        (
            "#257F#6P#30W……结果，\x01",
            "其他人都没回来……\x02\x03",

            "#253F喂……这还真是不像话啊！ \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x13,
        (
            "#232F#5P#30W……玲似乎已经\x01",
            "脱离这个空域了。\x02\x03",

            "露茜奥拉行踪不明……\x01",
            "不过我们担心她也没用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x15,
        (
            "#252F#6P#30W呵呵……\x01",
            "我才没担心。\x02\x03",

            "#250F不过，\x01",
            "要是那女人死了倒也有点可惜。\x02\x03",

            "现在也只能祈祷\x01",
            "她别白白死去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x13,
        (
            "#231F#5P#30W呵呵，同感。\x02\x03",

            "#232F只是……\x01",
            "莱维大概没希望了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x15,
        (
            "#257F#6P#30W……是啊。\x02\x03",

            "#256F啧，若知是这样，\x01",
            "早点和他比试一下就好了。\x02\x03",

            "那个混帐，\x01",
            "总是找借口逃避比试……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x13,
        (
            "#230F#5P#30W他和我们不同，\x01",
            "有自己明确的目的。\x02\x03",

            "而且看来……\x01",
            "似乎已经达成这个目的了。\x02\x03",

            "现在应该很满足了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x15,
        "#257F#6P#30W嘁……\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_12F6():
        OP_6B(2320, 3000)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_12F6)

    def lambda_1306():
        OP_99(0xFE, 0x0, 0x6, 0x320)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_1306)
    WaitChrThread(0x15, 0x2)
    OP_22(0x2E4, 0x0, 0x46)
    PlayEffect(0x1, 0x0, 0x15, -200, 100, -150, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_22(0x2E5, 0x0, 0x64)
    OP_82(0x0, 0x2)

    def lambda_1362():
        OP_99(0xFE, 0x6, 0x8, 0x320)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_1362)
    WaitChrThread(0x15, 0x2)
    Sleep(1500)
    PlayEffect(0x1, 0x0, 0x15, -350, 100, -80, 0, 0, 0, 600, 700, 600, 0xFF, 0, 0, 0, 0)
    Sleep(800)

    ChrTalk(    #32
        0x15,
        "#254F#5P#30W……祭典之后……吗………\x02",
    )

    CloseMessageWindow()

    def lambda_13E7():
        OP_6D(16000, 200, -55800, 4000)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_13E7)
    FadeToDark(3000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    SetMapFlags(0x100000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/C5400   ._SN", 109, 0, 0)
    IdleLoop()
    Return()

    # Function_3_C37 end

    def Function_4_141B(): pass

    label("Function_4_141B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x124, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 1020, 150, -14080, 180)
    SetChrPos(0x10, 4550, 0, -32170, 270)
    OP_A1(0x10, 0x4)
    ClearChrFlags(0x10, 0x1)
    SetChrFlags(0x10, 0x1)
    ClearChrFlags(0x10, 0x80)
    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xC350), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_72(0x401, 0x0)
    ExitThread()
    OP_6F(0x1, 0)
    OP_70(0x1, 0x0)
    OP_6D(-1910, 14950, -20340, 0)
    OP_67(0, 4490, -10000, 0)
    OP_6B(2550, 0)
    OP_6C(45000, 0)
    OP_6E(405, 0)

    def lambda_14F1():
        OP_6D(3040, 0, -18590, 6000)
        ExitThread()

    QueueWorkItem(0x124, 0, lambda_14F1)

    def lambda_1509():
        OP_67(0, 4960, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x124, 1, lambda_1509)

    def lambda_1521():
        OP_6B(2550, 6000)
        ExitThread()

    QueueWorkItem(0x124, 2, lambda_1521)

    def lambda_1531():
        OP_6E(405, 6000)
        ExitThread()

    QueueWorkItem(0x124, 3, lambda_1531)
    OP_11(0xFF, 0xFF, 0xFF, 0x50140, 0x68BC8, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(3000)
    OP_22(0x133, 0x0, 0x64)
    OP_6F(0x1, 0)
    OP_70(0x1, 0xE6)
    Sleep(2000)

    def lambda_1578():
        OP_8F(0xFE, 0x474, 0x96, 0xFFFFAE20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1578)
    WaitChrThread(0x12, 0x0)
    OP_73(0x1)
    WaitChrThread(0x124, 0x0)
    Sleep(1000)
    OP_43(0x12, 0x0, 0x0, 0x8)
    Sleep(2000)
    Fade(1000)
    OP_6D(8720, 0, -33830, 0)
    OP_67(0, 3940, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(113000, 0)
    OP_6E(418, 0)
    OP_11(0xFF, 0xFF, 0xFF, 0x64578, 0x68BC8, 0x0)
    OP_72(0x404, 0x0)
    ExitThread()
    SetChrFlags(0x10, 0x1)
    OP_0D()
    WaitChrThread(0x12, 0x0)
    Sleep(500)

    ChrTalk(    #33
        0x12,
        (
            "#120F#5P呼……\x01",
            "怎么看都是一副凶恶的样子。\x02\x03",

            "不过，我们要前往的场所\x01",
            "是阴森的古代牢狱……\x02\x03",

            "作为先锋的座机\x01",
            "这样子再合适不过了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_169F():
        OP_6D(6410, 2500, -33810, 2000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_169F)

    def lambda_16B7():
        OP_67(0, 4110, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_16B7)

    def lambda_16CF():
        OP_6B(2940, 2000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_16CF)

    def lambda_16DF():
        OP_6C(135000, 2000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_16DF)
    Sleep(500)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x20)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x12, 0x1)
    SetChrChipByIndex(0x12, 0)
    SetChrSubChip(0x12, 1)
    Sleep(500)
    SetChrSubChip(0x12, 2)
    OP_7D(0x0, 0x12, 0x32, 0x1F4)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_172E():
        OP_96(0xFE, 0x12C0, 0x12C0, 0xFFFF810C, 0x157C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_172E)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 180, 0)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0x12, 0x4)
    SetChrSubChip(0x12, 1)
    OP_CF(0x12, 0x4, "Frame143_on_head")
    OP_7D(0x1, 0x12, 0x0, 0x0)
    Sleep(500)
    SetChrChipByIndex(0x12, 1)
    SetChrSubChip(0x12, 0)
    Sleep(500)
    OP_8C(0x12, 0, 400)
    Sleep(1000)
    Fade(300)
    SetChrChipByIndex(0x12, 0)
    SetChrSubChip(0x12, 1)
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Sleep(1000)
    LoadEffect(0x0, "monster\\ms30803a.eff")
    LoadEffect(0x1, "monster\\ms30803b.eff")
    LoadEffect(0x2, "map\\mp021_00.eff")
    OP_22(0xF3, 0x0, 0x64)
    Fade(300)
    PlayEffect(0x0, 0x0, 0x10, 0, 3300, 900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    Fade(300)
    OP_82(0x0, 0x2)
    OP_0D()
    Sleep(500)
    OP_D8(0x4, 0x1F4)
    OP_43(0x10, 0x3, 0x0, 0x7)
    OP_71(0x2004, 0x0)
    ExitThread()
    OP_B0(0x4, 0xF)
    OP_6F(0x4, 845)
    OP_70(0x4, 0x361)

    def lambda_187B():
        OP_8F(0xFE, 0x3B6, 0x0, 0xFFFF840E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_187B)
    Sleep(1000)
    Fade(1000)
    OP_11(0xFF, 0xFF, 0xFF, 0x64578, 0xC3500, 0x0)
    OP_6D(780, -2700, -25780, 0)
    OP_67(0, 4170, -10000, 0)
    OP_6B(3850, 0)
    OP_6C(0, 0)
    OP_6E(510, 0)

    def lambda_18ED():
        OP_6D(780, -4000, -27780, 7500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_18ED)

    def lambda_1905():
        OP_67(0, 4000, -10000, 7500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1905)

    def lambda_191D():
        OP_6B(4500, 7500)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_191D)
    Sleep(1000)

    def lambda_1932():
        OP_8C(0xFE, 180, 60)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1932)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x10, 0x1)
    OP_72(0x2004, 0x0)
    ExitThread()
    OP_73(0x4)
    OP_D8(0x4, 0x1F4)
    OP_71(0x2004, 0x0)
    ExitThread()
    OP_6F(0x4, 0)
    OP_70(0x4, 0x14)
    Sleep(500)
    OP_44(0x10, 0x3)
    OP_23(0xEC)
    Sleep(500)
    OP_72(0x2004, 0x0)
    ExitThread()
    OP_73(0x4)
    OP_B0(0x4, 0xF)
    OP_6F(0x4, 140)
    OP_70(0x4, 0x95)
    OP_73(0x4)
    OP_44(0x12, 0x1)
    OP_44(0x12, 0x2)
    OP_44(0x12, 0x3)
    Fade(500)
    OP_6D(-3500, 500, -60560, 0)
    OP_67(0, 4520, -10000, 0)
    OP_6B(2570, 0)
    OP_6C(272000, 0)
    OP_6E(544, 0)
    OP_11(0xFF, 0xFF, 0xFF, 0x61A80, 0x829D8, 0x0)

    def lambda_19F8():

        label("loc_19F8")

        OP_7C(0x32, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_19F8")

    QueueWorkItem2(0x12, 3, lambda_19F8)
    OP_22(0x85, 0x1, 0x50)

    def lambda_1A18():
        OP_6D(-3500, 500, -30000, 2000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1A18)
    Play3DEffect(0x1, 0x1, 0x4, "Frame80_Bone__79_", 0x190, 0x0, 0x708, 0xFFF1, 0x10E, 0xB4, 0x7D0, 0x7D0, 0x4B0, 0x0)
    Play3DEffect(0x1, 0x2, 0x4, "Frame83_Bone__82_", 0xFFFFFE70, 0x0, 0x708, 0xFFE7, 0x10E, 0xB4, 0x7D0, 0x7D0, 0x4B0, 0x0)
    OP_22(0x113, 0x1, 0x64)
    PlayEffect(0x2, 0x3, 0x10, 0, 0, 3000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xCC, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x114, 0x0, 0x64)
    OP_0D()
    WaitChrThread(0x12, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(-2000, 0, -39590, 0)
    OP_67(0, 4830, -10000, 0)
    OP_6B(2770, 0)
    OP_6C(212000, 0)
    OP_6E(599, 0)
    OP_0D()

    def lambda_1B37():

        label("loc_1B37")

        OP_7C(0x1E, 0x1E, 0xBB8, 0x64)
        OP_48()
        Jump("loc_1B37")

    QueueWorkItem2(0x12, 3, lambda_1B37)

    ChrTalk(    #34
        0x12,
        (
            "#120F#5P去吧，漆黑之翼！\x02\x03",

            "为了让愚蠢的人们\x01",
            "知道这世界的真相!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B94():

        label("loc_1B94")

        OP_7C(0x50, 0x50, 0xBB8, 0x64)
        OP_48()
        Jump("loc_1B94")

    QueueWorkItem2(0x12, 3, lambda_1B94)
    Sleep(1000)
    OP_82(0x3, 0x2)
    OP_23(0xCC)
    OP_B0(0x4, 0x14)
    OP_6F(0x4, 150)
    OP_70(0x4, 0xC8)
    Sleep(500)
    Play3DEffect(0x1, 0x1, 0x4, "Frame80_Bone__79_", 0x190, 0x0, 0x708, 0xFFF1, 0x10E, 0xB4, 0xFA0, 0xFA0, 0xDAC, 0x0)
    Play3DEffect(0x1, 0x2, 0x4, "Frame83_Bone__82_", 0xFFFFFE70, 0x0, 0x708, 0xFFE7, 0x10E, 0xB4, 0xFA0, 0xFA0, 0xDAC, 0x0)
    Sleep(200)

    def lambda_1C46():
        OP_91(0xFE, 0x0, 0x1388, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_1C46)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    Sleep(200)
    Fade(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_6D(730, 0, -62900, 0)
    OP_67(0, 7680, -10000, 0)
    OP_6B(10860, 0)
    OP_6C(56000, 0)
    OP_6E(560, 0)
    OP_71(0x404, 0x0)
    ExitThread()
    SetChrPos(0x11, 0, 5000, -60000, 0)
    OP_A1(0x11, 0x3)
    OP_72(0x403, 0x0)
    ExitThread()
    OP_8C(0x11, 180, 0)
    OP_D1(17, -45000, 150000, 15000, 0)
    OP_CF(0x12, 0x3, "Frame134_on_head")
    OP_71(0x2003, 0x0)
    ExitThread()
    OP_B0(0x3, 0x1E)
    OP_6F(0x3, 320)
    OP_70(0x3, 0x154)

    def lambda_1D25():

        label("loc_1D25")

        OP_7C(0x32, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_1D25")

    QueueWorkItem2(0x12, 3, lambda_1D25)

    def lambda_1D40():
        OP_6B(16460, 8000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1D40)
    OP_43(0x12, 0x1, 0x0, 0x5)
    OP_43(0x11, 0x3, 0x0, 0x6)
    OP_98(0x0, 0x11)
    OP_98(0x1, 0xFFFFB1E0, 0x7530, 0xFFFEA840)
    OP_98(0x1, 0xFFFF15A0, 0xC350, 0xFFFEEE90)
    OP_98(0x1, 0xFFFE2B40, 0x1ADB0, 0xFFFD8F00)

    def lambda_1D8C():
        OP_98(0x2, 0xFE, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1D8C)
    Sleep(6500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    Sleep(2000)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E2E")
    Sleep(1000)
    OP_28(0x10, 0x4, 0x10)
    OP_28(0x10, 0x4, 0x20)
    OP_3E(0x2EA, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #35
        "\x07\x00得到了\x1F\xEA\x02\x07\x00。\x02",
    )

    Jump("loc_1DF9")

    label("loc_1DF9")

    CloseMessageWindow()
    AddMira(4000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #36
        "\x07\x00得到了\x07\x02４０００米拉\x07\x00。\x02",
    )

    Jump("loc_1E22")

    label("loc_1E22")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_1E2E")

    OP_A2(0x2504)
    NewScene("ED6_DT21/M5402   ._SN", 128, 0, 0)
    IdleLoop()
    Return()

    # Function_4_141B end

    def Function_5_1E3B(): pass

    label("Function_5_1E3B")

    OP_24(0x113, 0x32)
    OP_24(0x114, 0x32)
    Sleep(500)
    OP_24(0x113, 0x3C)
    OP_24(0x114, 0x3C)
    Sleep(500)
    OP_24(0x113, 0x46)
    OP_24(0x114, 0x46)
    Sleep(500)
    OP_24(0x113, 0x50)
    OP_24(0x114, 0x5A)
    Sleep(500)

    def lambda_1E75():

        label("loc_1E75")

        OP_7C(0x64, 0x64, 0xBB8, 0x64)
        OP_48()
        Jump("loc_1E75")

    QueueWorkItem2(0x12, 3, lambda_1E75)
    OP_24(0x113, 0x64)
    OP_24(0x114, 0x64)
    Sleep(3500)
    OP_24(0x113, 0x5A)
    OP_24(0x114, 0x5A)
    Sleep(500)
    OP_24(0x113, 0x4B)
    OP_24(0x114, 0x4B)
    Sleep(400)
    OP_24(0x113, 0x32)
    OP_24(0x114, 0x32)
    Sleep(300)
    OP_24(0x113, 0x19)
    OP_24(0x114, 0x19)
    Sleep(200)
    OP_24(0x113, 0x0)
    OP_24(0x114, 0x0)
    Sleep(100)
    OP_23(0x113)
    OP_23(0x114)
    OP_23(0x85)
    OP_44(0x12, 0x3)
    Return()

    # Function_5_1E3B end

    def Function_6_1EE6(): pass

    label("Function_6_1EE6")

    OP_D1(254, -150000, 150000, 30000, 800)
    OP_D1(254, -150000, 130000, 220000, 800)
    OP_D1(254, -10000, 170000, 310000, 500)
    OP_D1(254, -20000, 180000, 345000, 1500)
    Return()

    # Function_6_1EE6 end

    def Function_7_1F33(): pass

    label("Function_7_1F33")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F4C")
    OP_22(0xEC, 0x0, 0x64)
    Sleep(700)
    OP_23(0xEC)
    Jump("Function_7_1F33")

    label("loc_1F4C")

    Return()

    # Function_7_1F33 end

    def Function_8_1F4D(): pass

    label("Function_8_1F4D")

    OP_8F(0xFE, 0x19A, 0x0, 0xFFFF897C, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_8_1F4D end

    def Function_9_1F69(): pass

    label("Function_9_1F69")

    OP_8F(0xFE, 0x11C6, 0xC350, 0xFFFF7A86, 0x1388, 0x0)
    Return()

    # Function_9_1F69 end

    SaveToFile()

Try(main)
