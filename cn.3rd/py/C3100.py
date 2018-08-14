from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3100   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
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
        '士兵塞缪尔',                           # 9
        '王国军军官',                           # 10
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
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01310 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01310P._CP',             # 01
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = -3230,
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


    ScpFunction(
        "Function_0_FA",           # 00, 0
        "Function_1_123",          # 01, 1
        "Function_2_129",          # 02, 2
        "Function_3_9C9",          # 03, 3
        "Function_4_9E5",          # 04, 4
        "Function_5_A0D",          # 05, 5
    )


    def Function_0_FA(): pass

    label("Function_0_FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_122")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_122")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_122")

    Return()

    # Function_0_FA end

    def Function_1_123(): pass

    label("Function_1_123")

    OP_22(0x1CD, 0x1, 0x5A)
    Return()

    # Function_1_123 end

    def Function_2_129(): pass

    label("Function_2_129")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10A, 420, 0, -55520, 0)
    OP_6D(250, 3770, -2820, 0)
    OP_67(0, 8930, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(45000, 0)
    OP_6E(435, 0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00三天之后——\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(1000)
    OP_1D(0x65)

    def lambda_1CB():
        OP_6D(250, 3770, -42460, 6000)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_1CB)

    def lambda_1E3():
        OP_8E(0xFE, 0x140, 0x0, 0xFFFF5E48, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_1E3)
    FadeToBright(2000, 0)
    OP_0D()
    OP_C8(0x200, 0x46, "C_PLAC10._CH", 0x0, 0x7D0)
    WaitChrThread(0x10A, 0x0)
    Fade(500)
    OP_6D(1120, 0, -40520, 0)
    OP_67(0, 7410, -10000, 0)
    OP_6B(2580, 0)
    OP_6C(45000, 0)
    OP_6E(307, 0)
    OP_0D()
    WaitChrThread(0x10A, 0x1)
    Sleep(500)

    ChrTalk(    #1
        0x10A,
        (
            "#810F#5P哇、哇啊～……\x01",
            "这里就是雷斯顿要塞啊。\x02\x03",

            "不愧是王国军的根据地，\x01",
            "这规模真是不得了啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_2D8():
        OP_8E(0xFE, 0x10E, 0x0, 0xFFFFEA7A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_2D8)
    Sleep(3000)
    Fade(1000)
    OP_6D(1190, 0, -3550, 0)
    OP_67(0, 7940, -10000, 0)
    OP_6B(2810, 0)
    OP_6C(44000, 0)
    OP_6E(274, 0)
    OP_0D()
    OP_44(0x10A, 0x0)
    SetChrPos(0x10A, 150, 250, -14360, 0)
    Sleep(500)

    def lambda_355():
        OP_8E(0xFE, 0x10E, 0x0, 0xFFFFEA7A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_355)
    WaitChrThread(0x10A, 0x0)

    ChrTalk(    #2
        0x10,
        "#5P嗯？……有什么事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10A,
        (
            "#810F嗯，\x01",
            "我想见卡西乌斯准将……\x02\x03",

            "请问他现在\x01",
            "有没有空呢？\x02",
        )
    )

    Jump("loc_3D4")

    label("loc_3D4")

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        (
            "#5P哪有这么简单。\x01",
            "很不巧，准将是百忙之身。\x02\x03",

            "不通过正式途径\x01",
            "事先取得联络，\x01",
            "是不可能见得到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10A,
        (
            "#810F咦咦！？　怎么这样……\x02\x03",

            "好不容易请假\x01",
            "来到这里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        (
            "#5P唔，虽然很遗憾，\x01",
            "但我也没有办法。\x02\x03",

            "不过，虽说可能没用，\x01",
            "我还是听听你有何贵干吧。\x02\x03",

            "以防万一，\x01",
            "我至少可以通知相关人士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10A,
        (
            "#810F是、是……那就拜托了。\x02\x03",

            "嗯～其实是这样……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetChrPos(0x10A, 3380, 250, -9200, 90)
    OP_6D(4950, 250, -8010, 0)
    OP_67(0, 5710, -10000, 0)
    OP_6B(2620, 0)
    OP_6C(44000, 0)
    OP_6E(294, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #8
        0x10A,
        (
            "#810F#5P呼～～……\x02\x03",

            "都来到这里了，\x01",
            "实在不想空手回去啊。\x02\x03",

            "……既然无法会面，\x01",
            "就去一趟王都的百货店吧。\x02\x03",

            "……嗯，看来只好这样了！\x02\x03",

            "要治愈受伤的心灵\x01",
            "那就非时尚小饰品莫属了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x10, 0x334, 0x0, 0xFFFFEB88, 0x7D0, 0x0)

    ChrTalk(    #9
        0x10,
        (
            "#2P喂，游击士小姑娘。\x02\x03",

            "来接你的人已经到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10A, 0, 400)

    ChrTalk(    #10
        0x10A,
        "#810F#2P咦？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 70, 0, 4000, 180)
    OP_22(0x6C, 0x0, 0x64)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1C2)
    Fade(500)
    OP_6D(40, 2450, -2700, 0)
    OP_67(0, 2060, -10000, 0)
    OP_6B(3580, 0)
    OP_6C(0, 0)
    OP_6E(365, 0)
    OP_8C(0x10, 0, 400)
    OP_0D()
    Sleep(1000)

    def lambda_745():
        OP_6D(570, 0, -3080, 5000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_745)

    def lambda_75D():
        OP_67(0, 4600, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_75D)

    def lambda_775():
        OP_6B(2580, 5000)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_775)

    def lambda_785():
        OP_6E(327, 5000)
        ExitThread()

    QueueWorkItem(0x10A, 3, lambda_785)
    OP_43(0x10, 0x0, 0x0, 0x4)
    Sleep(1000)
    OP_43(0x10A, 0x0, 0x0, 0x3)
    OP_73(0x0)
    OP_8F(0x11, 0x19A, 0x0, 0xFFFFF222, 0xBB8, 0x0)
    WaitChrThread(0x10A, 0x3)

    ChrTalk(    #11
        0x10,
        "#2P您辛苦了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x11,
        (
            "#5P辛苦了。\x02\x03",

            "你就是亚妮拉丝小姐？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10A,
        "#810F是、是的，是我没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x11,
        (
            "#5P哦～这样的小姑娘\x01",
            "竟然是大师的孙女啊……\x02\x03",

            "哦，现在不是\x01",
            "为这个感动的时候。\x02\x03",

            "准将同意见你了。\x01",
            "赶快跟我来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10A,
        "#810F咦，真的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x11,
        (
            "#5P是啊，\x01",
            "他专门为你腾出了时间来。\x02\x03",

            "好了，快来吧。\x02",
        )
    )

    Jump("loc_8F4")

    label("loc_8F4")

    CloseMessageWindow()

    ChrTalk(    #17
        0x10A,
        "#810F是、是！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 0, 400)

    def lambda_917():
        OP_6D(80, 0, 4520, 5000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_917)

    def lambda_92F():
        OP_67(0, 4000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_92F)

    def lambda_947():
        OP_6B(3010, 5000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_947)

    def lambda_957():
        OP_6E(347, 5000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_957)

    def lambda_967():
        OP_8E(0xFE, 0x46, 0x0, 0x222E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_967)
    Sleep(400)

    def lambda_987():
        OP_8E(0xFE, 0x46, 0x0, 0x222E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_987)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x10, 0x0)
    OP_44(0x10, 0x1)
    OP_44(0x10, 0x2)
    OP_44(0x10, 0x3)
    OP_A2(0x2506)
    NewScene("ED6_DT21/C3110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_129 end

    def Function_3_9C9(): pass

    label("Function_3_9C9")

    OP_8E(0xFE, 0x12C, 0xD2, 0xFFFFE3D6, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_3_9C9 end

    def Function_4_9E5(): pass

    label("Function_4_9E5")


    def lambda_9EB():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9EB)
    OP_8F(0xFE, 0x82A, 0x0, 0xFFFFEB88, 0x5DC, 0x0)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_4_9E5 end

    def Function_5_A0D(): pass

    label("Function_5_A0D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10A, 420, 0, -55520, 0)
    OP_6D(250, 3770, -2820, 0)
    OP_67(0, 8930, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(45000, 0)
    OP_6E(435, 0)
    OP_1D(0x65)
    OP_C8(0x200, 0x46, "C_PLAC10._CH", 0x0, 0x7D0)

    def lambda_A89():
        OP_6D(250, 3770, -42460, 6000)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_A89)

    def lambda_AA1():
        OP_8E(0xFE, 0x140, 0x0, 0xFFFF5E48, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_AA1)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x10A, 0x0)
    Fade(500)
    OP_6D(1120, 0, -40520, 0)
    OP_67(0, 7410, -10000, 0)
    OP_6B(2580, 0)
    OP_6C(45000, 0)
    OP_6E(307, 0)
    OP_0D()
    WaitChrThread(0x10A, 0x1)
    Sleep(500)

    ChrTalk(    #18
        0x10A,
        (
            "#1316F#6P呼～终于到了呢。\x02\x03",

            "#816F约定的时间也刚刚好……\x01",
            "那就赶快进去吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B73():
        OP_8E(0xFE, 0x10E, 0x0, 0xFFFFEA7A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_B73)
    Sleep(3000)
    Fade(1000)
    OP_6D(1190, 0, -2550, 0)
    OP_67(0, 7940, -10000, 0)
    OP_6B(2810, 0)
    OP_6C(44000, 0)
    OP_6E(274, 0)
    OP_44(0x10A, 0x0)
    SetChrPos(0x10A, 150, 250, -12360, 0)
    OP_0D()
    Sleep(500)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #19
        0x10,
        "#5P嗯？……有什么事？\x02",
    )

    CloseMessageWindow()

    def lambda_C2E():
        OP_8E(0xFE, 0x10E, 0x0, 0xFFFFEA7A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_C2E)
    OP_6D(1190, 0, -3550, 2300)
    WaitChrThread(0x10A, 0x0)
    Sleep(500)

    ChrTalk(    #20
        0x10A,
        (
            "#1310F#12P嗯～\x01",
            "我叫亚妮拉丝·艾尔菲德，\x01",
            "是一名游击士。\x02\x03",

            "今天是来会见\x01",
            "卡西乌斯准将的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        "#5P啊啊，是你吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        (
            "#5P我听说了。\x01",
            "这就联络相关人士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        (
            "#5P不过，\x01",
            "需要你稍微在这里等一下。\x02",
        )
    )

    Jump("loc_D4D")

    label("loc_D4D")

    CloseMessageWindow()

    ChrTalk(    #24
        0x10A,
        (
            "#814F#12P咦？　约定的时间\x01",
            "应该是刚刚好的……\x02\x03",

            "发生什么事了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        (
            "#5P不，\x01",
            "详情我也不是很清楚……\x02",
        )
    )

    Jump("loc_DD0")

    label("loc_DD0")

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        (
            "#5P准将的工作十分繁忙，\x01",
            "这次也是尽量挤出\x01",
            "时间来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        (
            "#5P不管如何，我先联络一下，\x01",
            "就请你稍等片刻吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10A,
        "#816F#12P是，好的……那就拜托了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(2000)
    SetChrPos(0x10A, 3380, 250, -9200, 90)
    OP_6D(4950, 250, -8010, 0)
    OP_67(0, 5710, -10000, 0)
    OP_6B(2620, 0)
    OP_6C(44000, 0)
    OP_6E(294, 0)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #29
        0x10A,
        (
            "#813F#5P唔，好慢啊……\x02\x03",

            "难道，\x01",
            "会面被取消了吗？\x02\x03",

            "#1316F唉，特地从大老远来到这里，\x01",
            "实在不想空手回去啊。\x02",
        )
    )

    Jump("loc_F70")

    label("loc_F70")

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x10A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10A)
    Sleep(500)

    ChrTalk(    #30
        0x10A,
        (
            "#816F#5P……如果无法会面的话，\x01",
            "就去一趟王都的百货店吧。\x02\x03",

            "现在应该正是新品玩偶\x01",
            "快要进货的时期了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #31
        0x10A,
        (
            "#1311F#5P嗯，买只小熊如何呢？\x01",
            "或者偶尔买一个鳄鱼娃娃也不错吧㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x10, 0x334, 0x0, 0xFFFFEB88, 0x7D0, 0x0)
    Sleep(300)

    ChrTalk(    #32
        0x10,
        "#2P喂，游击士小姑娘。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10,
        "#2P来接你的人已经到了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10A, 0, 400)
    Sleep(300)

    ChrTalk(    #34
        0x10A,
        "#814F#11P咦？\x02",
    )

    CloseMessageWindow()
    OP_59()
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 0, 0, 4000, 180)
    OP_22(0x6C, 0x0, 0x64)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1C2)
    Fade(500)
    OP_6D(40, 2450, -2700, 0)
    OP_67(0, 2060, -10000, 0)
    OP_6B(3580, 0)
    OP_6C(0, 0)
    OP_6E(365, 0)
    OP_8C(0x10, 0, 400)
    OP_0D()
    Sleep(1000)

    def lambda_1192():
        OP_6D(570, 0, -3080, 5000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_1192)

    def lambda_11AA():
        OP_67(0, 4600, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_11AA)

    def lambda_11C2():
        OP_6B(2580, 5000)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_11C2)

    def lambda_11D2():
        OP_6E(327, 5000)
        ExitThread()

    QueueWorkItem(0x10A, 3, lambda_11D2)
    OP_43(0x10, 0x0, 0x0, 0x4)
    Sleep(1500)
    OP_43(0x10A, 0x0, 0x0, 0x3)
    OP_73(0x0)
    OP_8F(0x11, 0x0, 0x0, 0xFFFFF222, 0xBB8, 0x0)
    WaitChrThread(0x10A, 0x3)

    ChrTalk(    #35
        0x10,
        "#2P您辛苦了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x11,
        "#5P辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x11,
        "#5P你就是亚妮拉丝小姐吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10A,
        "#814F#6P是，是的，我就是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x11,
        "#5P欢迎光临雷斯顿要塞。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x11,
        (
            "#5P准将正等着呢。\x01",
            "那就请跟我来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10A,
        (
            "#1310F#6P咦，真的吗？\x02\x03",

            "#811F那就是说，\x01",
            "可以和卡西乌斯先生见面了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x11,
        (
            "#5P嗯，让你久等了，\x01",
            "真是抱歉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x11,
        "#5P那么，就请到这边来吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x10A,
        "#816F#6P是，知道了！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 0, 400)

    def lambda_13B3():
        OP_6D(80, 0, 4520, 5000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_13B3)

    def lambda_13CB():
        OP_67(0, 4000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_13CB)

    def lambda_13E3():
        OP_6B(3010, 5000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_13E3)

    def lambda_13F3():
        OP_6E(347, 5000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_13F3)

    def lambda_1403():
        OP_8E(0xFE, 0x46, 0x0, 0x222E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1403)
    Sleep(400)

    def lambda_1423():
        OP_8E(0xFE, 0x46, 0x0, 0x222E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_1423)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x10, 0x0)
    OP_44(0x10, 0x1)
    OP_44(0x10, 0x2)
    OP_44(0x10, 0x3)
    SetMapFlags(0x2000000)
    OP_A2(0x2506)
    NewScene("ED6_DT21/C3110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_A0D end

    SaveToFile()

Try(main)
