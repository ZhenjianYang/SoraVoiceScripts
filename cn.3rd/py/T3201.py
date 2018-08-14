from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3201   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3201.x',
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
        '金',                                   # 9
        '雾香',                                 # 10
        '目标用摄像机',                         # 11
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
        'ED6_DT07/CH00070 ._CH',             # 00
        'ED6_DT07/CH02610 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH00070P._CP',             # 00
        'ED6_DT07/CH02610P._CP',             # 01
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_11A",          # 00, 0
        "Function_1_13A",          # 01, 1
        "Function_2_13B",          # 02, 2
        "Function_3_960",          # 03, 3
        "Function_4_97C",          # 04, 4
    )


    def Function_0_11A(): pass

    label("Function_0_11A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_139")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_139")
    OP_A3(0x2507)
    SetMapFlags(0x10000000)
    Event(0, 4)

    label("loc_139")

    Return()

    # Function_0_11A end

    def Function_1_13A(): pass

    label("Function_1_13A")

    Return()

    # Function_1_13A end

    def Function_2_13B(): pass

    label("Function_2_13B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 50900, 2500, -2400, 0)
    OP_6D(50730, 2500, 2180, 0)
    OP_67(0, 7220, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(141000, 0)
    OP_6E(411, 0)

    def lambda_1B4():
        OP_6E(324, 5000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_1B4)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x0, 0x0)
    Fade(1000)
    OP_6D(51440, 2500, -3490, 0)
    OP_67(0, 5710, -10000, 0)
    OP_6B(2570, 0)
    OP_6C(141000, 0)
    OP_6E(298, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #0
        0x11,
        "#790F#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_72(0x806, 0x0)
    ExitThread()
    OP_72(0x1006, 0x0)
    ExitThread()
    OP_6F(0x6, 0)
    OP_70(0x6, 0x1D)
    OP_73(0x6)
    Sleep(200)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 60800, 2500, -3050, 270)

    def lambda_27C():
        OP_8E(0xFE, 0xD638, 0x9C4, 0xFFFFF4DE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_27C)

    def lambda_297():
        OP_6D(54110, 2500, -4810, 3000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_297)

    def lambda_2AF():
        OP_67(0, 4019, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2AF)

    def lambda_2C7():
        OP_6B(2710, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2C7)

    def lambda_2D7():
        OP_6E(313, 3000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_2D7)
    Sleep(1000)
    OP_6F(0x6, 29)
    OP_70(0x6, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x11, 90, 400)
    Sleep(200)

    ChrTalk(    #1
        0x11,
        "#790F#4P好快啊，这就出来了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        (
            "#070F#5P喂喂，快什么啊……\x02\x03",

            "我都已经泡了\x01",
            "一个小时了啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x11,
        "#790F#4P是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        (
            "#070F#5P怎么了，\x01",
            "难得看到你在深思啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_3C7():
        OP_6D(53380, 2500, -5270, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_3C7)

    def lambda_3DF():
        OP_67(0, 4490, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3DF)

    def lambda_3F7():
        OP_6B(2760, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_3F7)

    def lambda_407():
        OP_6E(325, 2000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_407)
    OP_43(0x10, 0x0, 0x0, 0x3)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x0, 0x0)
    OP_8C(0x11, 0, 400)

    ChrTalk(    #5
        0x11,
        (
            "#790F嗯嗯……\x02\x03",

            "……就差一步了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        "#070F#5P是吗……\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_8C(0x10, 0, 400)
    Sleep(1500)

    ChrTalk(    #7
        0x10,
        (
            "#070F#5P师父去世后，都过了六年了吗。\x02\x03",

            "你似乎经过了漫长的旅途啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x11,
        (
            "#790F是走过不少地方了呢……\x02\x03",

            "不过，\x01",
            "并不是旅行这么轻松的事情。\x02\x03",

            "只不过是在大陆上随波逐流，\x01",
            "偶尔停留在某个角落……\x02\x03",

            "就像河流中的落叶一样。\x02",
        )
    )

    Jump("loc_564")

    label("loc_564")

    CloseMessageWindow()

    ChrTalk(    #9
        0x10,
        (
            "#070F#5P原来如此啊……\x02\x03",

            "不过，要是这样的话，\x01",
            "你也差不多该和其他人一样……\x02\x03",

            "开始寻找\x01",
            "自己的道路怎么样？\x02",
        )
    )

    Jump("loc_5E2")

    label("loc_5E2")

    CloseMessageWindow()
    OP_8C(0x11, 90, 400)

    ChrTalk(    #10
        0x11,
        (
            "#790F#4P哎呀……\x02\x03",

            "难不成\x01",
            "你是打算对我说教吗？\x02",
        )
    )

    Jump("loc_629")

    label("loc_629")

    CloseMessageWindow()
    OP_8C(0x10, 315, 400)

    ChrTalk(    #11
        0x10,
        (
            "#070F#5P啧……\x01",
            "抱歉我嘴这么笨。\x02\x03",

            "总、总而言之\x01",
            "我想说的就是啊……\x02\x03",

            "我们已经花费了\x01",
            "足够的时间。\x02\x03",

            "要治愈过去的伤痛，\x01",
            "这段时间已经足够了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x11,
        (
            "#790F#4P嗯嗯……是啊。\x02\x03",

            "或许是这样……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_8C(0x11, 0, 400)
    Sleep(2000)

    ChrTalk(    #13
        0x11,
        "#790F我说，金。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        "#070F#5P嗯？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x11,
        "#790F我要是回国你会高兴吗？\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #16
        0x10,
        "#070F#5P怎、怎么了，突然这么问。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 90, 400)
    Sleep(300)

    ChrTalk(    #17
        0x11,
        "#790F#4P别管了，你回答我就是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10,
        (
            "#070F#5P嗯，唔……那当然。\x02\x03",

            "一定要说的话，\x01",
            "当然是高兴的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x11,
        "#790F#4P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10,
        "#070F#5P那、那又怎么样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x11,
        (
            "#790F#4P不……\x02\x03",

            "总统的邀请，\x01",
            "我决定接受了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #22
        0x10,
        (
            "#070F#5P喂、喂！？\x02\x03",

            "也别因为我就……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x11,
        (
            "#790F#4P不要误会。\x02\x03",

            "我只是需要一个\x01",
            "终结旅程的契机而已。\x02\x03",

            "还有一个更能发挥\x01",
            "自己能力的地方……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    Sleep(2000)
    OP_A2(0x2508)
    NewScene("ED6_DT21/T3200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_13B end

    def Function_3_960(): pass

    label("Function_3_960")

    OP_8E(0xFE, 0xCABC, 0x9C4, 0xFFFFF448, 0x5DC, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_3_960 end

    def Function_4_97C(): pass

    label("Function_4_97C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_22(0x1CF, 0x0, 0x64)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 50900, 2500, -2400, 0)
    OP_6D(48910, 380, 2620, 0)
    OP_67(0, 5410, -10000, 0)
    OP_6B(1660, 0)
    OP_6C(143000, 0)
    OP_6E(731, 0)
    StopSound(0xC8, 0x1D4C0, 0x0)

    def lambda_A07():
        OP_6D(53710, 380, -6310, 6000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_A07)

    def lambda_A1F():
        OP_67(0, 5410, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_A1F)

    def lambda_A37():
        OP_6B(1400, 6000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_A37)

    def lambda_A47():
        OP_6C(143000, 6000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_A47)

    def lambda_A57():
        OP_6E(731, 6000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_A57)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x12, 0x0)
    Sleep(1000)

    ChrTalk(    #24
        0x11,
        "#793F#11P………………………………\x02",
    )

    CloseMessageWindow()
    OP_72(0x806, 0x0)
    ExitThread()
    OP_72(0x1006, 0x0)
    ExitThread()
    OP_6F(0x6, 0)
    OP_70(0x6, 0x1D)
    OP_73(0x6)
    Sleep(300)
    ClearChrFlags(0x10, 0x80)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, 60800, 2500, -3050, 270)

    def lambda_AEC():
        OP_8E(0xFE, 0xD638, 0x9C4, 0xFFFFF4DE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_AEC)

    def lambda_B07():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_B07)

    def lambda_B19():
        OP_6D(54110, 2500, -4810, 3000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_B19)

    def lambda_B31():
        OP_67(0, 4019, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_B31)

    def lambda_B49():
        OP_6B(1430, 3000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_B49)

    def lambda_B59():
        OP_6E(720, 3000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_B59)
    Sleep(1000)
    OP_72(0x6, 0x8)
    ExitThread()
    OP_6F(0x6, 29)
    OP_70(0x6, 0x0)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x11, 90, 400)
    Sleep(300)

    ChrTalk(    #25
        0x11,
        "#791F#12P好快啊，这就出来了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        (
            "#073F#5P喂喂……这还叫快？\x02\x03",

            "#070F我都已经泡了\x01",
            "一个小时了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x11,
        "#792F#12P是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10,
        (
            "#070F#5P怎么了，\x01",
            "难得看到你在深思啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C67():
        OP_6D(52580, 2500, -4620, 3000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_C67)

    def lambda_C7F():
        OP_67(0, 3840, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_C7F)

    def lambda_C97():
        OP_6B(1260, 3000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_C97)

    def lambda_CA7():
        OP_6E(731, 3000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_CA7)
    OP_43(0x10, 0x0, 0x0, 0x3)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x12, 0x0)
    OP_8C(0x11, 0, 400)
    Sleep(500)

    ChrTalk(    #29
        0x11,
        (
            "#792F#6P嗯嗯……\x02\x03",

            "#793F……就差一步了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10,
        "#074F#5P是吗……\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_8C(0x10, 0, 300)
    OP_21()
    OP_1D(0xB7)
    Sleep(500)

    ChrTalk(    #31
        0x10,
        (
            "#074F#5P自龙牙师父去世后，\x01",
            "已经过了六年了吗……\x02\x03",

            "#070F你似乎经过了漫长的旅途啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x11,
        (
            "#791F嗯嗯，是走过不少地方呢……\x02\x03",

            "#792F不过，\x01",
            "并不是旅行这么轻松的事情。\x02\x03",

            "只不过是在大陆上随波逐流，\x01",
            "偶尔停留在某个角落……\x02\x03",

            "#793F就像河流中的落叶一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10,
        (
            "#074F#5P…………………………\x02\x03",

            "#070F……那么，\x01",
            "看来你找到之前所说的答案了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x11,
        (
            "#792F呵呵，\x01",
            "答案这种东西现在还没找到呢。\x02\x03",

            "#794F一定要说的话，就是……\x02\x03",

            "可能是找到\x01",
            "所谓的『结论』了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10,
        "#072F#5P结论……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x11,
        (
            "#791F我说，金……\x02\x03",

            "我不直接参加战斗而去当接待员，\x01",
            "你对此有什么看法？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10,
        (
            "#073F#5P这个啊……\x02\x03",

            "#573F……不想走上和\x01",
            "我或瓦鲁特一样傻的道路。\x02\x03",

            "#070F大概，就是这个原因吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x11,
        (
            "#794F呵呵……\x02\x03",

            "#792F关于你们是傻瓜这一点，\x01",
            "我倒是不否定。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2300, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #39
        0x10,
        (
            "#075F#5P喂！\x01",
            "这点姑且给我否定吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x11,
        (
            "#793F………………………………\x02\x03",

            "#792F我啊，是想确定一下。\x01",
            "父亲所说的『活人拳』的意义。\x02\x03",

            "通过战斗彼此提高，\x01",
            "这种理念的意义。\x02\x03",

            "#793F的确……这种理念\x01",
            "或许接近理想状态。\x02\x03",

            "#790F……但是，\x01",
            "以战斗为前提我却不敢苟同。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10,
        "#072F#5P嗯………\x02",
    )

    CloseMessageWindow()

    def lambda_11D6():
        OP_6B(1210, 30000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_11D6)
    Sleep(500)

    ChrTalk(    #42
        0x11,
        (
            "#792F我知道作为一名武者\x01",
            "其人生完整的意义。\x02\x03",

            "也理解在此基础上\x01",
            "即使死也在所不惜的心情。\x02\x03",

            "关于这种想法，\x01",
            "我至今也没有改变。\x02\x03",

            "#793F但是……在父亲去世、\x01",
            "瓦鲁特离开时，\x01",
            "我无意中想到。\x02\x03",

            "#794F不通过战斗而救人……\x01",
            "如果有这样的道路，\x01",
            "不是更好吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10,
        "#073F#5P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x11,
        (
            "#793F我寻求着答案，\x01",
            "在大陆各地彷徨。\x02\x03",

            "然后，\x01",
            "在旅途中多次目睹纷争暴力，\x01",
            "深感自己的无力。\x02\x03",

            "#792F……这时闯入我生活的是在\x01",
            "利贝尔看到的游击士协会。\x02\x03",

            "任何时候都以民众安全\x01",
            "为第一要务而行动的组织理念……\x02\x03",

            "在这种理念下工作\x01",
            "我或许能够找到答案。\x02\x03",

            "#794F但是……结果却还是\x01",
            "无法逃离战斗。\x02",
        )
    )

    Jump("loc_1471")

    label("loc_1471")

    CloseMessageWindow()

    ChrTalk(    #45
        0x10,
        (
            "#572F#5P#572F……………………………\x02\x03",

            "#074F『人既生为人，\x01",
            "  何时何地都会伴随斗争。』\x02\x03",

            "『那么，要如何才能通过\x01",
            "　战斗来消灭纷争呢。』\x02\x03",

            "『看清了「现实」的我产生了\x01",
            "  这样一个「理想」。』\x02\x03",

            "#072F……这是师父说过的话吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x11,
        (
            "#791F嗯嗯……\x02\x03",

            "#793F从这个意义上来说……\x02\x03",

            "#792F……我只不过是将视线\x01",
            "从现实上逃避开了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10,
        "#075F#5P喂喂……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 315, 400)
    Sleep(300)

    ChrTalk(    #48
        0x10,
        (
            "#072F#5P话虽如此，\x01",
            "你自己也知道\x01",
            "并不是这么回事吧。\x02\x03",

            "师父所说的『现实』，\x01",
            "并不完全是\x01",
            "仅仅指战斗啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x11,
        (
            "#792F……不，\x01",
            "这是两个问题。\x02\x03",

            "#793F这几年来……\x01",
            "我完全没有\x01",
            "用自己的脚去走路。\x02\x03",

            "新的救人之道……\x01",
            "我以寻找这种道路为借口，\x01",
            "实际上是放弃了它。\x02\x03",

            "#794F……在协会舒适的气氛中\x01",
            "变得娇气了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x10,
        "#572F#5P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x11,
        (
            "#794F从这个意义上来说……\x01",
            "我大概是父亲的弟子中\x01",
            "最落后的一个吧。\x02\x03",

            "#792F且不论方式的对错……\x02\x03",

            "无论是你还是瓦鲁特\x01",
            "都选择了自己的道路，并不断前行。\x02\x03",

            "直面父亲所教导的活人拳，\x01",
            "找到了自己的答案。\x02\x03",

            "并且，\x01",
            "都以自己的方式\x01",
            "面对世界这个『现实』……\x02\x03",

            "#793F结果……\x01",
            "只有我停滞不前。\x02",
        )
    )

    Jump("loc_18C5")

    label("loc_18C5")

    CloseMessageWindow()

    ChrTalk(    #52
        0x10,
        "#074F#5P……………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #53
        0x10,
        (
            "#573F#5P#070F不……#1140W \x01",
            "#20W你确实前进了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x11, 90, 500)

    ChrTalk(    #54
        0x11,
        "#790F咦？\x02",
    )

    Jump("loc_1988")

    label("loc_1988")

    CloseMessageWindow()

    ChrTalk(    #55
        0x10,
        (
            "#573F#5P只不过……\x01",
            "那是为他人而开拓的道路。\x02\x03",

            "你在协会里\x01",
            "为了踏平别人前进的道路\x01",
            "而努力的前进着。\x02\x03",

            "#070F而这个……\x01",
            "我想正是救人之道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x11,
        (
            "#790F………………………………\x02\x03",

            "#792F呵呵……\x02\x03",

            "#794F难不成\x01",
            "这是在安慰我？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10,
        (
            "#072F#5P呜……抱歉我嘴这么笨。\x02\x03",

            "#074F总、总而言之\x01",
            "我想说的就是啊……\x02\x03",

            "#072F你实在是太要强，\x01",
            "而且太认真了。\x02\x03",

            "而这种要强和认真\x01",
            "在我看来却束缚了你自己。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x11,
        "#793F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x10,
        (
            "#573F#5P所以……雾香。\x01",
            "稍微放松点吧。\x02\x03",

            "一点点……只要一点点就好。\x02\x03",

            "#070F这样的话，\x01",
            "你应该能看透很多事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x11,
        "#792F#6P………………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 0, 300)
    Sleep(500)
    OP_62(0x11, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #61
        0x11,
        "#792F………我说，金。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x10,
        "#070F#5P嗯，怎么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x11,
        "#791F我要是回国，你会高兴吗？\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #64
        0x10,
        "#073F#5P怎、怎么了，突然这么问。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 90, 400)

    ChrTalk(    #65
        0x11,
        "#790F#6P别管了，你回答我就是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x10,
        (
            "#073F#5P嗯，唔……那当然。\x02\x03",

            "#074F一定要说的话，\x01",
            "当然是高兴的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x11,
        "#792F#6P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x10,
        "#072F#5P那、那又怎么样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x11,
        (
            "#792F#6P没什么……\x02\x03",

            "#791F总统的邀请，\x01",
            "我决定接受了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #70
        0x10,
        (
            "#073F#5P喂、喂！？\x02\x03",

            "这到底是什么意思……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x11,
        (
            "#792F#6P不要误会。\x02\x03",

            "我只是需要一个\x01",
            "终结旅程的契机而已。\x02\x03",

            "#791F还有一个更能发挥\x01",
            "自己能力的地方……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1EDC():
        OP_6B(1180, 3000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1EDC)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xFA0)
    OP_24(0x1CF, 0x5A)
    Sleep(400)
    OP_24(0x1CF, 0x50)
    Sleep(400)
    OP_24(0x1CF, 0x46)
    Sleep(400)
    OP_24(0x1CF, 0x3C)
    Sleep(400)
    OP_24(0x1CF, 0x32)
    Sleep(400)
    OP_24(0x1CF, 0x28)
    Sleep(400)
    OP_24(0x1CF, 0x1E)
    Sleep(400)
    OP_24(0x1CF, 0x14)
    Sleep(400)
    OP_24(0x1CF, 0xA)
    Sleep(400)
    OP_23(0x1CF)
    OP_21()
    OP_A2(0x2508)
    NewScene("ED6_DT21/T3200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_97C end

    SaveToFile()

Try(main)
