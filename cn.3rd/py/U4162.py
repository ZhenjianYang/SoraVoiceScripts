from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U4162   ._SN',
        MapName             = 'gaiden2',
        Location            = 'U4162.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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


    DeclActor(
        TriggerX            = 5090,
        TriggerZ            = 0,
        TriggerY            = 2190,
        TriggerRange        = 800,
        ActorX              = 5090,
        ActorZ              = 800,
        ActorY              = 2190,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7840,
        TriggerZ            = 4000,
        TriggerY            = 6700,
        TriggerRange        = 800,
        ActorX              = 7840,
        ActorZ              = 5700,
        ActorY              = 6700,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 75860,
        TriggerZ            = 0,
        TriggerY            = -2000,
        TriggerRange        = 800,
        ActorX              = 75860,
        ActorZ              = 1500,
        ActorY              = -2000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 73200,
        TriggerZ            = 0,
        TriggerY            = 710,
        TriggerRange        = 800,
        ActorX              = 73200,
        ActorZ              = 800,
        ActorY              = 710,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 68740,
        TriggerZ            = 0,
        TriggerY            = 7310,
        TriggerRange        = 800,
        ActorX              = 68740,
        ActorZ              = 800,
        ActorY              = 7310,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 73480,
        TriggerZ            = 0,
        TriggerY            = 6420,
        TriggerRange        = 800,
        ActorX              = 73480,
        ActorZ              = 800,
        ActorY              = 6420,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 75820,
        TriggerZ            = 4000,
        TriggerY            = 8010,
        TriggerRange        = 800,
        ActorX              = 75820,
        ActorZ              = 5700,
        ActorY              = 8010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 71960,
        TriggerZ            = 4000,
        TriggerY            = 9290,
        TriggerRange        = 800,
        ActorX              = 71960,
        ActorZ              = 4800,
        ActorY              = 9290,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -20,
        TriggerZ            = 0,
        TriggerY            = 77880,
        TriggerRange        = 800,
        ActorX              = -20,
        ActorZ              = 1700,
        ActorY              = 77880,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -770,
        TriggerZ            = 0,
        TriggerY            = 72650,
        TriggerRange        = 800,
        ActorX              = -770,
        ActorZ              = 800,
        ActorY              = 72650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7000,
        TriggerZ            = 0,
        TriggerY            = 66550,
        TriggerRange        = 1200,
        ActorX              = 7000,
        ActorZ              = 800,
        ActorY              = 66550,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1770,
        TriggerZ            = 0,
        TriggerY            = 66890,
        TriggerRange        = 800,
        ActorX              = 1770,
        ActorZ              = 800,
        ActorY              = 66890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -3790,
        TriggerZ            = 0,
        TriggerY            = 64959,
        TriggerRange        = 800,
        ActorX              = -3790,
        ActorZ              = 800,
        ActorY              = 64959,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_27E",          # 00, 0
        "Function_1_27F",          # 01, 1
        "Function_2_280",          # 02, 2
        "Function_3_400",          # 03, 3
        "Function_4_5AA",          # 04, 4
        "Function_5_71F",          # 05, 5
        "Function_6_840",          # 06, 6
        "Function_7_928",          # 07, 7
        "Function_8_A03",          # 08, 8
        "Function_9_B15",          # 09, 9
        "Function_10_C2D",         # 0A, 10
        "Function_11_D9F",         # 0B, 11
        "Function_12_F6B",         # 0C, 12
        "Function_13_109F",        # 0D, 13
        "Function_14_1191",        # 0E, 14
    )


    def Function_0_27E(): pass

    label("Function_0_27E")

    Return()

    # Function_0_27E end

    def Function_1_27F(): pass

    label("Function_1_27F")

    Return()

    # Function_1_27F end

    def Function_2_280(): pass

    label("Function_2_280")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        (
            "\x07\x05【『四轮之塔』的外壁】\x01",
            "　　　　　　　　　　　年代：七耀历以前？\x01",
            "　　这块朴素的石壁，是从『大崩坏』后所建\x01",
            "的『四轮之塔』上作为研究资料切割出来的。\x01",
            "其上所绘制的纹样是同时代建筑物中的典型，\x01",
            "据说描述的是持杖的祭司，以及展翅的神祗的\x01",
            "身姿。关于其与七耀教会成立之后的代表神格\x01",
            "『空之女神』的关系，各方面的研究仍在进行\x01",
            "中。\x01",
            "　　\x02",
        )
    )

    Jump("loc_3E7")

    label("loc_3E7")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_2_280 end

    def Function_3_400(): pass

    label("Function_3_400")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #1
        (
            "\x07\x05【七耀历１１５０～１２００年\x01",
            "　　　　　　　～导力革命以后的世界～】\x01",
            "　　Ｃ·爱普斯泰恩博士发明导力器后仅仅五\x01",
            "十年。世界以惊人的速度进步着，接连不断地\x01",
            "开拓岀导力技术新的应用领域。堪称其象征的\x01",
            "就是飞艇。\x01",
            "　　\x01",
            "　　利贝尔王国定期飞艇的运航已经成为国民\x01",
            "们习以为常的交通方式，近年来埃雷波尼亚帝\x01",
            "国等其它国家也开始正式引进飞艇制造业，使\x01",
            "得飞艇级的船体逐步实用化。\x01",
            "　　\x02",
        )
    )

    Jump("loc_591")

    label("loc_591")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_3_400 end

    def Function_4_5AA(): pass

    label("Function_4_5AA")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #2
        (
            "\x07\x05【七耀历以前\x01",
            "　　　　　～古代塞姆里亚文明～】\x01",
            "　　距今约１２００年前，当时繁荣绝顶的塞\x01",
            "姆里亚文明突然迎来了终结，失去了文明的人\x01",
            "们开始度过漫长的暗黑时代。\x01",
            "　　\x01",
            "　　第一层的展示物据考证是『大崩坏』之后\x01",
            "所制造的遗物。虽然据判断并非古代文明的直\x01",
            "接遗物，但因受到其深刻影响，学术方面的价\x01",
            "值极高。\x01",
            "　　\x02",
        )
    )

    Jump("loc_706")

    label("loc_706")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_4_5AA end

    def Function_5_71F(): pass

    label("Function_5_71F")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #3
        (
            "\x07\x05【古代的照明器具】\x01",
            "　　　　　　　　　　　年代：七耀历以前？\x01",
            "　　专用于焚烧篝火的容器。在塔之类被认为\x01",
            "与祭祀仪式有关联的建筑物中频繁被使用，其\x01",
            "具体用途不仅仅是照明，在宗教上可能也拥有\x01",
            "某种程度的意义。当然这点目前还只是推测罢\x01",
            "了。  \x02",
        )
    )

    Jump("loc_827")

    label("loc_827")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_5_71F end

    def Function_6_840(): pass

    label("Function_6_840")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #4
        (
            "\x07\x05【浮雕石柱】\x01",
            "　　　　　　　　　　　年代：七耀历以前？\x01",
            "　　刻有优美雕刻的石柱。在瓦雷利亚湖的湖\x01",
            "底被打捞上来，可以看出与『四轮之塔』的壁\x01",
            "画类似的纹样在其上也被反复使用。\x01",
            "　　\x02",
        )
    )

    Jump("loc_90F")

    label("loc_90F")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_6_840 end

    def Function_7_928(): pass

    label("Function_7_928")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #5
        (
            "\x07\x05【瓷工艺的地板】\x01",
            "　　　　　　　　　　　年代：七耀历以前？\x01",
            "　　遗迹内部彩色镶嵌的瓷工艺地板。将破碎\x01",
            "的天然石块巧妙拼接，作出朴素而美妙的花纹\x01",
            "样式。\x01",
            "　　\x02",
        )
    )

    Jump("loc_9EA")

    label("loc_9EA")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_928 end

    def Function_8_A03(): pass

    label("Function_8_A03")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #6
        (
            "\x07\x05【七耀历１～５００年左右\x01",
            "　　　　　　　　～暗黑时代的到来～】\x01",
            "　　由于『大崩坏』而导致文明尽失，世界陷\x01",
            "入了长期的混乱时代。\x01",
            "　　大小各异的国家、势力使得无尽的战争持\x01",
            "续了约５００年间，后世称此时代为『暗黑时\x01",
            "代』。\x02",
        )
    )

    Jump("loc_AFC")

    label("loc_AFC")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_A03 end

    def Function_9_B15(): pass

    label("Function_9_B15")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #7
        (
            "\x07\x05【骑士们的武具】\x01",
            "　　　　　　　　年代：七耀历５００年左右\x01",
            "　　日夜征战的时代中，战士们的集团拥有社\x01",
            "会性的强大影响力，最终成长为特权的骑士阶\x01",
            "级。\x01",
            "　　他们佩戴着如展品所示的武具投身沙场，\x01",
            "获得战利品和领土，势力不断扩大。\x01",
            "  \x02",
        )
    )

    Jump("loc_C14")

    label("loc_C14")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_9_B15 end

    def Function_10_C2D(): pass

    label("Function_10_C2D")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #8
        (
            "\x07\x05【七耀历５００～１１００年左右\x01",
            "　　　　　　～七耀教会带来的安定期～】\x01",
            "　　七耀教会登上历史舞台，正值暗黑时代末\x01",
            "期，七耀历５００年左右。\x01",
            "　　以『空之女神』为中心所整理的教义，通\x01",
            "过教会救济民众的社会活动，瞬间深入人心。\x01",
            "　　它的权威很快成长到连贵族、骑士阶级也\x01",
            "无法忽视的地步，其后以教会为中心的新秩序\x01",
            "便逐步形成了。\x01",
            "  \x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_10_C2D end

    def Function_11_D9F(): pass

    label("Function_11_D9F")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #9
        (
            "\x07\x05【古代文明的遗物——\x01",
            "　　　　　　　　『古代遗物』】\x01",
            "　　　　　　　　　　　　　　　年代：不明\x01",
            "　　『古代遗物』是从各地发现的古代遗迹中\x01",
            "出土的诸如器物、杖等形态各异、不可思议的\x01",
            "遗物。\x01",
            "　　在七耀教会的教义中，作为与女神赐予的\x01",
            "『七至宝』相关的物品，其回收成为教会必须\x01",
            "履行的义务之一。展品的『古代遗物』也是教\x01",
            "会所回收的物品。\x01",
            "　　许多传闻称其拥有超常的力量，但此展品\x01",
            "已经失去能力，无法启动。\x01",
            "　　\x02",
        )
    )

    Jump("loc_F52")

    label("loc_F52")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_11_D9F end

    def Function_12_F6B(): pass

    label("Function_12_F6B")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #10
        (
            "\x07\x05【七耀教会的祭具】\x01",
            "　　　　　　　　年代：七耀历９００年左右\x01",
            "　　七耀教会创造岀种种的宗教艺术，由此开\x01",
            "始教会开拓出一个稳定的时代。据考证，『空\x01",
            "之女神』的圣像也是由此时起被塑造为现今的\x01",
            "姿态。此外，现在所使用的祭祀道具多数也是\x01",
            "在这个时代被定型的。\x01",
            "　　\x02",
        )
    )

    Jump("loc_1086")

    label("loc_1086")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_12_F6B end

    def Function_13_109F(): pass

    label("Function_13_109F")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #11
        (
            "\x07\x05【七耀教会圣典的抄本】\x01",
            "　　　　　　　　年代：七耀历５００年左右\x01",
            "　　暗黑时代末期的原始七耀教会所使用的圣\x01",
            "典抄本。中世纪没有印刷技术，因此这本书是\x01",
            "由人手工抄写在兽皮制的纸张上的。\x01",
            "　　\x02",
        )
    )

    Jump("loc_1178")

    label("loc_1178")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_13_109F end

    def Function_14_1191(): pass

    label("Function_14_1191")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #12
        (
            "\x07\x05【中世纪的纺纱机】\x01",
            "　　　　　　　　年代：七耀历９００年左右\x01",
            "　　纺纱用的手工机械。到了稳定的中世纪，\x01",
            "农民的生活逐渐富裕，作为商品作物的棉花栽\x01",
            "培日渐繁盛。为了收入货币，这个时代的手工\x01",
            "业也开始发展。\x01",
            "　　\x02",
        )
    )

    Jump("loc_127D")

    label("loc_127D")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_14_1191 end

    SaveToFile()

Try(main)
