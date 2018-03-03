from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'C4203   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4203.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60031",
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
        'Norche',                               # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
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
        'ED6_DT07/CH01230 ._CH',             # 00
        'ED6_DT09/CH11120 ._CH',             # 01
        'ED6_DT09/CH11121 ._CH',             # 02
        'ED6_DT09/CH11110 ._CH',             # 03
        'ED6_DT09/CH11111 ._CH',             # 04
        'ED6_DT09/CH11130 ._CH',             # 05
        'ED6_DT09/CH11131 ._CH',             # 06
        'ED6_DT09/CH10040 ._CH',             # 07
        'ED6_DT09/CH10041 ._CH',             # 08
        'ED6_DT09/CH11140 ._CH',             # 09
        'ED6_DT09/CH11141 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH01230P._CP',             # 00
        'ED6_DT09/CH11120P._CP',             # 01
        'ED6_DT09/CH11121P._CP',             # 02
        'ED6_DT09/CH11110P._CP',             # 03
        'ED6_DT09/CH11111P._CP',             # 04
        'ED6_DT09/CH11130P._CP',             # 05
        'ED6_DT09/CH11131P._CP',             # 06
        'ED6_DT09/CH10040P._CP',             # 07
        'ED6_DT09/CH10041P._CP',             # 08
        'ED6_DT09/CH11140P._CP',             # 09
        'ED6_DT09/CH11141P._CP',             # 0A
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


    DeclMonster(
        X                   = -47360,
        Z                   = 0,
        Y                   = 42620,
        Unknown_0C          = 180,
        Unknown_0E          = 1,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -121330,
        Z                   = 0,
        Y                   = 50600,
        Unknown_0C          = 180,
        Unknown_0E          = 5,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B3,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -88180,
        Z                   = 0,
        Y                   = 51510,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -91330,
        TriggerZ            = 0,
        TriggerY            = 60050,
        TriggerRange        = 1000,
        ActorX              = -91210,
        ActorZ              = 1500,
        ActorY              = 60790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_19A",          # 00, 0
        "Function_1_1AE",          # 01, 1
        "Function_2_1E3",          # 02, 2
        "Function_3_318",          # 03, 3
        "Function_4_341",          # 04, 4
        "Function_5_D2E",          # 05, 5
        "Function_6_122E",         # 06, 6
        "Function_7_1D64",         # 07, 7
        "Function_8_1DC5",         # 08, 8
    )


    def Function_0_19A(): pass

    label("Function_0_19A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_1AD")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_1AD")

    Return()

    # Function_0_19A end

    def Function_1_1AE(): pass

    label("Function_1_1AE")

    OP_64(0x1, 0x1)
    OP_72(0x1000, 0x0)
    ExitThread()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CA")
    OP_6F(0x1, 0)
    Jump("loc_1D1")

    label("loc_1CA")

    OP_6F(0x1, 60)

    label("loc_1D1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E2")
    OP_22(0x1CD, 0x1, 0x64)

    label("loc_1E2")

    Return()

    # Function_1_1AE end

    def Function_2_1E3(): pass

    label("Function_2_1E3")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BC")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x203, 1)"), scpexpr(EXPR_END)), "loc_251")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\x03\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FF7)
    Jump("loc_2B9")

    label("loc_251")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\x03\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x03\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_2B9")

    Jump("loc_30A")

    label("loc_2BC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05So I heard you like chests... YOU PERVERT!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x13, 0x0)

    label("loc_30A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_1E3 end

    def Function_3_318(): pass

    label("Function_3_318")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D6(0x0)
    OP_E3(0x0, 0xC, 1, 0x0)
    ClearParty()
    AddParty(0x0, 0xEE, 0xFF)
    OP_28(0x1D, 0x4, 0x8)
    Call(0, 4)
    Call(0, 5)
    Return()

    # Function_3_318 end

    def Function_4_341(): pass

    label("Function_4_341")

    OP_20(0x0)
    OP_23(0x1CD)
    OP_C4(0x0, 0x20000000)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x101, -60570, 0, 90980, 90)
    SetChrPos(0x10, -59240, 0, 90940, 270)
    OP_6D(-59750, 200, 90940, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_77(0xEE, 0xB0, 0x70, 0x0, 0x0)
    OP_82(0xA4, 0x0)
    OP_82(0xA6, 0x0)
    OP_75(0xFF, 0x0, 0x5)
    OP_75(0xFF, 0x1, 0x5)
    OP_C4(0x0, 0x800)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #3 op#A op#5
        "\x07\x00#15A～Chapter 2 - In the Capital～\x05\x02",
    )

    CloseMessageWindow()
    Sleep(2000)
    OP_56(0x0)
    Sleep(500)
    OP_1E()
    FadeToBright(3000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, 80)
    Sleep(2000)

    AnonymousTalk(    #4
        (
            "\x07\x00Today was yet another day in which Estelle found\x01",
            "herself roaming the north block of Grancel City's\x01",
            "sewers.\x02\x01",

            "Her objective was simple: defeat a wanted monster\x01",
            "for the guild.\x02\x01",

            "But down there, she found more than just monsters.\x02\x01",

            "In addition to the nasties she'd become accustomed\x01",
            "to braining on a regular basis, she also came face to\x01",
            "face with a young noblewoman whose delicate\x01",
            "demeanor couldn't have looked more out of place.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #5
        (
            "\x07\x00Estelle certainly hadn't expected this!\x01",
            "'Wh-What are you doing down here?' she asked.\x02\x01",

            "The woman tittered and responded as if the answer\x01",
            "were the most obvious thing in the world:\x01",
            "'What else? Fishing, of course!'\x02\x01",

            "The noblewoman's name was Norche, and as it\x01",
            "turned out, she was a member of the Fisherman's\x01",
            "Guild.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #6
        (
            "\x07\x00'D-Do you really have to fish HERE of all places,\x01",
            "though? I mean, what if monsters find you?'\x02\x01",

            "Estelle made up her mind to try and escort the\x01",
            "woman back to the city with her...\x02\x01",

            "but Norche had other ideas, and she refused\x01",
            "to budge from what she felt was a prime fishing\x01",
            "spot.\x02\x01",

            "The two were soon locked in a battle of pure\x01",
            "stubbornness; neither would simply back down\x01",
            "gracefully, as it wasn't in their natures.\x02\x01",

            "It was in the middle of a heated argument when\x01",
            "the silver lure Estelle kept on her person fell\x01",
            "from her pocket.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_22(0x1CD, 0x1, 0x64)
    FadeToBright(1000, 0)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x9C4)
    OP_75(0xFF, 0x0, 0x1)
    OP_75(0xFF, 0x1, 0x1)
    Sleep(4000)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #7
        0x10,
        (
            "Goodness! Is that the famous silver lure?! One of\x01",
            "the three famed fishing tackles?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        "Where in Aidios' name did you obtain such a thing?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#1015FI-I don't know anything about any famous fishing\x01",
            "tackles...but I guess you mean this guy here?\x02\x03",

            "I won it from Lloyd...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        "...!!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        (
            "So you fought an anglers' duel against him, did\x01",
            "you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        (
            "I'd intended to challenge him to one myself\x01",
            "when the time was right, but I never imagined\x01",
            "he would be defeated before then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        "#1011FOookay... I am so lost right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "Very well! I shall challenge you to a ten-round\x01",
            "anglers' duel in his place!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        "#1019FT-Ten rounds?! Listen, lad--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10,
        "I will not accept no for an answer! Let us begin!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        "#1004FW-Wait a sec...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C4(0x1, 0x20000000)
    OP_23(0x1CD)
    Sleep(300)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(3000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    PlayEffect(0xA4, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0xA6, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_20(0xBB8)
    OP_21()
    Return()

    # Function_4_341 end

    def Function_5_D2E(): pass

    label("Function_5_D2E")

    OP_1D(0xC0)
    OP_AD(0x240138, 0x0, 0x0, 0x1F4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D47")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_122D")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        330,
        0,
        (
            "Start\x01",      # 0
            "Rules\x01",      # 1
            "Quit\x01",       # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0xFF)
    SetMessageWindowPos(72, 320, 56, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_DA4"),
        (1, "loc_DCE"),
        (2, "loc_11EB"),
        (SWITCH_DEFAULT, "loc_122A"),
    )


    label("loc_DA4")

    OP_AE(0x1F4)
    Sleep(1000)
    Call(0, 6)
    OP_1D(0xC0)
    OP_AD(0x240138, 0x0, 0x0, 0x1F4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_122A")

    label("loc_DCE")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "\x07\x05#0W―――――――――――――――――――――――――――\x01\x01",
            "Estelle and Norche will face off in a ten-round duel of the century. Both\x01",
            "will take turns at fishing, and whoever has the most points at the end of\x01",
            "the ten rounds will be declared the winner.\x01\x01",
            "When it is Estelle's turn, you will be prompted to choose a rod and a bait\x01",
            "to use. Certain baits can only be used with certain rods.\x01\x01",
            "After choosing, the game begins. When the ! mark appears, quickly press\x01",
            "confirm to catch the fish.\x01\x01",
            "―――――――――――――――――――――――――――#20W\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #19
        (
            "\x07\x05#0W―――――――――――――――――――――――――――\x01\x01",
            "Certain fish can only be caught with certain baits, and in addition, some\x01",
            "fish can be used as bait to catch other fish.\x01\x01",
            "Different varieties of fish are worth different amounts of points, making\x01",
            "trying to catch more valuable ones the key to success.\x01\x01",
            "More valuable ones are also more likely to escape, but don't let that deter\x01",
            "you.\x01\x01",
            "―――――――――――――――――――――――――――#20W\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_122A")

    label("loc_11EB")

    OP_AE(0x1F4)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_A2(0x2505)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_121E")
    NewScene("ED6_DT21/U4169   ._SN", 105, 0, 0)
    IdleLoop()
    Jump("loc_1227")

    label("loc_121E")

    NewScene("ED6_DT21/U4121   ._SN", 110, 0, 0)
    IdleLoop()

    label("loc_1227")

    Jump("loc_122A")

    label("loc_122A")

    Jump("loc_D47")

    label("loc_122D")

    Return()

    # Function_5_D2E end

    def Function_6_122E(): pass

    label("Function_6_122E")

    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-65390, 0, 88950, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x101, -65820, 0, 90500, 180)
    SetChrPos(0x10, -58350, 0, 90510, 180)
    OP_48()
    OP_3E(0x24F, 1)
    OP_3E(0x250, 1)
    OP_3E(0x24E, 1)
    OP_3E(0x253, 1)
    OP_3E(0x3D4, 3)
    OP_3E(0x3D5, 3)
    OP_3E(0x3D6, 3)
    OP_3E(0x3D7, 3)
    OP_22(0x1CD, 0x1, 0x64)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_C0(0x1B, 0x1, 0xFFFFF470, 0xFFFFF830, 0x7EF4, 0xB4, 0xFFFFF45C, 0xFFFFF448, 0x72C4)"), scpexpr(EXPR_END)), "loc_1315")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_131F")

    label("loc_1315")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_131F")

    EventBegin(0x0)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x101, -60570, 0, 90980, 90)
    SetChrPos(0x10, -59240, 0, 90940, 270)
    OP_6D(-59750, 200, 90940, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(3000)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_13A0"),
        (0, "loc_1586"),
        (SWITCH_DEFAULT, "loc_1589"),
    )


    label("loc_13A0")

    FadeToBright(1000, 0)
    OP_1E()
    Sleep(1000)

    ChrTalk(    #20
        0x101,
        "#1003FI-I lost...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        "Ohohohoho! The silver lure is mine at last!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        (
            "And soon, I will be able to defeat our guild's\x01",
            "leader! I can feel it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#1009FCrap... I wasn't expecting to feel this frustrated\x01",
            "about losing a duel I didn't even want to do in\x01",
            "the first place...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_20(0x7D0)
    OP_0D()
    OP_23(0x1CD)
    Sleep(1000)
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #24
        "\x18\x07\x05Try again?\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        200,
        0,
        (
            "Try Again\x01",       # 0
            "Leave Door\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(1000)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_154D"),
        (0, "loc_1577"),
        (SWITCH_DEFAULT, "loc_1586"),
    )


    label("loc_154D")

    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_A2(0x2505)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_1568")
    NewScene("ED6_DT21/U4169   ._SN", 105, 0, 0)
    IdleLoop()
    Jump("loc_1571")

    label("loc_1568")

    NewScene("ED6_DT21/U4121   ._SN", 110, 0, 0)
    IdleLoop()

    label("loc_1571")

    Jump("loc_1586")

    label("loc_1577")

    OP_D6(0x1)
    OP_D6(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_1586")

    Jump("loc_1589")

    label("loc_1589")

    FadeToBright(1000, 0)
    OP_1E()
    OP_C4(0x0, 0x20000000)
    Sleep(1000)

    ChrTalk(    #25
        0x10,
        (
            "H-How could this have happened...? \x01",
            "How could I, of all people, be defeated?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#1000F*sigh* Well? You satisfied now?\x02\x03",

            "If you are, it's time you came with me back to\x01",
            "the city. Trust me--it's not safe down here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        (
            "You were truly more worried about me than\x01",
            "winning the duel, weren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10,
        "Haha... No wonder I couldn't defeat you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        "Now, if you will...kindly accept this.\x02",
    )

    CloseMessageWindow()
    OP_8E(0x10, 0xFFFF15FA, 0x0, 0x1630A, 0x7D0, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #30
        "\x07\x05Estelle received a golden rod from Norche.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_8F(0x10, 0xFFFF1898, 0x0, 0x1633C, 0x7D0, 0x0)
    Sleep(500)

    ChrTalk(    #31
        0x101,
        (
            "#1004FWow! It's so shiny!\x02\x03",

            "#1008FAre you sure I can have this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x10,
        (
            "In fact, I insist. I would be more troubled\x01",
            "if you didn't accept it--these are the laws\x01",
            "behind an anglers' duels, as you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10,
        (
            "Still, kindly remember that you have more\x01",
            "to fear than just me. No getting complacent\x01",
            "simply because I fell in battle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10,
        (
            "There's still our guild's leader to defeat,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#1011FAww, man. Is he really that good?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10,
        (
            "Indeed. His name is Mr. Fisher, and he is both this\x01",
            "guild's founder and its most capable member.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10,
        (
            "Knowing that may incline you to avoid facing him,\x01",
            "but don't think you will be so lucky--with the\x01",
            "two tackles you now possess, he will come for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10,
        (
            "A duel with him is nigh...whether you desire it or\x01",
            "not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        "#1015FA-All righty, then... If you say so.\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_23(0x1CD)
    OP_20(0xBB8)
    Sleep(3000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #40
        (
            "\x07\x05At this point, Estelle still had no idea just how\x01",
            "capable this 'Fisher' may prove to be.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #41
        (
            "\x07\x05And while there was a small part of her that couldn't\x01",
            "help but regret biting the lure of the Fisherman's\x01",
            "Guild, there was a much greater part that couldn't deny\x01",
            "wanting to see where this journey would take her...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C4(0x1, 0x20000000)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CAB")
    Sleep(3000)
    OP_28(0x1D, 0x4, 0x10)
    OP_28(0x1D, 0x4, 0x20)
    OP_28(0x1E, 0x4, 0x2)
    OP_3E(0x1AB, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #42
        "\x07\x05Received \x1F\xAB\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    AddMira(5000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #43
        "\x07\x05Received \x07\x025,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_1CAB")

    Sleep(2000)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")

    AnonymousTalk(    #44
        "\x18\x07\x05Continue to Chapter 3?\x02",
    )

    Sleep(1000)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        200,
        0,
        (
            "Continue\x01",        # 0
            "Leave Door\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(1000)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_1D32"),
        (0, "loc_1D54"),
        (SWITCH_DEFAULT, "loc_1D63"),
    )


    label("loc_1D32")

    OP_A2(0x2505)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_1D48")
    NewScene("ED6_DT21/U4169   ._SN", 105, 0, 0)
    IdleLoop()
    Jump("loc_1D51")

    label("loc_1D48")

    NewScene("ED6_DT21/U4121   ._SN", 110, 0, 0)
    IdleLoop()

    label("loc_1D51")

    Jump("loc_1D63")

    label("loc_1D54")

    OP_A2(0x2504)
    NewScene("ED6_DT21/R2201   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1D63")

    label("loc_1D63")

    Return()

    # Function_6_122E end

    def Function_7_1D64(): pass

    label("Function_7_1D64")

    EventBegin(0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #45
        "\x07\x05It's locked tightly.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_7_1D64 end

    def Function_8_1DC5(): pass

    label("Function_8_1DC5")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #46
        "\x07\x05The trapdoor is locked tightly.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_8_1DC5 end

    SaveToFile()

Try(main)
