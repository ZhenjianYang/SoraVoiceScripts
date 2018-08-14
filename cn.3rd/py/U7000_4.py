from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U7000_4 ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U7000.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60210",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/U7000   ._SN',
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
        '',                                     # 8
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
        "Function_3_E0E",          # 03, 3
        "Function_4_4684",         # 04, 4
        "Function_5_469E",         # 05, 5
        "Function_6_46B8",         # 06, 6
        "Function_7_46D2",         # 07, 7
        "Function_8_46EC",         # 08, 8
        "Function_9_4706",         # 09, 9
        "Function_10_4720",        # 0A, 10
        "Function_11_473A",        # 0B, 11
        "Function_12_4754",        # 0C, 12
        "Function_13_49EB",        # 0D, 13
        "Function_14_4CC1",        # 0E, 14
        "Function_15_4F53",        # 0F, 15
        "Function_16_53E2",        # 10, 16
        "Function_17_96EB",        # 11, 17
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS450._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS451._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS452._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS453._CH")
    OP_C5(0x4, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS454._CH")
    OP_C5(0x5, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS455._CH")
    Sleep(2000)
    OP_22(0xC3, 0x1, 0x64)
    Sleep(2000)
    OP_23(0xC3)
    OP_22(0x83, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0xAE)
    OP_C6(0x0, 0x3, -1, 2000, 0)
    Sleep(3000)
    SetMessageWindowPos(60, 240, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #0
        (
            "\x07\x0C#30W喂，这里是七耀教会、\x01",
            "艾梅洛斯市礼拜堂──\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(360, 120, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(    #1
        (
            "\x07\x0C#30W哎呀……\x01",
            "凯文，是你啊。\x02\x03",

            "我以为你还没到，\x01",
            "本想拜托教区长\x01",
            "替我带个话给你的……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(60, 240, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #2
        (
            "\x07\x0C#30W是露菲娜姐姐啊。\x02\x03",

            "我今天上午\x01",
            "就已经到了。\x02\x03",

            "你那边怎么样？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(360, 120, -1, -1)
    SetChrName("露菲娜的声音")

    AnonymousTalk(    #3
        (
            "\x07\x0C#30W好像是因为出了些事故，\x01",
            "列车要晚些才能到达。\x02\x03",

            "等到你那边\x01",
            "大概就要傍晚了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(60, 240, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #4
        (
            "\x07\x0C#30W是吗，\x01",
            "那我就在这里等你好了。\x02\x03",

            "如果就我一个人先回去，\x01",
            "莉丝和那些小鬼们\x01",
            "一定会失望的。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(360, 120, -1, -1)
    SetChrName("露菲娜的声音")

    AnonymousTalk(    #5
        (
            "\x07\x0C#30W呵呵，\x01",
            "我觉得应该不会吧。\x02\x03",

            "这么说来……\x01",
            "你已经想好\x01",
            "怎么哄莉丝高兴了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(60, 240, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #6
        (
            "\x07\x0C#30W嘿嘿，交给我吧。\x02\x03",

            "我执行任务的时候\x01",
            "买了很多各地的特产。\x02\x03",

            "那家伙一定会很开心的吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(360, 120, -1, -1)
    SetChrName("露菲娜的声音")

    AnonymousTalk(    #7
        (
            "\x07\x0C#30W唔……\x01",
            "难说啊。\x02\x03",

            "这种年纪的女孩\x01",
            "可不是这么简单就能搞定的哦？\x02",
        )
    )

    Jump("loc_5AA")

    label("loc_5AA")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(60, 240, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #8
        (
            "\x07\x0C#30W唔，是这样吗？\x02\x03",

            "说起来，那家伙也已经13岁了。\x02\x03",

            "姐姐第一次见到我的时候，\x01",
            "大概就是这个年龄吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(360, 120, -1, -1)
    SetChrName("露菲娜的声音")

    AnonymousTalk(    #9
        (
            "\x07\x0C#30W呵呵……\x01",
            "听你这么一说，还真是呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    OP_22(0x17D, 0x1, 0x64)
    Sleep(1600)
    SetMessageWindowPos(360, 120, -1, -1)
    SetChrName("露菲娜的声音")

    AnonymousTalk(    #10
        (
            "\x07\x0C#30W不好……\x01",
            "列车似乎要出发了。\x02\x03",

            "那就以后再聊了。\x02\x03",

            "要是方便的话，\x01",
            "你先回去也可以。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(60, 240, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #11
        "\x07\x0C#30W我知道了，回头见。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    OP_23(0x17D)
    OP_22(0x83, 0x0, 0x64)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    Sleep(1500)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(60, 240, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #12
        (
            "\x07\x0C#30W是吗……\x01",
            "自那以来已经九年了吗。\x02\x03",

            "而且也有两年没有回家了……\x02\x03",

            "唉，莉丝那家伙\x01",
            "一定会非常生气吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(360, 180, -1, -1)
    SetChrName("男性的声音")

    AnonymousTalk(    #13
        "\x07\x0C#30W凯、凯文！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x3, -1, 1000, 0)
    Sleep(1500)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(60, 240, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #14
        (
            "\x07\x0C#30W教区长……\x02\x03",

            "您怎么了？\x01",
            "这么慌慌张张的。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(360, 180, -1, -1)
    SetChrName("教区长")

    AnonymousTalk(    #15
        (
            "\x07\x0C#30W那、那是……\x02\x03",

            "刚才有人看到了\x01",
            "一群穿黑衣的可疑人物\x01",
            "往郊外去了。\x02\x03",

            "好像是往山道那个方向……\x02",
        )
    )

    Jump("loc_95F")

    label("loc_95F")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x3, 0x3, -1, 500, 0)
    Sleep(1000)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(60, 240, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #16
        (
            "\x07\x0C#30W！？\x02\x03",

            "山道……难道！？\x02",
        )
    )

    Jump("loc_9CF")

    label("loc_9CF")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(360, 180, -1, -1)
    SetChrName("教区长")

    AnonymousTalk(    #17
        (
            "\x07\x0C#30W是啊……\x01",
            "大概是去『紫苑之家』吧。\x02\x03",

            "你想到什么了吗？\x02",
        )
    )

    Jump("loc_A36")

    label("loc_A36")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(60, 240, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #18
        (
            "\x07\x0C#30W不，\x01",
            "至少他们和骑士团没有关系。\x02\x03",

            "……我知道了。\x01",
            "我这就去确认一下。\x02",
        )
    )

    Jump("loc_AAF")

    label("loc_AAF")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(360, 180, -1, -1)
    SetChrName("教区长")

    AnonymousTalk(    #19
        (
            "\x07\x0C#30W好，那就拜托你了。\x02\x03",

            "对了……\x01",
            "露菲娜怎么样了？\x02",
        )
    )

    Jump("loc_B1C")

    label("loc_B1C")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(60, 240, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #20
        (
            "\x07\x0C#30W因为列车晚点，\x01",
            "她大概傍晚才能赶到。\x02\x03",

            "教区长，等她到了之后\x01",
            "请你把这件事转告给她。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x3, 0x3, 16777215, 1500, 0)
    Sleep(2500)
    OP_C6(0x4, 0x3, -1, 2000, 0)
    Sleep(3000)
    SetMessageWindowPos(340, 280, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #21
        (
            "\x07\x0C#30W可恶，这是哪来的佣兵……\x01",
            "不对，是『猎兵团』……\x02\x03",

            "从气息上来判断应该有五到十人……\x02\x03",

            "可是，他们为什么要来\x01",
            "袭击教会的福音设施……\x02\x03",

            "………………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0xD5, 0x0, 0x64)
    OP_C6(0x5, 0x3, -1, 500, 0)
    Sleep(1000)
    OP_C6(0x4, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(340, 280, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #22
        (
            "\x07\x0C#30W……这么磨蹭下去\x01",
            "莉丝和小鬼们会有危险的。\x02\x03",

            "没办法。\x01",
            "只好看我一个人的了。\x02",
        )
    )

    Jump("loc_D4F")

    label("loc_D4F")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x5, 0x3, 16777215, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #23
        (
            "\x07\x0C#40W百般磨练的武术和法术……\x01",
            "派上用场的时候到了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x5, 0x3, 16777215, 1500, 0)
    Sleep(2000)
    OP_20(0x1388)
    OP_21()
    Sleep(1000)
    OP_AD(0x2400E8, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    OP_A2(0x2505)
    OP_A2(0x250A)
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_2_AC end

    def Function_3_E0E(): pass

    label("Function_3_E0E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x26033B, 0x260340, 0x13)
    OP_D2(0x270080, 0x270084, 0x14)
    OP_D2(0x70598, 0x7059D, 0x15)
    LoadEffect(0x0, "map\\mp259_01.eff")
    ClearChrFlags(0x10F, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x22, 0, 4500, 1000, 180)
    SetChrChipByIndex(0x22, 21)
    SetChrSubChip(0x22, 0)
    SetChrFlags(0x22, 0x4)

    def lambda_E80():

        label("loc_E80")

        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_E80")

    QueueWorkItem2(0x22, 3, lambda_E80)
    OP_9F(0x22, 0xFF, 0xFF, 0xFF, 0xB4, 0x0)
    PlayEffect(0x0, 0x7, 0x22, 0, 800, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x10F, -100, 4000, -1600, 0)
    SetChrPos(0x101, -100, 4000, -3000, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x15, -1100, 4000, -3200, 0)
    SetChrPos(0x1F, 1300, 4000, -3100, 0)
    SetChrPos(0x11, 2400, 4000, -3170, 315)
    SetChrPos(0x12, 1300, 4000, -6500, 0)
    SetChrPos(0x13, 100, 4000, -6500, 0)
    SetChrPos(0x14, 2800, 4000, -5870, 0)
    SetChrPos(0x16, 800, 4000, -4300, 0)
    SetChrPos(0x18, -500, 4000, -4700, 0)
    SetChrPos(0x1E, -1520, 4000, -4800, 0)
    SetChrPos(0x1A, 2200, 4000, -4570, 0)
    SetChrPos(0x1B, 1450, 4000, -5600, 0)
    SetChrPos(0x1C, 3500, 4000, -4960, 315)
    SetChrPos(0x19, -1400, 4000, -6200, 0)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    OP_6D(-1100, 4000, -600, 0)
    OP_67(0, 4800, -10000, 0)
    OP_6B(2550, 0)
    OP_6C(315000, 0)
    OP_6E(350, 0)
    OP_E5(0x2, 0xFF, 0x13, 500)
    OP_1D(0xD2)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #24
        0x101,
        (
            "#1004F#6P赛雷斯托……\x02\x03",

            "这、这个名字好像是——\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x15,
        (
            "#1505F#6P将『辉之环』封印在异空间的\x01",
            "古代人类首领……\x02\x03",

            "#1500F并且还是传说中的\x01",
            "利贝尔王家始祖。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x22,
        (
            "\x07\x0C#1616F#11P呵呵……\x02\x03",

            "#1611F看来『我』留下来的情报\x01",
            "起了很大作用呢。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#1008F#6P是、是的……\x01",
            "承蒙您的帮忙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x16,
        (
            "#1163F#6P您是……\x01",
            "……利贝尔的始祖大人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x22,
        (
            "\x07\x0C#1616F#11P呵呵……准确的说，不是这样的。\x02\x03",

            "#1610F『我』只是真正的赛雷斯托的『影』。\x02\x03",

            "为了干涉这『影之国』\x01",
            "而再现出来的人格的一部分而已。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x16,
        "#1164F#6P再、再现出来的人格……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10F,
        (
            "#1446F#6P……我们已经明白了\x01",
            "这件事情的复杂性。\x02\x03",

            "#1448F不过，看起来\x01",
            "您并不是普通的幽灵吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x22,
        (
            "\x07\x0C#1615F#11P嗯，你说的没错。\x02\x03",

            "#1610F要说明我存在的原理……\x01",
            "首先需要向你们\x01",
            "解释清楚前提条件。\x02\x03",

            "也就是『这个世界\x01",
            "为什么会存在』的事情。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x11,
        "#560F#6P是、是真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x1F,
        (
            "#261F#6P嘻嘻……\x01",
            "越来越有趣了。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_21()
    OP_1D(0xB7)
    OP_AD(0x24015C, 0x0, 0x0, 0xC8)
    Sleep(3000)
    SetMessageWindowPos(220, 50, -1, -1)
    SetChrName("赛雷斯托")

    AnonymousTalk(    #35
        (
            "\x07\x0C#1615F『影之国』──\x02\x03",

            "这是数千年之前\x01",
            "由『辉之环』所构筑的\x01",
            "属于高位次元的世界。\x02\x03",

            "#1612F它是『辉之环』为了接受并处理\x01",
            "利贝尔方舟市民膨大的愿望和意念\x01",
            "而制造出来的子系统……\x02\x03",

            "也可以说它是能够实现各种可能的，\x01",
            "具有自己组织化机能的世界吧。\x07\x00\x02",
        )
    )

    Jump("loc_1563")

    label("loc_1563")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 100, -1, -1)
    SetChrName("莉丝")

    AnonymousTalk(    #36
        "\x07\x00#1444F哎……\x02",
    )

    Jump("loc_1593")

    label("loc_1593")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 150, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #37
        "\x07\x00#1019F等、等一下……！\x02",
    )

    Jump("loc_15D7")

    label("loc_15D7")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 280, -1, -1)
    SetChrName("亚妮拉丝")

    AnonymousTalk(    #38
        (
            "\x07\x00#1317F您突然这么说，\x01",
            "脑筋实在是有些跟不上……\x02",
        )
    )

    Jump("loc_1632")

    label("loc_1632")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(250, 50, -1, -1)
    SetChrName("赛雷斯托")

    AnonymousTalk(    #39
        (
            "\x07\x0C#1615F……是啊……\x02\x03",

            "#1610F这么解释起来太难理解了，\x01",
            "如果要说得浅显些……\x02\x03",

            "这里是『辉之环』\x01",
            "为了满足人们愿望\x01",
            "而创建的『虚构世界』。\x07\x00\x02",
        )
    )

    Jump("loc_16F1")

    label("loc_16F1")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 150, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #40
        "\x07\x00#1016F这、这还能够理解……\x02",
    )

    Jump("loc_1739")

    label("loc_1739")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("尤莉亚　　　　　　　")

    AnonymousTalk(    #41
        (
            "\x07\x00#172F『虚构世界』……\x02\x03",

            "可是，\x01",
            "说这里是虚假的世界，\x01",
            "给人的感觉也太过真实了。\x02",
        )
    )

    Jump("loc_17C2")

    label("loc_17C2")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(250, 50, -1, -1)
    SetChrName("赛雷斯托")

    AnonymousTalk(    #42
        (
            "\x07\x0C#1610F虽说是『虚构世界』，\x01",
            "但并不是单纯的『虚假』。\x02\x03",

            "#1616F它是依靠独自法则运行的影之世界……\x01",
            "又能够反映现实世界，\x01",
            "并像万花筒一样产生丰富的变化。\x02\x03",

            "#1611F这么说应该能够\x01",
            "更容易理解一些。\x07\x00\x02",
        )
    )

    Jump("loc_18B8")

    label("loc_18B8")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("尤莉亚　　　　　　　")

    AnonymousTalk(    #43
        "\x07\x00#170F……原来如此………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 250, -1, -1)
    SetChrName("穆拉")

    AnonymousTalk(    #44
        "\x07\x00#278F不愧被称为『影之国』……\x02",
    )

    Jump("loc_193E")

    label("loc_193E")

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1500)

    ChrTalk(    #45
        0x22,
        (
            "\x07\x0C#1610F#11P然后，这个『影之国』\x01",
            "还是协助『辉之环』\x01",
            "进行庞大处理的子系统。\x02\x03",

            "#1615F虽然不是『环』的本身，\x01",
            "但与其也是表里一体的存在……\x02\x03",

            "#1612F我们『封印机构』\x01",
            "就是看穿了这一点。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x16,
        (
            "#1162F#6P『封印机构』……\x02\x03",

            "那应该是立案并实行了\x01",
            "『辉之环』封印计划的古代人组织吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x22,
        (
            "\x07\x0C#1615F#11P是的。\x02\x03",

            "#1612F但是当初，\x01",
            "封印『环』的计划曾经被\x01",
            "认为是无法实现的。\x02\x03",

            "因为对空间具有绝对\x01",
            "支配权的『环』可以干涉\x01",
            "人类的绝大多数行动。\x02\x03",

            "#1613F由异空间产生的『时间冻结』\x01",
            "以及『重力结界』造成的间接约束，\x02\x03",

            "就算研究出了这两重封印方法，\x01",
            "也找不到可以实行的契机……\x02\x03",

            "#1615F计划走到了死胡同。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x18,
        (
            "#1545F#6P虽然找到了敌人的弱点，\x01",
            "但并没有攻击的机会……\x02\x03",

            "#1540F是这样一种状况吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x22,
        (
            "\x07\x0C#1616F#11P嗯，正如你说的那样。\x02\x03",

            "#1610F后来，为了制造出机会，\x01",
            "我们『封印机构』就开发出了\x01",
            "『雷克鲁斯方石』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x19, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Sleep(300)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 19)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #50
        0x10F,
        "#1443F#6P……是说这个吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x22,
        (
            "\x07\x0C#1610F#11P嗯，它是可以不依靠『环』\x01",
            "而直接对『影之国』进行干涉的\x01",
            "唯一终端装置。\x02\x03",

            "真正的赛雷斯托通过方石\x01",
            "使自己人格的一部分——也就是『我』，\x01",
            "侵入了『影之国』。\x02\x03",

            "然后『我』以这个『庭院』为据点\x01",
            "做了各种各样的干涉行动，\x01",
            "使『影之国』全体陷入了机能不全的状况。\x02\x03",

            "#1615F其结果就是──\x01",
            "『环』的处理能力暂时得到降低，\x01",
            "而产生出了让计划得以实行的破绽。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x1F,
        "#263F#6P嗯，原来如此……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #53
        0x19,
        (
            "#573F#6P声东击西吗……\x02\x01",

            "#070F十分符合武术原理呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x11,
        (
            "#560F#6P真、真是\x01",
            "严密的计划……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x22,
        (
            "\x07\x0C#1611F#11P呵呵……\x01",
            "其实也有运气的成分。\x02\x03",

            "#1616F然后──\x01",
            "『辉之环』被封印之后，\x01",
            "我就在这个地方陷入了长眠。\x02\x03",

            "以备在将来『环』的封印解除之时，\x01",
            "能够给予后世的人们帮助。\x02\x03",

            "#1610F不过──\x01",
            "看来担心是多余的了，对吧？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        (
            "#1016F#6P哈、哈哈……\x02\x03",

            "#1008F那才应该说是\x01",
            "运气占了大多数吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x15,
        (
            "#1505F#6P但是，『辉之环』\x01",
            "不知消失到何处去了。\x02\x03",

            "#1503F遗憾的是现在仍然\x01",
            "无法判断它的行踪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x22,
        (
            "\x07\x0C#1613F#11P果然是这样吗……\x02\x03",

            "#1615F……『环』的消失一事\x01",
            "我也已经确认过了。\x02\x03",

            "这样我的任务就已结束……\x02\x03",

            "接下来就是悠闲地等待\x01",
            "和『影之国』一起灭亡的时候到来。\x02\x03",

            "#1612F就是在我\x01",
            "这么想着的时候——\x02\x03",

            "那个『影之王』出现了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x19, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #59
        0x16,
        "#1163F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x10F,
        "#1443F#6P……原来如此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x1F,
        (
            "#1306F#6P嘻嘻……\x01",
            "终于到了核心部分呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x22,
        (
            "\x07\x0C#1615F#11P那个人毫无预兆地出现，\x01",
            "夺走了身处『庭院』的我的力量。\x02\x03",

            "而且还肆意的改变了\x01",
            "『影之国』的面貌。\x02\x03",

            "#1612F构成现在这个世界的\x01",
            "被称为『星层』的若干领域……\x02\x03",

            "那都是『影之王』\x01",
            "所创造出来的。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x1E,
        (
            "#115F#6P嗯……\x01",
            "和玲所推测的一样。\x02\x03",

            "#112F可是这样一来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x1C,
        (
            "#055F#6P是、是啊……\x02\x03",

            "难道你也不知道\x01",
            "那个面具小子的真实身份吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x22,
        (
            "\x07\x0C#1615F#11P……很遗憾。\x02\x03",

            "#1613F那个人如何入侵\x01",
            "这个全封闭的世界……\x02\x03",

            "以及为什么要将你们\x01",
            "卷入这里并且进行试炼……\x02\x03",

            "#1612F这一连串的事件\x01",
            "我现在也无法判明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x1B,
        "#1525F#6P真是糟糕……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x14,
        (
            "#413F#6P嗯、嗯……\x01",
            "那可是最关键的地方啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x22,
        (
            "\x07\x0C#1615F#11P对了……\x01",
            "如果说线索的话……\x02\x03",

            "#1612F我认为『影之王』\x01",
            "大概就在所谓的\x01",
            "『第七星层』领域中。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x19, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #69
        0x10F,
        "#1444F#6P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        "#1004F#6P为、为什么会这样想呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x22,
        (
            "\x07\x0C#1612F#11P那是『影之王』刚出现的时候\x01",
            "最先创造的领域。\x02\x03",

            "其中究竟是怎样一种景象\x01",
            "我也无从知晓……\x02\x03",

            "#1615F但可以感觉到\x01",
            "从那个地方向整个『影之国』\x01",
            "扩散的非同寻常的意念。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "#1026F#6P是、是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x11,
        (
            "#062F#6P说到『第七』……\x01",
            "那应该是下一个的下一个吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x15,
        (
            "#1505F#6P嗯，\x01",
            "现在我们到达了『第五星层』的终点。\x02\x03",

            "#1502F……看来对决的时刻\x01",
            "已经不远了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x1C,
        "#051F#6P哼……正好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x18,
        (
            "#1545F#6P呵呵，\x01",
            "看到解决这件事情的希望了。\x02\x03",

            "#1540F如果能知道一点影之王的目的，\x01",
            "那就更好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, 320, 4100, -14250, 0)
    SetChrChipByIndex(0x21, 20)
    SetChrSubChip(0x21, 0)

    NpcTalk(    #77
        0x21,
        "青年的声音",
        (
            "#2P──关于那件事，\x01",
            "我已经有想法了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x19, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2E00():

        label("loc_2E00")

        TurnDirection(0xFE, 0x21, 400)
        OP_48()
        Jump("loc_2E00")

    QueueWorkItem2(0x10F, 3, lambda_2E00)

    def lambda_2E11():

        label("loc_2E11")

        TurnDirection(0xFE, 0x21, 400)
        OP_48()
        Jump("loc_2E11")

    QueueWorkItem2(0x101, 3, lambda_2E11)

    def lambda_2E22():

        label("loc_2E22")

        TurnDirection(0xFE, 0x21, 400)
        OP_48()
        Jump("loc_2E22")

    QueueWorkItem2(0x15, 3, lambda_2E22)

    def lambda_2E33():

        label("loc_2E33")

        TurnDirection(0xFE, 0x21, 400)
        OP_48()
        Jump("loc_2E33")

    QueueWorkItem2(0x11, 3, lambda_2E33)

    def lambda_2E44():

        label("loc_2E44")

        TurnDirection(0xFE, 0x21, 400)
        OP_48()
        Jump("loc_2E44")

    QueueWorkItem2(0x19, 3, lambda_2E44)

    def lambda_2E55():

        label("loc_2E55")

        TurnDirection(0xFE, 0x21, 400)
        OP_48()
        Jump("loc_2E55")

    QueueWorkItem2(0x12, 3, lambda_2E55)

    def lambda_2E66():

        label("loc_2E66")

        TurnDirection(0xFE, 0x21, 400)
        OP_48()
        Jump("loc_2E66")

    QueueWorkItem2(0x16, 3, lambda_2E66)

    def lambda_2E77():

        label("loc_2E77")

        TurnDirection(0xFE, 0x21, 400)
        OP_48()
        Jump("loc_2E77")

    QueueWorkItem2(0x13, 3, lambda_2E77)

    def lambda_2E88():

        label("loc_2E88")

        TurnDirection(0xFE, 0x21, 400)
        OP_48()
        Jump("loc_2E88")

    QueueWorkItem2(0x18, 3, lambda_2E88)

    def lambda_2E99():

        label("loc_2E99")

        TurnDirection(0xFE, 0x21, 400)
        OP_48()
        Jump("loc_2E99")

    QueueWorkItem2(0x14, 3, lambda_2E99)

    def lambda_2EAA():

        label("loc_2EAA")

        TurnDirection(0xFE, 0x21, 400)
        OP_48()
        Jump("loc_2EAA")

    QueueWorkItem2(0x1C, 3, lambda_2EAA)

    def lambda_2EBB():

        label("loc_2EBB")

        TurnDirection(0xFE, 0x21, 400)
        OP_48()
        Jump("loc_2EBB")

    QueueWorkItem2(0x1A, 3, lambda_2EBB)

    def lambda_2ECC():

        label("loc_2ECC")

        TurnDirection(0xFE, 0x21, 400)
        OP_48()
        Jump("loc_2ECC")

    QueueWorkItem2(0x1B, 3, lambda_2ECC)

    def lambda_2EDD():

        label("loc_2EDD")

        TurnDirection(0xFE, 0x21, 400)
        OP_48()
        Jump("loc_2EDD")

    QueueWorkItem2(0x1F, 3, lambda_2EDD)

    def lambda_2EEE():

        label("loc_2EEE")

        TurnDirection(0xFE, 0x21, 400)
        OP_48()
        Jump("loc_2EEE")

    QueueWorkItem2(0x1E, 3, lambda_2EEE)
    Fade(500)
    OP_6D(-770, 4100, -12910, 0)
    OP_67(0, 5310, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(222000, 0)
    OP_6E(398, 0)
    SetChrPos(0x22, 500, 4500, 500, 180)
    SetChrPos(0x10F, -530, 4000, -1900, 180)
    SetChrPos(0x101, -520, 4000, -3300, 180)
    SetChrPos(0x15, -1900, 4000, -3140, 180)
    SetChrPos(0x1F, 910, 4000, -3240, 180)
    SetChrPos(0x11, 2400, 4000, -2870, 225)
    SetChrPos(0x12, 370, 4000, -6430, 180)
    SetChrPos(0x13, -980, 4000, -6350, 180)
    SetChrPos(0x14, 2000, 4000, -6250, 225)
    SetChrPos(0x16, -270, 4000, -4590, 180)
    SetChrPos(0x18, -1600, 4000, -4850, 180)
    SetChrPos(0x1E, -3030, 4000, -5200, 135)
    SetChrPos(0x1A, 2600, 4000, -4350, 225)
    SetChrPos(0x1B, 1170, 4000, -4730, 180)
    SetChrPos(0x1C, 3600, 4000, -5020, 225)
    SetChrPos(0x19, -2790, 4000, -6770, 135)
    OP_1D(0xAD)

    def lambda_3053():
        OP_6D(-1000, 4000, -8000, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_3053)

    def lambda_306B():
        OP_8E(0xFE, 0x64, 0xFA0, 0xFFFFD936, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_306B)
    WaitChrThread(0x21, 0x0)
    WaitChrThread(0x10F, 0x0)

    ChrTalk(    #78
        0x10F,
        "#1444F#11P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        "#1018F#11P凯文先生！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x1E,
        (
            "#111F#11P凯文神父……\x01",
            "庆祝会以后就没再见过面了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x21,
        (
            "#1075F#5P是呀……\x01",
            "没想到连你\x01",
            "也被卷了进来。\x02\x03",

            "#1840F而且……还有这位小姑娘。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x1F,
        (
            "#263F#6P……是啊。\x02\x03",

            "#1305F玲可是有一些事情\x01",
            "要问这位哥哥呢。\x02\x03",

            "不过，以后有机会再说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x21,
        "#1066F#5P哈哈，不好意思。\x02",
    )

    CloseMessageWindow()

    def lambda_3202():
        OP_6D(-820, 4000, -4440, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_3202)
    SetChrFlags(0x21, 0x40)

    def lambda_321F():
        OP_8E(0xFE, 0x514, 0xFA0, 0xFFFFF894, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_321F)
    OP_43(0x12, 0x0, 0x4, 0x4)
    OP_43(0x13, 0x0, 0x4, 0x5)
    OP_43(0x1B, 0x0, 0x4, 0x6)
    OP_43(0x1A, 0x0, 0x4, 0x7)
    OP_43(0x16, 0x0, 0x4, 0x8)
    OP_43(0x18, 0x0, 0x4, 0x9)
    OP_43(0x1F, 0x0, 0x4, 0xA)
    OP_43(0x11, 0x0, 0x4, 0xB)
    WaitChrThread(0x21, 0x0)
    OP_44(0x10F, 0x3)
    OP_44(0x101, 0x3)
    OP_44(0x15, 0x3)
    OP_44(0x11, 0x3)
    OP_44(0x19, 0x3)
    OP_44(0x12, 0x3)
    OP_44(0x16, 0x3)
    OP_44(0x13, 0x3)
    OP_44(0x18, 0x3)
    OP_44(0x14, 0x3)
    OP_44(0x1C, 0x3)
    OP_44(0x1A, 0x3)
    OP_44(0x1B, 0x3)
    OP_44(0x1F, 0x3)
    OP_44(0x1E, 0x3)
    WaitChrThread(0x10F, 0x0)
    Fade(500)
    OP_6D(-1000, 4000, -510, 0)
    OP_67(0, 5340, -10000, 0)
    OP_6B(1950, 0)
    OP_6C(318000, 0)
    OP_6E(466, 0)
    SetChrPos(0x22, 0, 4500, 1000, 180)
    SetChrPos(0x21, 800, 4000, -1600, 0)
    SetChrPos(0x10F, -500, 4000, -1700, 90)
    SetChrPos(0x101, -100, 4000, -3000, 0)
    SetChrPos(0x15, -1100, 4000, -3200, 0)
    SetChrPos(0x1F, 1300, 4000, -3100, 0)
    SetChrPos(0x11, 2400, 4000, -3170, 315)
    SetChrPos(0x12, 1300, 4000, -6500, 0)
    SetChrPos(0x13, 100, 4000, -6500, 0)
    SetChrPos(0x14, 2800, 4000, -5870, 0)
    SetChrPos(0x16, 800, 4000, -4300, 0)
    SetChrPos(0x18, -500, 4000, -4700, 0)
    SetChrPos(0x1E, -1520, 4000, -4800, 0)
    SetChrPos(0x1A, 2200, 4000, -4570, 0)
    SetChrPos(0x1B, 1500, 4000, -5600, 0)
    SetChrPos(0x1C, 3500, 4000, -4960, 315)
    SetChrPos(0x19, -1400, 4000, -6200, 0)
    OP_0D()
    ClearChrFlags(0x21, 0x40)
    OP_8C(0x21, 270, 400)
    Sleep(500)

    ChrTalk(    #84
        0x10F,
        (
            "#1802F#5P凯文……\x01",
            "那个，你已经没事了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x21,
        (
            "#1071F#12P嗯，舒舒服服地睡了一觉，\x01",
            "现在感到精神十分爽快。\x02\x03",

            "#1840F话说回来，在我倒下期间，\x01",
            "你们的进展可真是不小。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x10F,
        "#1806F#5P嗯……\x02",
    )

    CloseMessageWindow()

    def lambda_3502():
        OP_6D(-800, 4000, 0, 1000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_3502)

    def lambda_351A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_351A)
    Sleep(100)
    OP_8C(0x10F, 0, 400)
    WaitChrThread(0x10F, 0x0)
    Sleep(300)

    ChrTalk(    #87
        0x21,
        (
            "#1075F#6P初次见面……\x01",
            "我是凯文·格拉汉姆。\x02\x03",

            "#1078F看来您已经十分了解\x01",
            "我们的事情了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x22,
        (
            "\x07\x0C#1616F#11P嗯，\x01",
            "我在这个『庭院』已经知道了\x01",
            "利贝尔方舟上所发生的事情。\x02\x03",

            "#1610F不过……\x01",
            "关于这次的事件，\x01",
            "你应该是最接近真相的人。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x10F,
        "#1444F#6P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x21,
        (
            "#1075F#6P嗯，我也是这样认为的。\x02\x03",

            "#1840F『影之国』是什么东西\x01",
            "暂且不说……\x02\x03",

            "关于『影之王』的身份\x01",
            "我的确已有结论。\x02\x03",

            "说老实话，会弄出这些名堂的家伙\x01",
            "再也找不到第二个人了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x10F,
        "#1802F#6P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        (
            "#1020F#6P这、这么说……\x01",
            "是凯文先生认识的人吗！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_378E():
        OP_6D(-500, 4000, -1000, 1000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_378E)

    def lambda_37A6():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_37A6)
    Sleep(50)

    def lambda_37B9():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_37B9)
    Sleep(50)

    def lambda_37CC():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_37CC)
    Sleep(50)
    OP_8C(0x10F, 135, 400)
    WaitChrThread(0x10F, 0x0)

    ChrTalk(    #93
        0x21,
        (
            "#1075F#11P哈哈……\x01",
            "该怎么说呢。\x02\x03",

            "#1067F这么来形容吧……\x01",
            "那是个性格相当恶劣的家伙。\x02\x03",

            "又奸诈又傲慢……\x01",
            "不把人当人看的冷血动物。\x02\x03",

            "#1840F总之，就是这么个无赖吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x14,
        (
            "#212F#6P听、听起来好像\x01",
            "是个来头很大的家伙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x18,
        (
            "#1542F#6P唔……\x01",
            "你就明说吧，那到底是谁？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x21,
        (
            "#1841F#11P话虽这么说……\x02\x03",

            "在说出答案之前，\x01",
            "你们能再给我一些时间吗？\x02\x03",

            "#1840F虽然我已经确信自己的想法，\x01",
            "但还是缺少关键的证据。\x02\x03",

            "大概，在接下来的『第六星层』\x01",
            "就可以得到确证了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x18,
        (
            "#1545F#6P呵呵……\x01",
            "原来如此，我就知道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x13,
        (
            "#276F……看来有我们\x01",
            "不了解的隐情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x21,
        (
            "#1065F#11P我知道这种做法很自私。\x02\x03",

            "#1063F所以我向你们保证，\x01",
            "等我得到确证，一定会向你们坦陈一切。\x02\x03",

            "以空之女神以及星杯纹章的名义。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x12,
        "#170F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x1C,
        "#051F#6P──唉，这样也好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x1B,
        (
            "#1534F#6P是啊……\x01",
            "既然都已经说到这种份上……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x1A,
        (
            "#819F#6P凯文先生会拜托我们\x01",
            "也很难得呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x14,
        "#210F#6P反、反正我是无所谓啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        (
            "#1016F#6P啊哈哈……\x01",
            "我就更不用说了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x15,
        (
            "#1513F#6P我也认为\x01",
            "凯文先生的判断值得信赖。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x11,
        "#560F#6P我、我也是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x1F,
        (
            "#261F#6P嗯～只要是好玩儿的事情，\x01",
            "对玲来说怎样都无所谓啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x16,
        (
            "#1168F#6P呵呵，看来没有人\x01",
            "提出反对意见呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x19,
        "#573F#6P嗯，那就这么决定吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x10F,
        "#1806F#5P大家……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x21,
        (
            "#1075F#11P……十分感谢。\x02\x03",

            "#1840F接下来就由我\x01",
            "继续担当各位的向导吧。\x02\x03",

            "再次请你们多多关照。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        "#1018F#6P嗯，彼此彼此！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x22,
        (
            "\x07\x0C#1616F#11P呵呵……\x01",
            "看来你们已经达成一致了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3DE5():
        OP_6D(-800, 4000, 0, 1000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_3DE5)

    def lambda_3DFD():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_3DFD)
    Sleep(100)
    OP_8C(0x10F, 0, 400)
    WaitChrThread(0x10F, 0x0)
    Sleep(300)

    ChrTalk(    #115
        0x22,
        (
            "\x07\x0C#1610F#11P我就在这里继续调查\x01",
            "关于『第七星层』的情报。\x02\x03",

            "当然，我也会继续\x01",
            "通过『方石』和『石碑』\x01",
            "给你们以必要的帮助。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x21,
        (
            "#1079F#6P对了……\x01",
            "之前我们也受到了您\x01",
            "各种各样的帮助呢。\x02\x03",

            "#1075F真是太感谢您了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x16,
        (
            "#1382F#6P……始祖大人。\x01",
            "由衷地感谢您。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x22,
        (
            "\x07\x0C#1616F呵呵……\x01",
            "不用那么客气。\x02\x03",

            "#1611F我只是『影』……\x01",
            "赛雷斯托本人的\x01",
            "一部分人格的再现而已。\x02\x03",

            "而且这也可以说是\x01",
            "过去我被赋予使命的延续。\x02\x03",

            "我会尽全力帮忙的。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x21,
        (
            "#1840F#6P十分感谢。\x01",
            "那就拜托您了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(1440, 4000, -520, 0)
    OP_67(0, 5280, -10000, 0)
    OP_6B(2150, 0)
    OP_6C(36000, 0)
    OP_6E(376, 0)
    SetChrPos(0x21, 1200, 4000, -1500, 0)
    SetChrPos(0x10F, -190, 4000, -1900, 0)
    SetChrPos(0x101, -110, 4000, -4240, 0)
    SetChrPos(0x15, -1200, 4000, -4050, 45)
    SetChrPos(0x1F, 1400, 4000, -3680, 0)
    SetChrPos(0x11, 2800, 4000, -3060, 315)
    SetChrPos(0x12, 1500, 4000, -6600, 0)
    SetChrPos(0x13, 100, 4000, -6940, 0)
    SetChrPos(0x14, 3250, 4000, -5870, 0)
    SetChrPos(0x16, 1160, 4000, -5170, 0)
    SetChrPos(0x18, -120, 4000, -5740, 0)
    SetChrPos(0x1E, -1550, 4000, -5800, 45)
    SetChrPos(0x1A, 3700, 4000, -3600, 315)
    SetChrPos(0x1B, 2200, 4000, -5440, 0)
    SetChrPos(0x1C, 4300, 4000, -4400, 315)
    SetChrPos(0x19, -1500, 4000, -7310, 45)
    OP_0D()
    OP_8C(0x21, 270, 400)
    Sleep(50)
    OP_8C(0x10F, 90, 400)
    Sleep(300)

    ChrTalk(    #120
        0x21,
        (
            "#1065F#11P莉丝……\x01",
            "让你担心了，实在抱歉。\x02\x03",

            "#1063F不过，接下来的事\x01",
            "请交给我吧。\x02\x03",

            "这是我一生的愿望。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x10F,
        (
            "#1802F#6P…………………………………\x02\x03",

            "#1445F……和我做个约定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x21,
        "#1079F#11P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x10F,
        (
            "#1446F#6P我不会劝你不要胡来。\x02\x03",

            "#1806F不过……\x01",
            "请一定不要做出\x01",
            "让姐姐伤心的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #124
        0x21,
        (
            "#1063F#11P………哎……………\x02\x03",

            "#1068F哈哈……\x01",
            "你说到我的痛处了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x10F,
        "#1806F#6P……你答应吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x21,
        (
            "#1067F#11P……………………………………\x02\x03",

            "#1075F嗯，我和你约定。\x02\x03",

            "#1840F不以女神或是星杯的名义……\x01",
            "而是以姐姐的名义发誓。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4414():
        OP_6B(3000, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_4414)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    Sleep(1000)
    OP_1D(0xD2)
    OP_44(0x10F, 0x0)
    OP_A2(0x2B00)
    OP_28(0x36, 0x1, 0x100)
    OP_28(0x35, 0x4, 0x10)
    OP_28(0x35, 0x4, 0x20)
    OP_28(0x36, 0x4, 0x10)
    OP_28(0x36, 0x4, 0x20)
    OP_28(0x37, 0x4, 0x4)
    OP_28(0x37, 0x4, 0x8)
    OP_28(0x37, 0x1, 0x1)
    OP_3F(0x360, 1)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x21, 0x80)
    ClearChrFlags(0xF0, 0x80)
    ClearChrFlags(0xF1, 0x80)
    OP_DB(0x0, 0x8)
    ClearParty()
    AddParty(0x8, 0xEE, 0xFF)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_DD(0x1, 0x0, 0x0, 256, 0, 0, 0)
    FadeToDark(0, 0, -1)
    OP_C0(0x20, 0x1, 0x100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    OP_6D(390, 4000, -1290, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x0, 390, 4000, -1290, 180)
    SetChrPos(0x1, 390, 4000, -1290, 180)
    SetChrPos(0x2, 390, 4000, -1290, 180)
    SetChrPos(0x3, 390, 4000, -1290, 180)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_E5(0x2, 0xFF, 0x13, 700)
    Call(0, 5)
    SetChrChipByIndex(0x22, 0)
    SetChrSubChip(0x22, 0)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x22, -2100, 4500, 3610, 135)
    SetChrFlags(0x22, 0x4)

    def lambda_4626():

        label("loc_4626")

        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_4626")

    QueueWorkItem2(0x22, 3, lambda_4626)
    OP_9F(0x22, 0xFF, 0xFF, 0xFF, 0xB4, 0x0)
    PlayEffect(0x0, 0x7, 0x22, 0, 800, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_3_E0E end

    def Function_4_4684(): pass

    label("Function_4_4684")

    Sleep(500)
    OP_8F(0xFE, 0xFFFFFE34, 0xFA0, 0xFFFFE822, 0x3E8, 0x0)
    Return()

    # Function_4_4684 end

    def Function_5_469E(): pass

    label("Function_5_469E")

    Sleep(600)
    OP_8F(0xFE, 0xFFFFF984, 0xFA0, 0xFFFFE48A, 0x3E8, 0x0)
    Return()

    # Function_5_469E end

    def Function_6_46B8(): pass

    label("Function_6_46B8")

    Sleep(900)
    OP_8F(0xFE, 0x76C, 0xFA0, 0xFFFFEDFE, 0x3E8, 0x0)
    Return()

    # Function_6_46B8 end

    def Function_7_46D2(): pass

    label("Function_7_46D2")

    Sleep(1000)
    OP_8F(0xFE, 0xCD0, 0xFA0, 0xFFFFF09C, 0x3E8, 0x0)
    Return()

    # Function_7_46D2 end

    def Function_8_46EC(): pass

    label("Function_8_46EC")

    Sleep(1000)
    OP_8F(0xFE, 0xFFFFFC54, 0xFA0, 0xFFFFED7C, 0x3E8, 0x0)
    Return()

    # Function_8_46EC end

    def Function_9_4706(): pass

    label("Function_9_4706")

    Sleep(1100)
    OP_8F(0xFE, 0xFFFFF89E, 0xFA0, 0xFFFFECA0, 0x3E8, 0x0)
    Return()

    # Function_9_4706 end

    def Function_10_4720(): pass

    label("Function_10_4720")

    Sleep(1300)
    OP_8F(0xFE, 0x852, 0xFA0, 0xFFFFF448, 0x3E8, 0x0)
    Return()

    # Function_10_4720 end

    def Function_11_473A(): pass

    label("Function_11_473A")

    Sleep(1400)
    OP_8F(0xFE, 0xBE0, 0xFA0, 0xFFFFF6F0, 0x3E8, 0x0)
    Return()

    # Function_11_473A end

    def Function_12_4754(): pass

    label("Function_12_4754")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_6D(-790, 4000, 1200, 0)
    OP_67(0, 7010, -10000, 0)
    OP_6B(1830, 0)
    OP_6C(315000, 0)
    OP_6E(444, 0)
    SetChrPos(0x109, 150, 4000, -810, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47F3")
    SetChrPos(0xEF, 270, 4000, 1220, 180)
    SetChrPos(0xF0, -370, 4000, -2190, 0)
    SetChrPos(0xF1, 1180, 4000, -2270, 0)
    Jump("loc_4878")

    label("loc_47F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4837")
    SetChrPos(0xF0, 270, 4000, 1220, 180)
    SetChrPos(0xEF, -370, 4000, -2190, 0)
    SetChrPos(0xF1, 1180, 4000, -2270, 0)
    Jump("loc_4878")

    label("loc_4837")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4878")
    SetChrPos(0xF1, 270, 4000, 1220, 180)
    SetChrPos(0xEF, -370, 4000, -2190, 0)
    SetChrPos(0xF0, 1180, 4000, -2270, 0)

    label("loc_4878")

    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #127
        0x105,
        (
            "#1382F#11P各位……\x01",
            "情况我已经从始祖大人那里听说了。\x02\x03",

            "看来要继续前进\x01",
            "似乎需要我的力量对吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x109,
        (
            "#1066F#6P哦……\x01",
            "既然你知道就好办了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x105,
        (
            "#1383F#11P我已经做好准备了。\x02\x03",

            "#1160F打算继续前进的话，\x01",
            "随时都可以加我做同伴。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x109,
        (
            "#1075F#6P明白了。\x02\x03",

            "#1078F做好准备之后，\x01",
            "就回第六星层继续前进吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2B04)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_12_4754 end

    def Function_13_49EB(): pass

    label("Function_13_49EB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_6D(-790, 4000, 1200, 0)
    OP_67(0, 7010, -10000, 0)
    OP_6B(1830, 0)
    OP_6C(315000, 0)
    OP_6E(444, 0)
    SetChrPos(0x109, 150, 4000, -810, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A8A")
    SetChrPos(0xEF, 270, 4000, 1220, 180)
    SetChrPos(0xF0, -370, 4000, -2190, 0)
    SetChrPos(0xF1, 1180, 4000, -2270, 0)
    Jump("loc_4B0F")

    label("loc_4A8A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4ACE")
    SetChrPos(0xF0, 270, 4000, 1220, 180)
    SetChrPos(0xEF, -370, 4000, -2190, 0)
    SetChrPos(0xF1, 1180, 4000, -2270, 0)
    Jump("loc_4B0F")

    label("loc_4ACE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B0F")
    SetChrPos(0xF1, 270, 4000, 1220, 180)
    SetChrPos(0xEF, -370, 4000, -2190, 0)
    SetChrPos(0xF0, 1180, 4000, -2270, 0)

    label("loc_4B0F")

    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #131
        (
            "\x07\x05凯文把琥耀石石碑上\x01",
            "记述的语句向亚妮拉丝作了说明。\x01",
            "　\x02",
        )
    )

    Jump("loc_4B71")

    label("loc_4B71")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #132
        0x10A,
        (
            "#1317F#11P『剑道之少女』……是说我吗！？\x02\x03",

            "#819F唔，那个……\x01",
            "我倒是觉得自己\x01",
            "并没有那么了不起啦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x109,
        (
            "#1077F#6P没关系，不试试看怎么知道呢。\x02\x03",

            "#1078F能陪我们去看看吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x10A,
        (
            "#810F#11P嗯，当然了。\x01",
            "这点小事倒不要紧……\x02\x03",

            "#1310F那么我们就尽快\x01",
            "前往那块石碑试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2B0B)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_13_49EB end

    def Function_14_4CC1(): pass

    label("Function_14_4CC1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_6D(-790, 4000, 1200, 0)
    OP_67(0, 7010, -10000, 0)
    OP_6B(1830, 0)
    OP_6C(315000, 0)
    OP_6E(444, 0)
    SetChrPos(0x109, 150, 4000, -810, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D60")
    SetChrPos(0xEF, 270, 4000, 1220, 180)
    SetChrPos(0xF0, -370, 4000, -2190, 0)
    SetChrPos(0xF1, 1180, 4000, -2270, 0)
    Jump("loc_4DE5")

    label("loc_4D60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DA4")
    SetChrPos(0xF0, 270, 4000, 1220, 180)
    SetChrPos(0xEF, -370, 4000, -2190, 0)
    SetChrPos(0xF1, 1180, 4000, -2270, 0)
    Jump("loc_4DE5")

    label("loc_4DA4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DE5")
    SetChrPos(0xF1, 270, 4000, 1220, 180)
    SetChrPos(0xEF, -370, 4000, -2190, 0)
    SetChrPos(0xF0, 1180, 4000, -2270, 0)

    label("loc_4DE5")

    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #135
        (
            "\x07\x05凯文把红耀石石碑上\x01",
            "记述的语句向理查德作了说明。\x01",
            "　\x02",
        )
    )

    Jump("loc_4E45")

    label("loc_4E45")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #136
        0x10C,
        (
            "#113F#11P『剑圣的继承者』……我吗？\x02\x03",

            "#116F可、可是……\x02\x03",

            "#115F……啊，也罢。\x01",
            "先不说是否有继承的资格，\x01",
            "看来这里只有我符合这个条件。\x02\x03",

            "#110F周游道的石碑吗……\x01",
            "去试试看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x109,
        "#1060F#6P嗯，那就拜托你了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2B17)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_14_4CC1 end

    def Function_15_4F53(): pass

    label("Function_15_4F53")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_6D(-790, 4000, 1200, 0)
    OP_67(0, 7010, -10000, 0)
    OP_6B(1830, 0)
    OP_6C(315000, 0)
    OP_6E(444, 0)
    SetChrPos(0x109, 150, 4000, -810, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FF2")
    SetChrPos(0xEF, 270, 4000, 1220, 180)
    SetChrPos(0xF0, -370, 4000, -2190, 0)
    SetChrPos(0xF1, 1180, 4000, -2270, 0)
    Jump("loc_5077")

    label("loc_4FF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5036")
    SetChrPos(0xF0, 270, 4000, 1220, 180)
    SetChrPos(0xEF, -370, 4000, -2190, 0)
    SetChrPos(0xF1, 1180, 4000, -2270, 0)
    Jump("loc_5077")

    label("loc_5036")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5077")
    SetChrPos(0xF1, 270, 4000, 1220, 180)
    SetChrPos(0xEF, -370, 4000, -2190, 0)
    SetChrPos(0xF0, 1180, 4000, -2270, 0)

    label("loc_5077")

    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #138
        (
            "\x07\x05凯文把黑耀石石碑上\x01",
            "记述的语句向约修亚作了说明。\x01",
            "　\x02",
        )
    )

    Jump("loc_50D7")

    label("loc_50D7")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #139
        0x102,
        (
            "#1503F#11P……………………………\x02\x03",

            "#1513F……看来，『黑骑士』\x01",
            "就在这最后的领域中啊。\x02\x03",

            "#1514F而且不知为何，\x01",
            "故意点了我的名字。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x109,
        (
            "#1065F#6P啊啊……看来是这样。\x02\x03",

            "#1063F约修亚。\x01",
            "你打算怎么办呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x102,
        (
            "#1505F#11P那还用说……\x01",
            "当然是接受招待了。\x02\x03",

            "#1500F做好准备之后\x01",
            "就赶快去周游道的\x01",
            "那个石碑前看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5275")

    ChrTalk(    #142
        0x101,
        "#1026F#6P约修亚……\x02",
    )

    CloseMessageWindow()

    label("loc_5275")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52A4")

    ChrTalk(    #143
        0x10B,
        "#215F#6P哎，那个……\x02",
    )

    CloseMessageWindow()

    label("loc_52A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52D2")

    ChrTalk(    #144
        0x105,
        "#1163F#6P约修亚……\x02",
    )

    CloseMessageWindow()

    label("loc_52D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5301")

    ChrTalk(    #145
        0x107,
        "#063F#6P哥、哥哥……\x02",
    )

    CloseMessageWindow()

    label("loc_5301")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5335")

    ChrTalk(    #146
        0x110,
        "#1307F#6P…………可以吗？\x02",
    )

    CloseMessageWindow()

    label("loc_5335")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_53D7")

    ChrTalk(    #147
        0x102,
        (
            "#1513F#11P……没关系。\x01",
            "不管发生什么都无所谓。\x02\x03",

            "#1500F总之……\x01",
            "现在只需考虑如何前进。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53D7")

    OP_A2(0x2B22)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_15_4F53 end

    def Function_16_53E2(): pass

    label("Function_16_53E2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_82(0x7, 0x0)
    OP_E5(0x2, 0xFF, 0x13, 500)
    LoadEffect(0x0, "map\\mp263_05.eff")
    LoadEffect(0x1, "map\\mp259_01.eff")
    OP_D2(0x260350, 0x260355, 0x13)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x22, -1890, 4500, 1230, 135)
    OP_9F(0x22, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x22, 0x4)
    SetChrFlags(0x22, 0x4)

    def lambda_545A():

        label("loc_545A")

        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_545A")

    QueueWorkItem2(0x22, 3, lambda_545A)
    SetChrPos(0x109, 690, 4000, 250, 180)
    SetChrPos(0x10F, 1580, 4000, 960, 180)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1D, 850, 4000, -2160, 0)
    SetChrPos(0x15, -350, 4000, -2200, 0)
    SetChrPos(0x1F, 2100, 4000, -2050, 0)
    SetChrPos(0x11, 2610, 4000, -3630, 0)
    SetChrPos(0x12, 1950, 4000, -4980, 0)
    SetChrPos(0x13, 630, 4000, -5130, 0)
    SetChrPos(0x14, 4400, 4000, -4590, 315)
    SetChrPos(0x16, 1220, 4000, -3520, 0)
    SetChrPos(0x18, -10, 4000, -3630, 0)
    SetChrPos(0x19, -920, 4000, -4200, 0)
    SetChrPos(0x1A, 3590, 4000, -1950, 315)
    SetChrPos(0x1B, 5170, 4000, -3440, 315)
    SetChrPos(0x1C, 3920, 4000, -3280, 315)
    SetChrPos(0x1E, 3340, 4000, -5090, 0)
    OP_6D(250, 4000, -500, 0)
    OP_67(0, 5280, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(315000, 0)
    OP_6E(362, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("凯文")

    AnonymousTalk(    #148
        (
            "\x07\x00──以上就是\x01",
            "这次事件的大致情况。\x02",
        )
    )

    Jump("loc_563C")

    label("loc_563C")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_1D(0xC8)

    def lambda_5650():
        OP_6B(2430, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_5650)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Sleep(300)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("伙伴们")

    AnonymousTalk(    #149
        "\x07\x00……………………………………\x02",
    )

    Jump("loc_56B0")

    label("loc_56B0")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #150
        0x109,
        (
            "#1067F#11P简单来说……\x01",
            "我就是这次事件的元凶。\x02\x03",

            "各位被卷入这次事件，\x01",
            "实在是对不起。\x02\x03",

            "#1065F……抱歉。\x01",
            "我的本意不是想吓你们的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x1D,
        (
            "#1007F#6P这、这个……\x02\x03",

            "#1008F老实说，\x01",
            "我不明白凯文先生为什么会\x01",
            "感到这样过意不去……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x109,
        "#1079F#11P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x13,
        (
            "#278F#6P听你刚才的叙述，\x01",
            "失去了『环』的『影之国』\x01",
            "寻求『主人』是必然的事……\x02\x03",

            "#277F这样的话，\x01",
            "就算没有你的出现，\x01",
            "也还是会发生这种程度的事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x18,
        (
            "#1545F#6P呵呵，的确是啊。\x02\x03",

            "#1540F到时恐怕会有其他什么人被选中，\x01",
            "然后会诞生出反映那个人的\x01",
            "心理创伤的『影之国』吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x13,
        (
            "#276F#6P……一想到万一是\x01",
            "你被选中的情形，\x01",
            "我就觉得毛骨悚然了。\x02\x03",

            "光从这点来说也是很侥幸的事呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5976():
        OP_6D(-250, 4000, -1000, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_5976)
    OP_8C(0x18, 135, 400)
    WaitChrThread(0xEE, 0x0)

    ChrTalk(    #156
        0x18,
        (
            "#1544F#5P真失礼……\x01",
            "你也多少信任我一下嘛。\x02\x03",

            "#1547F至少让我把这里\x01",
            "变成能让在场的各位举行\x01",
            "酒池肉林的宴会的世界吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x19, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1D, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x11, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1E, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1F, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x13, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    def lambda_5B86():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5B86)

    def lambda_5B94():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_5B94)
    Sleep(50)

    def lambda_5BA7():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_5BA7)

    def lambda_5BB5():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5BB5)
    Sleep(50)

    def lambda_5BC8():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_5BC8)

    def lambda_5BD6():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5BD6)
    Sleep(50)

    def lambda_5BE9():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_5BE9)

    def lambda_5BF7():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5BF7)
    Sleep(50)

    def lambda_5C0A():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_5C0A)

    def lambda_5C18():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_5C18)
    Sleep(50)

    def lambda_5C2B():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_5C2B)
    OP_8C(0x1F, 225, 400)

    ChrTalk(    #157
        0x13,
        "#274F#6P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x11,
        "#065F#12P哇、哇啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x1C,
        "#057F#12P这家伙……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x1D,
        "#1019F#11P你、你啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x14,
        "#214F#12P别、别开玩笑了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x1B,
        (
            "#1525F#12P唉……\x01",
            "真没风度啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x109,
        (
            "#1840F#11P我、我说……\x01",
            "是这样的吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1F, 0, 400)
    Sleep(300)

    ChrTalk(    #164
        0x1F,
        (
            "#263F#6P哎，我也不是\x01",
            "在帮哥哥说话啦……\x02\x03",

            "#1305F从某种意义上，\x01",
            "『影之国』选中了哥哥你，\x01",
            "对我们来说也许是件很幸运的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_5E1F():
        OP_6D(250, 4000, -500, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_5E1F)

    def lambda_5E37():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5E37)
    Sleep(50)

    def lambda_5E4A():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5E4A)

    def lambda_5E58():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_5E58)
    Sleep(50)

    def lambda_5E6B():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_5E6B)

    def lambda_5E79():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5E79)
    Sleep(50)

    def lambda_5E8C():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_5E8C)

    def lambda_5E9A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5E9A)
    Sleep(50)

    def lambda_5EAD():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_5EAD)

    def lambda_5EBB():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5EBB)
    Sleep(50)

    def lambda_5ECE():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_5ECE)

    def lambda_5EDC():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_5EDC)
    Sleep(50)

    def lambda_5EEF():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_5EEF)

    def lambda_5EFD():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_5EFD)
    Sleep(50)
    Sleep(500)
    WaitChrThread(0xEE, 0x0)

    ChrTalk(    #165
        0x109,
        "#1079F#5P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x10F,
        "#1934F#11P什么……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x1F,
        (
            "#263F#6P哥哥的『圣痕』有着\x01",
            "相当强的支配力呢。\x02\x03",

            "以至于连扭曲了的『影之国』\x01",
            "都能保持着这样的秩序。\x02\x03",

            "#1306F但是，如果这个空间\x01",
            "是源自其他人的心理创伤的话，\x01",
            "能保持这样的秩序吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x109,
        "#1063F#5P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x15,
        (
            "#1505F#5P无法制御住混沌，\x01",
            "『影之国』就会暴走……\x02\x03",

            "#1500F这种可能性也是有的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1F, 270, 400)
    Sleep(300)

    ChrTalk(    #170
        0x1F,
        (
            "#269F#12P嘻嘻，不愧是约修亚。\x02\x03",

            "在那种情况下，\x01",
            "也许会有更多人被卷入进来吧。\x02\x03",

            "#261F不过，那样也许就变成\x01",
            "更有趣的茶会了，不是吗? \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x11,
        "#067F#6P玲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x1D,
        (
            "#1016F#5P那、那个还是\x01",
            "不必了吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x19,
        "#573F#5P哈哈……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x19, 0, 400)
    Sleep(300)

    ChrTalk(    #174
        0x19,
        (
            "#070F#6P嗯，这种情况下\x01",
            "也没必要独自忧伤了吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_61EC():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_61EC)
    Sleep(50)

    def lambda_61FF():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_61FF)
    Sleep(50)

    def lambda_6212():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6212)
    Sleep(50)

    def lambda_6225():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_6225)
    Sleep(50)

    def lambda_6238():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_6238)
    Sleep(50)

    def lambda_624B():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_624B)
    Sleep(50)

    def lambda_625E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_625E)
    Sleep(500)

    ChrTalk(    #175
        0x1E,
        (
            "#119F#6P虽说立场不同,人生道路也不同……\x02\x03",

            "#111F不过，在现在的这种情况下\x01",
            "我们已经是同命相连了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x1A,
        (
            "#816F#6P对对。\x01",
            "困难的时候就要互相帮助。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x16,
        (
            "#1383F#6P而且关于『辉之环』的问题\x01",
            "本来就出在利贝尔王国。\x02\x03",

            "#1382F倒不如说凯文先生\x01",
            "也许是被我们卷进来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x12,
        (
            "#179F#6P就是这样，凯文神父。\x02\x03",

            "#170F请和之前一样，\x01",
            "继续担任我们的向导吧。\x02\x03",

            "也为了把半年前的那个事件\x01",
            "从真正意义上进行解决。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x10F,
        "#1932F#11P……各位…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x109,
        (
            "#1846F#11P#40W哈哈……\x02\x03",

            "#1844F真是的……\x01",
            "你们可真是笨蛋呀。\x02\x03",

            "每一个都是这样，\x01",
            "也太老好人了吧……\x02\x03",

            "#1845F我可是从头到尾\x01",
            "都在利用你们的哦……\x02\x03",

            "…………为什么会这样……………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x109, 19)
    SetChrSubChip(0x109, 0)
    OP_0D()
    OP_9E(0x109, 0xF, 0x0, 0x12C, 0x7D0)
    Sleep(500)

    ChrTalk(    #181
        0x10F,
        "#1946F#11P凯文……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x15,
        "#1500F#6P凯文先生……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x1D,
        (
            "#1016F#6P哈哈……\x01",
            "人嘛，就是要想得开。\x02\x03",

            "#1006F和我们牵扯上关系，\x01",
            "也算是凯文先生你倒霉吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_65FB():
        OP_6D(900, 4000, -1500, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_65FB)
    OP_44(0x109, 0x0)
    WaitChrThread(0xEE, 0x1)

    ChrTalk(    #184
        0x14,
        (
            "#210F#6P哼哼，与其说是『我们』，\x01",
            "其实最出头的不正是你吗？\x02\x03",

            "#211F又蛮横，又爱多管闲事，\x01",
            "就算人家逃跑也要拼命追上去。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1D, 135, 600)
    Sleep(200)

    ChrTalk(    #185
        0x1D,
        "#1019F#5P你、你说什么～！？\x02",
    )

    CloseMessageWindow()

    def lambda_66D7():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_66D7)
    Sleep(50)

    def lambda_66EA():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_66EA)
    Sleep(50)

    def lambda_66FD():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_66FD)
    Sleep(50)

    def lambda_6710():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_6710)
    Sleep(50)

    def lambda_6723():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_6723)
    Sleep(50)

    def lambda_6736():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_6736)
    Sleep(50)

    def lambda_6749():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_6749)
    Sleep(50)

    def lambda_675C():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_675C)
    Sleep(400)

    ChrTalk(    #186
        0x15,
        "#1514F#5P……哈哈。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x1B,
        (
            "#1521F#12P嗯，\x01",
            "也许确实可以这么说呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x1F,
        "#268F#12P嘻嘻，玲也有同感。\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #189
        0x11,
        (
            "#560F#6P嗯，那个……\x02\x03",

            "#067F我觉得那正是\x01",
            "姐姐的厉害之处……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x1A,
        (
            "#811F#12P嗯嗯。\x02\x03",

            "#1310F归根到底，\x01",
            "我们都是受了\x01",
            "艾丝蒂尔的影响呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x1D,
        "#1007F#5P真、真是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x1C,
        (
            "#051F#12P嗯，\x01",
            "我们的确可以称得上是笨蛋啊。\x02\x03",

            "明明面临这么严峻的状况，\x01",
            "却没有被逼到尽头的感觉。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #193
        0x18,
        (
            "#1540F#5P呵呵，正因为有这样的魄力，\x01",
            "我们才能聚集在这里的呢。\x02\x03",

            "#1541F照现在这种气势，\x01",
            "我觉得连推翻埃雷波尼亚政府\x01",
            "这样的事情都能做得出来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x13,
        "#274F#6P你又说这种奇怪的话了……\x02",
    )

    CloseMessageWindow()

    def lambda_6A1F():
        OP_6D(250, 4000, -500, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_6A1F)
    WaitChrThread(0xEE, 0x0)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #195
        0x109,
        "#1846F#11P哈哈……我投降了。\x02",
    )

    CloseMessageWindow()

    def lambda_6A7A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6A7A)

    def lambda_6A88():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_6A88)
    Sleep(50)

    def lambda_6A9B():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_6A9B)
    Sleep(50)

    def lambda_6AAE():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_6AAE)

    def lambda_6ABC():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6ABC)
    Sleep(50)

    def lambda_6ACF():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_6ACF)

    def lambda_6ADD():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6ADD)
    Sleep(50)

    def lambda_6AF0():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_6AF0)

    def lambda_6AFE():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6AFE)
    Sleep(50)

    def lambda_6B11():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_6B11)

    def lambda_6B1F():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_6B1F)
    Sleep(50)

    def lambda_6B32():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_6B32)

    def lambda_6B40():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_6B40)
    Sleep(500)

    ChrTalk(    #196
        0x109,
        (
            "#1065F#11P……我再一次………\x02\x03",

            "#1840F这次是真正意义上的\x01",
            "请多关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x1D,
        "#1017F#6P嗯……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x15,
        (
            "#1513F#6P彼此彼此……\x01",
            "请你多关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x109,
        (
            "#1065F#11P总而言之……\x01",
            "我们应该做的事\x01",
            "已经很清楚了。\x02\x03",

            "#1063F『影之王』……\x01",
            "露菲娜·亚尔珍特的行为\x01",
            "必须由我们来制止。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x10F,
        "#1935F#11P………嗯………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x12,
        "#176F#6P当然……就该这样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x18,
        (
            "#1551F#6P不过，凯文先生。\x02\x03",

            "#1542F在你们掉入的『炼狱』里\x01",
            "并没有找到她的行踪吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D7D")

    ChrTalk(    #203
        0x1D,
        (
            "#1007F#6P凯文先生，你们掉下去之后，\x01",
            "她就消失了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7106")

    label("loc_6D7D")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DCF")

    ChrTalk(    #204
        0x15,
        (
            "#1503F#6P凯文先生和莉丝小姐掉下去后，\x01",
            "她就立刻消失了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7106")

    label("loc_6DCF")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E18")

    ChrTalk(    #205
        0x14,
        (
            "#413F#6P你们两个掉下去后，\x01",
            "她就当场消失了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7106")

    label("loc_6E18")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E5F")

    ChrTalk(    #206
        0x1F,
        (
            "#268F#6P哥哥你们掉下去后，\x01",
            "她就立刻消失了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7106")

    label("loc_6E5F")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EAC")

    ChrTalk(    #207
        0x11,
        (
            "#561F#6P凯文哥哥他们掉下去后，\x01",
            "她就那样消失了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7106")

    label("loc_6EAC")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EFE")

    ChrTalk(    #208
        0x1A,
        (
            "#1316F#6P在凯文先生他们掉下去之后，\x01",
            "她就那样消失了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7106")

    label("loc_6EFE")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F50")

    ChrTalk(    #209
        0x16,
        (
            "#1163F#6P在凯文先生他们掉下去之后，\x01",
            "她就那样消失了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7106")

    label("loc_6F50")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F9A")

    ChrTalk(    #210
        0x1B,
        (
            "#1532F#6P你们两个掉下去后，\x01",
            "她就那样消失了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7106")

    label("loc_6F9A")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FE5")

    ChrTalk(    #211
        0x1C,
        (
            "#552F#6P你们两个掉下去之后，\x01",
            "她就那样消失了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7106")

    label("loc_6FE5")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_702E")

    ChrTalk(    #212
        0x19,
        (
            "#572F#6P你们两个掉下去之后，\x01",
            "她当时就消失了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7106")

    label("loc_702E")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7077")

    ChrTalk(    #213
        0x12,
        (
            "#175F#6P你们两个掉下去之后，\x01",
            "她就立刻消失了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7106")

    label("loc_7077")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70C0")

    ChrTalk(    #214
        0x13,
        (
            "#276F#6P你们两个掉下去之后，\x01",
            "她接着就消失了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7106")

    label("loc_70C0")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7106")

    ChrTalk(    #215
        0x1E,
        (
            "#116F#6P你们两个掉下去之后，\x01",
            "她马上就消失了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7106")


    ChrTalk(    #216
        0x109,
        "#1065F#11P……这样啊………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x10F,
        (
            "#1935F#11P至少……\x01",
            "在那个地方\x01",
            "完全感觉不到姐姐的气息。\x02\x03",

            "#1942F如果在的话……\x01",
            "我想她绝对会出现的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x109,
        (
            "#1840F#5P……是啊。\x02\x03",

            "#1841F不过这样一来，\x01",
            "姐姐到底去哪里了呢……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #219
        (
            "\x07\x0C──这个问题\x01",
            "我想我能回答你们。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x19, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_73ED():
        OP_6D(-1620, 4000, 1500, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_73ED)

    def lambda_7405():
        OP_67(0, 3610, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_7405)

    def lambda_741D():
        OP_6B(2800, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_741D)

    def lambda_742D():
        OP_6E(373, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_742D)

    def lambda_743D():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_743D)
    Sleep(100)

    def lambda_7450():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_7450)
    Sleep(100)

    def lambda_7463():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7463)
    Sleep(100)
    OP_8C(0x1F, 315, 400)
    WaitChrThread(0xEE, 0x0)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0x22, 0, 800, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_22(0x99, 0x0, 0x64)

    def lambda_74C6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xB4, 0x320)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_74C6)
    PlayEffect(0x1, 0x7, 0x22, 0, 900, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x22, 0x1)
    OP_82(0x0, 0x2)
    Sleep(1000)

    ChrTalk(    #220
        0x16,
        "#1164F#6P始祖大人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x109,
        (
            "#1840F#6P赛雷斯托小姐……\x02\x03",

            "#1065F刚才真的是\x01",
            "谢谢你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x10F,
        (
            "#1937F#12P……不然的话，\x01",
            "我想我和凯文\x01",
            "不会像现在这样平安无事。\x02\x03",

            "#1946F真是……\x01",
            "十分感谢您。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x22,
        (
            "\x07\x0C#1616F#5P呵呵，没关系。\x02\x03",

            "我和大家一样，\x01",
            "都处在『影之王』的囚禁之下……\x02\x03",

            "#1611F请让我作为同伴的一份子\x01",
            "尽力帮忙吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x109,
        (
            "#1075F#6P哈哈……谢谢。\x02\x03",

            "#1063F先别说这些……\x01",
            "你能回答我们的疑问吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x22,
        (
            "\x07\x0C#1615F#5P嗯……\x02\x03",

            "#1610F『影之王』的居所\x01",
            "我已经找到了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x19, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #226
        0x109,
        "#1064F#6P哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x10F,
        "#1934F#12P真、真的吗……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x16,
        (
            "#1382F#6P难道……\x01",
            "你之前一直\x01",
            "在调查这个吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x22,
        (
            "\x07\x0C#1616F#5P嗯嗯……\x02\x03",

            "#1612F在调查『第七星层』的过程中\x01",
            "我已经大致掌握了\x01",
            "『影之国』现在的全貌了。\x02\x03",

            "『影之王』现在\x01",
            "就在『星层』的外侧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x10F,
        "#1942F#12P『星层』的外侧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x11,
        (
            "#065F#6P那、那里是\x01",
            "什么地方呀？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x22,
        (
            "\x07\x0C#1612F#5P『星层』是『影之王』\x01",
            "在『影之国』的中心\x01",
            "建造的多层构造。\x02\x03",

            "在这个构造的外侧，\x01",
            "『影之国』是继续向外延伸的。\x02\x03",

            "#1615F虽然现在那里只是\x01",
            "以类似空旷荒野\x01",
            "那样的形态被放置着……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x1B,
        "#1522F#6P什么也没有的荒野……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x1C,
        (
            "#551F#6P唔……\x01",
            "真是相当模糊的回答呀。\x02\x03",

            "#555F也就是说还没找到\x01",
            "『影之王』具体的所在吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x22,
        (
            "\x07\x0C#1615F#5P不，大致的地点已经判明了。\x02\x03",

            "#1612F不过有个问题。\x02\x03",

            "那个荒野……\x01",
            "简直是无边无际的广阔。\x02\x03",

            "恐怕……\x01",
            "规模大概可以和一片大陆相比。\x07\x00\x02",
        )
    )

    Jump("loc_7C34")

    label("loc_7C34")

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x19, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #236
        0x1D,
        "#1005F#6P你、你说什么～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x15,
        (
            "#1502F#6P这真是……\x01",
            "相当严峻啊。\x02\x03",

            "#1503F徒步走过去的话\x01",
            "不知道要用几个月了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x1E,
        (
            "#112F#6P唔……\x01",
            "没有其它的移动手段吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x22,
        (
            "\x07\x0C#1615F#5P是啊……\x02\x03",

            "#1613F……以我能使用的力量来看，\x01",
            "确实是很难啊。\x02\x03",

            "就算用『石碑』路标，\x01",
            "也是不能传送到\x01",
            "离这里太远的地方的……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x109,
        (
            "#1841F#6P如果我们徒步行走的话……\x01",
            "在不能使用『方石』的情况下，\x01",
            "补给也会跟不上的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x10F,
        (
            "#1935F#12P准备几十天的干粮……\x01",
            "实在是太不现实了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x19,
        (
            "#075F#6P唔……这可真麻烦啊。\x02\x03",

            "#072F对方不来这里的话，\x01",
            "我们就没什么办法了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_62(0x1C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_803F():
        OP_6D(-670, 4000, 450, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_803F)

    def lambda_8057():
        OP_67(0, 3960, -10000, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_8057)
    OP_8C(0x1C, 270, 400)
    WaitChrThread(0xEE, 0x0)
    Sleep(300)

    ChrTalk(    #243
        0x1C,
        (
            "#052F怎么#12P……\x01",
            "想到什么了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11)
    Sleep(300)
    OP_8C(0x11, 90, 400)
    Sleep(300)

    ChrTalk(    #244
        0x11,
        (
            "#067F#5P啊，是的，那个……\x02\x03",

            "#560F我在想，\x01",
            "能不能使用『埃尔赛尤号』。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x22, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x19, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_829D():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_829D)

    def lambda_82AB():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_82AB)
    Sleep(50)

    def lambda_82BE():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_82BE)

    def lambda_82CC():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_82CC)
    Sleep(50)

    def lambda_82DF():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_82DF)
    Sleep(50)

    def lambda_82F2():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_82F2)

    def lambda_8300():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_8300)
    Sleep(50)

    def lambda_8313():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_8313)

    def lambda_8321():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_8321)
    Sleep(50)

    def lambda_8334():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_8334)

    def lambda_8342():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_8342)
    Sleep(400)

    ChrTalk(    #245
        0x1C,
        "#055F#12P什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x12,
        (
            "#173F#6P『埃尔赛尤号』……\x01",
            "是说停在『第一星层』的那个假货？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 180, 400)
    Sleep(300)

    ChrTalk(    #247
        0x11,
        (
            "#563F#11P嗯，是的。\x02\x03",

            "#560F唔，这个『影之国』\x01",
            "是能够反映人的愿望的吧？\x02\x03",

            "虽然那个『埃尔赛尤号』\x01",
            "只不过是个伪造品……\x02\x03",

            "但包括它的形状和构造在内，\x01",
            "大家应该很熟悉了，\x01",
            "我想有这样的印象已经足够了。\x02\x03",

            "大家一起祈祷的话\x01",
            "也许能开动起来……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x1D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x22, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x19, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x16, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x18, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x1C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x1A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x1B, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x1F, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x1E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_62(0x11, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x11, 0, 400)
    Sleep(300)
    OP_8C(0x11, 90, 400)
    OP_63(0x109)
    OP_63(0x10F)
    OP_63(0x1D)
    OP_63(0x15)
    OP_63(0x22)
    OP_63(0x19)
    OP_63(0x12)
    OP_63(0x16)
    OP_63(0x13)
    OP_63(0x18)
    OP_63(0x14)
    OP_63(0x1C)
    OP_63(0x1A)
    OP_63(0x1B)
    OP_63(0x1F)
    OP_63(0x1E)
    Sleep(300)

    ChrTalk(    #248
        0x11,
        (
            "#065F#5P啊，那个……\x01",
            "果然不行吗！？\x02\x03",

            "#562F光靠祈祷就能开动的话，\x01",
            "也太不符合技术人员的常识了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x1F,
        (
            "#263F#11P……不，提妲。\x02\x03",

            "#265F也许你想到了个\x01",
            "非常好的主意。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x11, 0, 400)

    ChrTalk(    #250
        0x11,
        "#064F#6P哎哎！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x109,
        (
            "#1060F#11P的确，\x01",
            "印象强烈的东西\x01",
            "在这个『影之国』里很容易得到再现。\x02\x03",

            "先不说尤莉亚小姐，\x01",
            "提妲对船的构造也是非常熟悉的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x15,
        (
            "#1513F#5P……也许不是不可能的事。\x02\x03",

            "#1501F『黑色方舟』都被再现了出来，\x01",
            "说明飞艇应该没问题的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8872():
        OP_6D(-1620, 4000, 1500, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_8872)

    def lambda_888A():
        OP_67(0, 3610, -10000, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_888A)
    OP_8C(0x1D, 0, 400)
    WaitChrThread(0xEE, 0x0)

    ChrTalk(    #253
        0x1D,
        "#1018F#6P赛雷斯托先祖，您觉得怎么样！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x22,
        (
            "\x07\x0C#1615F#5P……………………………………\x02\x03",

            "#1612F我记得你们在\x01",
            "登上『利贝尔方舟』的时候，\x01",
            "曾经使用过那艘船吧。\x02\x03",

            "那样的话，\x01",
            "就努力回想当时的印象……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x22, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    def lambda_89A1():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_89A1)

    def lambda_89AF():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_89AF)
    Sleep(50)

    def lambda_89C2():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_89C2)

    def lambda_89D0():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_89D0)
    Sleep(50)

    def lambda_89E3():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_89E3)

    def lambda_89F1():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_89F1)
    Sleep(50)

    def lambda_8A04():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_8A04)

    def lambda_8A12():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_8A12)
    Sleep(50)

    def lambda_8A25():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_8A25)

    def lambda_8A33():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_8A33)
    Sleep(50)

    def lambda_8A46():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_8A46)

    def lambda_8A54():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_8A54)
    Sleep(1700)
    OP_63(0x22)
    Sleep(500)

    ChrTalk(    #255
        0x22,
        (
            "\x07\x0C#1616F#5P……嗯，我想有可能。\x02\x03",

            "#1611F你们所有人都乘上来的话……\x01",
            "『白翼』一定会苏醒的。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x19, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #256
        0x109,
        "#1078F#6P真、真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x11,
        "#067F#6P真不敢相信……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x1F,
        "#261F#5P嘿嘿，提妲立大功了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x1D,
        (
            "#1001F#5P啊哈哈……\x01",
            "很厉害嘛，提妲！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #260
        0x14,
        (
            "#415F#6P等、等一下……\x02\x03",

            "那么，停在王都港口的\x01",
            "『山猫号』也能动了！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x15,
        "#1500F#5P对了，还有那个。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x22,
        (
            "\x07\x0C#1615F#5P那个嘛……\x02\x03",

            "#1610F大家对那艘飞艇的\x01",
            "熟悉程度如何？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x14,
        "#216F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x15,
        (
            "#1503F#6P乘过那艘船的，\x01",
            "大概只有……她和我了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x1D,
        (
            "#1015F#6P我和雪拉姐，还有奥利维尔\x01",
            "也有潜入船舱的经验……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x1B,
        "#1527F#6P哦，是在定期船被劫持事件的时候。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x18,
        (
            "#1541F#6P呵呵……\x01",
            "现在想起来还真是美好的回忆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x22,
        (
            "\x07\x0C#1613F#5P光是这点的话，\x01",
            "要动起来还是有点困难……\x02\x03",

            "#1610F我想还是优先\x01",
            "让『白翼』苏醒吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x14,
        "#413F#6P是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x12,
        (
            "#179F#6P总之……\x01",
            "这是求之不得的事情。\x02\x03",

            "#170F我们快点做好准备\x01",
            "去『埃尔赛尤号』那里吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x1C,
        "#051F#6P嗯……是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x1E,
        (
            "#111F#6P要这么决定的话……\x01",
            "就该忙起来了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x22,
        (
            "\x07\x0C#1615F#5P不过有一点……\x02\x03",

            "#1613F如果要乘坐『白翼』\x01",
            "出发前往『影之王』\x01",
            "那里的话……\x02\x03",

            "#1612F就不能再回到\x01",
            "这个『庭院』来了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x10F,
        "#1942F#12P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x16,
        (
            "#1163F#6P用『方石』的传送……\x01",
            "也办不到吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x22,
        (
            "\x07\x0C#1612F#5P嗯，『方石』的传送功能\x01",
            "离开这个『庭院』太远的话\x01",
            "就无法运作了。\x02\x03",

            "#1615F如果要出发的话……\x01",
            "请一定要做好准备。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x1D,
        "#1025F#6P是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x19,
        (
            "#573F#6P机会不多，\x01",
            "也许让大家都\x01",
            "重新锻炼一下比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x1A,
        (
            "#819F#6P嗯，是呀。\x02\x03",

            "#1310F为了不拖后腿，\x01",
            "要做点准备活动才行！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x18,
        (
            "#1545F#6P这也是打开各地的『门』的\x01",
            "最后机会了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_92A9():
        OP_6D(-150, 4000, 480, 1200)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_92A9)

    def lambda_92C1():
        OP_67(0, 4450, -10000, 1200)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_92C1)

    def lambda_92D9():
        OP_6B(2620, 1200)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_92D9)

    def lambda_92E9():
        OP_6E(346, 1200)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_92E9)

    def lambda_92F9():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_92F9)
    Sleep(100)
    OP_8C(0x10F, 180, 400)
    WaitChrThread(0xEE, 0x0)
    Sleep(300)

    ChrTalk(    #281
        0x109,
        (
            "#1075F#11P这样的话……\x01",
            "我也暂时不必当向导了。\x02\x03",

            "#1060F如果有必要的话，我可以教你们\x01",
            "『方石』和『星杯手册』的使用方法。\x02\x03",

            "#1078F各位，为了不留下遗憾，\x01",
            "我们尽全力加油吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("全体")

    AnonymousTalk(    #282
        "\x07\x00#5S 是！\x02",
    )

    Jump("loc_940B")

    label("loc_940B")

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    def lambda_942E():
        OP_6B(3300, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_942E)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0xEE, 0x0)
    OP_20(0x7D0)
    Sleep(2000)
    OP_AD(0x2400EA, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    OP_1D(0xD5)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_84(0x0)
    OP_A2(0x2C20)
    OP_E5(0x2, 0xFF, 0x13, 700)
    OP_28(0x3D, 0x1, 0x10)
    OP_28(0x3D, 0x1, 0x20)
    OP_28(0x3D, 0x1, 0x40)
    OP_28(0x3D, 0x1, 0x80)
    OP_28(0x3D, 0x4, 0x10)
    OP_28(0x3D, 0x4, 0x20)
    OP_28(0x3E, 0x4, 0x4)
    OP_28(0x3E, 0x4, 0x8)
    OP_28(0x3E, 0x1, 0x1)
    OP_28(0x3E, 0x1, 0x2)
    OP_28(0x3E, 0x1, 0x4)
    OP_28(0x3E, 0x1, 0x8)
    OP_28(0x3E, 0x1, 0x10)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_DB(0x0, 0x8)
    ClearParty()
    OP_DD(0x1, 0x0, 0x0, 0, 0, 0, 0)
    FadeToDark(0, 0, -1)
    OP_C0(0x20, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    OP_6D(250, 4000, -3050, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x0, 250, 4000, -3050, 180)
    SetChrPos(0x1, 250, 4000, -3050, 180)
    SetChrPos(0x2, 250, 4000, -3050, 180)
    SetChrPos(0x3, 250, 4000, -3050, 180)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    Call(0, 5)
    SetChrChipByIndex(0x22, 0)
    SetChrSubChip(0x22, 0)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x22, -2100, 4500, 3610, 135)

    def lambda_9675():

        label("loc_9675")

        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_9675")

    QueueWorkItem2(0x22, 3, lambda_9675)
    OP_9F(0x22, 0xFF, 0xFF, 0xFF, 0xB4, 0x0)
    LoadEffect(0x7, "map\\mp259_01.eff")
    PlayEffect(0x7, 0x7, 0x22, 0, 800, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_16_53E2 end

    def Function_17_96EB(): pass

    label("Function_17_96EB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9727")
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0x7D0)
    Sleep(1000)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0x7D0)
    Sleep(1500)
    Jump("Function_17_96EB")

    label("loc_9727")

    Return()

    # Function_17_96EB end

    SaveToFile()

Try(main)
