from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'E0000   ._SN',
        MapName             = 'event',
        Location            = 'E0000.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60001",
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
        '森特',                                 # 9
        '乘客',                                 # 10
        '乘客',                                 # 11
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 4000,
        Unknown_08              = -4500,
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
        'ED6_DT07/CH01660 ._CH',             # 00
        'ED6_DT07/CH01020 ._CH',             # 01
        'ED6_DT07/CH01160 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01660P._CP',             # 00
        'ED6_DT07/CH01020P._CP',             # 01
        'ED6_DT07/CH01160P._CP',             # 02
    )

    DeclNpc(
        X                   = -2840,
        Z                   = 5000,
        Y                   = 10090,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -1600,
        Z                   = 5000,
        Y                   = -4820,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -3510,
        Z                   = 5000,
        Y                   = -4010,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )


    ScpFunction(
        "Function_0_122",          # 00, 0
        "Function_1_134",          # 01, 1
        "Function_2_13F",          # 02, 2
        "Function_3_2BC",          # 03, 3
        "Function_4_459",          # 04, 4
        "Function_5_4F0",          # 05, 5
        "Function_6_57C",          # 06, 6
        "Function_7_181A",         # 07, 7
    )


    def Function_0_122(): pass

    label("Function_0_122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_133")
    SetMapFlags(0x10000000)
    Event(0, 6)

    label("loc_133")

    Return()

    # Function_0_122 end

    def Function_1_134(): pass

    label("Function_1_134")

    OP_22(0x79, 0x1, 0x46)
    OP_22(0x1C3, 0x0, 0x64)
    Return()

    # Function_1_134 end

    def Function_2_13F(): pass

    label("Function_2_13F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_164")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_2A6")

    label("loc_164")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17D")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_2A6")

    label("loc_17D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_196")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_2A6")

    label("loc_196")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AF")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_2A6")

    label("loc_1AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C8")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_2A6")

    label("loc_1C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E1")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_2A6")

    label("loc_1E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FA")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_2A6")

    label("loc_1FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_213")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_2A6")

    label("loc_213")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22C")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_2A6")

    label("loc_22C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_245")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_2A6")

    label("loc_245")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25E")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_2A6")

    label("loc_25E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_277")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_2A6")

    label("loc_277")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_290")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_2A6")

    label("loc_290")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A6")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_2A6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2BB")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_2A6")

    label("loc_2BB")

    Return()

    # Function_2_13F end

    def Function_3_2BC(): pass

    label("Function_3_2BC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 3)), scpexpr(EXPR_END)), "loc_364")

    ChrTalk(    #0
        0xFE,
        (
            "我现在要去调查\x01",
            "位于卢安的『绀碧之塔』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "其实诞辰庆典的时候，\x01",
            "就有人在『四轮之塔』目睹到了奇怪的现象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "但事后隔了很久，\x01",
            "才有人对其展开调查。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_455")

    label("loc_364")

    OP_A2(0x120B)

    ChrTalk(    #3
        0xFE,
        "呼，真遗憾啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "今天的云好像很多，\x01",
            "看不见『绀碧之塔』呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "我是历史资料馆的研究员。\x01",
            "正准备去绀碧之塔做实地调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "其实诞辰庆典的时候，\x01",
            "就有人在『四轮之塔』目睹到了奇怪的现象……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "但事后隔了很久，\x01",
            "才有人对其展开调查。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_455")

    TalkEnd(0xFE)
    Return()

    # Function_3_2BC end

    def Function_4_459(): pass

    label("Function_4_459")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4B5")

    ChrTalk(    #8
        0xFE,
        "唉，小孩子就是天不怕地不怕。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "我光是站在这个地方，\x01",
            "双腿就开始发软了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EC")

    label("loc_4B5")

    OP_A2(0x0)

    ChrTalk(    #10
        0xFE,
        (
            "喂，喂喂。\x01",
            "别去那边。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "掉下去怎么办。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)

    label("loc_4EC")

    TalkEnd(0xFE)
    Return()

    # Function_4_459 end

    def Function_5_4F0(): pass

    label("Function_5_4F0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_540")

    ChrTalk(    #12
        0xFE,
        "喂，爸爸也来这边嘛！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "那些山啊河啊，\x01",
            "全部都看起来好小哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_578")

    label("loc_540")

    OP_A2(0x1)

    ChrTalk(    #14
        0xFE,
        "哇，真厉害。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "嘿，看啊！\x01",
            "树木变得那么小了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_578")

    TalkEnd(0xFE)
    Return()

    # Function_5_4F0 end

    def Function_6_57C(): pass

    label("Function_6_57C")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58F")
    Call(0, 7)

    label("loc_58F")

    StopSound(0x1ADB0, 0x249F0, 0x0)
    OP_6D(600, 5000, 44810, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(7230, 0)
    OP_6C(143000, 0)
    OP_6E(332, 0)
    SetChrPos(0x101, 3260, 5000, -4580, 85)
    SetChrPos(0xF7, 3270, 5000, -3730, 101)
    StopSound(0x9C40, 0x1ADB0, 0x32C8)
    OP_C8(0x80, 0x46, "C_PLAC29._CH", 0x0, 0x7D0)
    FadeToBright(2000, 0)

    def lambda_62C():
        OP_6D(4040, 5000, -3270, 11000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_62C)

    def lambda_644():
        OP_67(0, 10000, -10000, 11000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_644)

    def lambda_65C():
        OP_6B(3500, 11000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_65C)
    Sleep(4000)

    def lambda_671():
        OP_6C(53000, 7000)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_671)
    WaitChrThread(0x101, 0x1)
    Fade(1000)
    OP_6D(4040, 5000, -3270, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(2140, 0)
    OP_6C(53000, 0)
    OP_6E(332, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_EBA")

    ChrTalk(    #16
        0x101,
        (
            "#1011F嗯嗯，天气真好啊～\x02\x03",

            "照这么看来，\x01",
            "今天卢安地区应该很适合观光吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x106,
        (
            "#5P#051F或许吧。\x02\x03",

            "不过现在，因为观光之外的事情\x01",
            "这里变得十分热闹。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #18
        0x101,
        "#1004F观光之外的事情？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #19
        0x106,
        (
            "#5P#053F就是市长选举。\x02\x03",

            "为了取代先前被捕的戴尔蒙，\x01",
            "好像有两个候选人进行角逐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#1011F噢～是这样啊。\x02\x03",

            "#1015F不过，确实也该这么做呢。\x02\x03",

            "毕竟一个城市应该不可能\x01",
            "永远都没有市长来管理吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x106,
        (
            "#5P#051F说起来，\x01",
            "那起事件是由你们解决的吧。\x02\x03",

            "之后我问过嘉恩了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#1016F啊、啊哈哈……\x02\x03",

            "#1008F嗯，阿加特离开之后，\x01",
            "就剩下我和约修亚，还有科洛丝了。\x02\x03",

            "不过，幸好得到了记者他们的帮助，\x01",
            "亲卫队最后将市长逮捕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x106,
        (
            "#5P#051F哼。成功不是单靠一个人的，\x01",
            "你能明白这点也算是进步了不少。\x02\x03",

            "#551F话说回来，没想到那个\x01",
            "穿校服的女孩竟然是科洛蒂娅公主……\x02\x03",

            "在王城知道她真正身份的时候，\x01",
            "就连我也吓了一大跳啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#1016F啊哈哈，你这种心情我能理解。\x02\x03",

            "#1015F说到这个，自从诞辰庆典结束后\x01",
            "就没见过科洛丝和奥利维尔了。\x02\x03",

            "#1003F嗯嗯，提妲、博士，\x01",
            "还有金先生他们也是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x106,
        (
            "#5P#552F其实之前我向提妲和老爷子\x01",
            "提过你和约修亚的事情。\x02\x03",

            "可以看得出来，\x01",
            "他们两个非常担心你啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#1025F是这样啊……\x01",
            "谢谢你，阿加特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x106,
        (
            "#5P#053F总之，有机会的话，\x01",
            "还是写封信直接问候他们一下吧。\x02\x03",

            "#050F金那家伙，\x01",
            "诞辰庆典之后就回卡尔瓦德了。\x02\x03",

            "不过，他出发前也叫我代他向你们问好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#1025F是吗……\x01",
            "真想亲自向他打招呼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x106,
        (
            "#5P#051F话说回来，\x01",
            "公主似乎已经回到学院继续念书了。\x02\x03",

            "反正我们难得去一趟卢安。\x01",
            "有空的话就去学校打个招呼吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#1016F嗯，说得也是。\x02\x03",

            "#1008F呵呵……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x106,
        (
            "#5P#055F干、干嘛。\x01",
            "我说错话了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#1012F不，不是的。\x02\x03",

            "#1017F只是我没有想到\x01",
            "阿加特有时候也懂得体贴他人呢。\x02\x03",

            "像是在王都准备出发的时候\x01",
            "也叮嘱过我要做好准备之类的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #33
        0x106,
        (
            "#5P#552F别、别说些无聊的话。\x02\x03",

            "#050F真是的……\x01",
            "到达卢安之前我要在座位上睡觉。\x02\x03",

            "你就在飞船内闲逛好了，\x01",
            "但是别忘了到卢安之后要下船哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF7, 315, 400)

    def lambda_DAF():
        OP_6D(1540, 5000, -2430, 2000)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_DAF)

    def lambda_DC7():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_DC7)
    OP_8E(0x106, 0xFFFFFFE2, 0x13EC, 0xFFFFF9A2, 0x7D0, 0x0)
    OP_8C(0x106, 14, 400)
    Sleep(500)
    OP_72(0x0, 0x800)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3B)
    OP_22(0x6, 0x0, 0x64)
    OP_73(0x0)

    def lambda_E12():

        label("loc_E12")

        TurnDirection(0x101, 0x106, 0)
        OP_48()
        Jump("loc_E12")

    QueueWorkItem2(0x101, 0, lambda_E12)
    OP_8E(0x106, 0xFFFFFFE2, 0x13EC, 0x10E, 0x7D0, 0x0)
    OP_6F(0x0, 59)
    OP_70(0x0, 0x0)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x0)
    OP_71(0x0, 0x800)

    ChrTalk(    #34
        0x101,
        (
            "#1016F真是的……\x01",
            "说话还是这么不饶人。\x02\x03",

            "#1006F那么，在抵达之前还有空闲时间，\x01",
            "不如在船里逛逛吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0x0)
    RemoveParty(0x5, 0xFF)
    Jump("loc_180F")

    label("loc_EBA")


    ChrTalk(    #35
        0x101,
        (
            "#1011F嗯嗯，天气真好啊～\x02\x03",

            "照这么看来，\x01",
            "今天卢安地区应该很适合观光吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x103,
        (
            "#5P#021F呵呵，或许吧。\x02\x03",

            "#020F不过现在的卢安市\x01",
            "好像在为观光之外的事情而狂热。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #37
        0x101,
        "#1004F观光之外的事情？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #38
        0x103,
        (
            "#5P#020F就是市长选举哦。\x02\x03",

            "前任市长被逮捕已经有一段时间，\x01",
            "如今终于举行新市长的选举了。\x02\x03",

            "而且，据说两名旗鼓相当的候选人\x01",
            "已经展开了激烈的选举战。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#1011F噢～是这样啊。\x02\x03",

            "#1015F不过确实也该这么做呢。\x02\x03",

            "毕竟一个城市应该不可能\x01",
            "永远都没有市长来管理吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x103,
        (
            "#5P#023F哎呀，说到这个……\x02\x03",

            "我记得前任市长戴尔蒙被逮捕事件\x01",
            "好像和你们有关吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#1016F啊、啊哈哈……\x02\x03",

            "#1008F嗯，其实是在调查其它事件时，\x01",
            "偶然发现市长其实也有所牵连的缘故。\x02\x03",

            "不过，我们之所以能逮捕到市长，\x01",
            "全是因为科洛丝和亲卫队的帮忙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x103,
        (
            "#5P#021F呵呵，你还真谦虚呢。\x02\x03",

            "能看到自己的学生表现得如此出色，\x01",
            "作为教官的我也感到很自豪哦。\x02\x03",

            "#020F不过，是这样的啊。\x02\x03",

            "你们和科洛蒂娅公主\x01",
            "就是在那个时候认识的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#1000F嗯，没错。\x01",
            "是和约修亚一起帮忙准备学院祭的时候……\x02\x03",

            "#1015F说起来，自从诞辰庆典结束之后，\x01",
            "我们再也没和科洛丝他们见过面了……\x02\x03",

            "#1003F呼呼，提妲，博士，\x01",
            "还有金先生他们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x103,
        (
            "#5P#020F金先生在\x01",
            "诞辰庆典之后就回到卡尔瓦德了。\x02\x03",

            "好像是因为接到了来自\x01",
            "共和国协会的回国请求。\x02\x03",

            "他回国前拜托过我代他向你们问好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#1007F是吗……\x01",
            "他有工作在身，没办法了。\x02\x03",

            "#1025F毕竟金先生帮了我们这么多，\x01",
            "真想亲自跟他打声招呼呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x103,
        (
            "#5P#020F将来总会有机会的。\x02\x03",

            "而至于提妲和\x01",
            "拉赛尔博士……\x02\x03",

            "我和卡西乌斯老师已经向他们\x01",
            "简单说明了你和约修亚的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#1025F是这样啊……\x01",
            "谢谢你，雪拉姐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x103,
        (
            "#5P#021F呵呵，说起来，\x01",
            "提妲真是个善良体贴的孩子呢。\x02\x03",

            "#027F听了我们的话之后，\x01",
            "她的眼眶一下子变得泪汪汪的，\x01",
            "还强忍着泪水说……\x02\x03",

            "『姐姐她现在正在努力，\x01",
            "  所以我也不能够哭。』\x01",
            "她是这样说的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#1008F啊、啊哈哈……\x02\x03",

            "#1013F那个孩子真是的……\x02\x03",

            "#1027F真是的……\x01",
            "雪拉姐，别逗我哭啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x103,
        (
            "#5P#021F抱歉抱歉。\x02\x03",

            "#027F不过说真的，\x01",
            "你们两人遇到了很多知心的好朋友呢。\x02\x03",

            "所以，好好珍惜这份友情吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        (
            "#1012F嗯……我知道的。\x02\x03",

            "#1017F对了，雪拉姐。\x02\x03",

            "我们到了卢安地区之后，\x01",
            "可不可以一边工作一边去向\x01",
            "曾经帮助过我们的朋友问好呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x103,
        (
            "#5P#021F嗯，当然可以了。\x02\x03",

            "#020F那么……\x01",
            "距离抵达还有一段时间呢。\x02\x03",

            "我想在座位上小睡一会儿，\x01",
            "你打算做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1015F嗯，这样啊。\x02\x03",

            "#1011F我倒是想在定期船里面散散步，\x01",
            "那我就先走了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x103,
        (
            "#5P#020F嗯，我知道了。\x02\x03",

            "但是，千万别忘记\x01",
            "我们要在卢安下飞船哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF7, 315, 400)

    def lambda_176B():
        OP_6D(1540, 5000, -2430, 2000)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_176B)

    def lambda_1783():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_1783)

    def lambda_1793():

        label("loc_1793")

        TurnDirection(0x101, 0x103, 0)
        OP_48()
        Jump("loc_1793")

    QueueWorkItem2(0x101, 0, lambda_1793)
    OP_8E(0x103, 0xFFFFFFE2, 0x13EC, 0xFFFFF9A2, 0x7D0, 0x0)
    OP_8C(0x103, 14, 400)
    Sleep(500)
    OP_72(0x0, 0x800)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3B)
    OP_22(0x6, 0x0, 0x64)
    OP_73(0x0)
    OP_8E(0x103, 0xFFFFFFE2, 0x13EC, 0x10E, 0x7D0, 0x0)
    OP_6F(0x0, 59)
    OP_70(0x0, 0x0)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x0)
    OP_44(0x101, 0x0)
    OP_71(0x0, 0x800)
    RemoveParty(0x2, 0xFF)

    label("loc_180F")

    OP_A2(0x1205)
    Fade(1000)
    EventEnd(0x0)
    Return()

    # Function_6_57C end

    def Function_7_181A(): pass

    label("Function_7_181A")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
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
        (0, "loc_1897"),
        (1, "loc_189D"),
        (SWITCH_DEFAULT, "loc_18A3"),
    )


    label("loc_1897")

    OP_A2(0x1200)
    Jump("loc_18A3")

    label("loc_189D")

    OP_A2(0x1201)
    Jump("loc_18A3")

    label("loc_18A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_18B1")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_18B5")

    label("loc_18B1")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_18B5")

    Return()

    # Function_7_181A end

    SaveToFile()

Try(main)
