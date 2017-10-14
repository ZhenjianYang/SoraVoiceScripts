from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T1130_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1130_1 ._SN',
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_10FE",         # 01, 1
        "Function_2_1236",         # 02, 2
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F1")

    ChrTalk(    #0
        0x101,
        (
            "#1002FHey, this looks like the place\x01",
            "on the card!\x02\x03",

            "Think we found our match?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C5")

    ChrTalk(    #1
        0x103,
        (
            "#022FIt's certainly possible.\x02\x03",

            "It's going to have to wait until later,\x01",
            "however. Right now, we need to hurry\x01",
            "to Ravennue Village.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #2
        0x101,
        "#1002FYeah, you're right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3ED")

    label("loc_1C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_281")

    ChrTalk(    #3
        0x108,
        (
            "#072FIt's certainly possible.\x02\x03",

            "It's going to have to wait until later,\x01",
            "though. Right now, we need to hurry\x01",
            "to Ravennue Village.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(    #4
        0x101,
        "#1002FYeah, you're right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3ED")

    label("loc_281")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_334")

    ChrTalk(    #5
        0x104,
        (
            "#030FIt's certainly possible...\x02\x03",

            "We mustn't concern ourselves\x01",
            "with it now, however. We must\x01",
            "hurry to Ravennue Village.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #6
        0x101,
        "#1002FYeah, you're right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3ED")

    label("loc_334")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3ED")

    ChrTalk(    #7
        0x105,
        (
            "#042FIt's certainly possible...\x02\x03",

            "Let's put that case aside for the\x01",
            "time being. Right now, we need to\x01",
            "hurry to Ravennue Village.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #8
        0x101,
        "#1002FYeah, you're right.\x02",
    )

    CloseMessageWindow()

    label("loc_3ED")

    TalkEnd(0xFF)
    Return()

    label("loc_3F1")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 15500, 4000, 43010, 90)
    SetChrPos(0xF7, 15490, 4000, 44530, 180)
    SetChrPos(0xF8, 14760, 4000, 45010, 180)
    SetChrPos(0xF9, 15520, 4000, 45770, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_459")
    SetChrPos(0x4, 14740, 4000, 46100, 180)

    label("loc_459")

    OP_6D(15000, 4500, 43060, 0)
    OP_67(0, 4940, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(47000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #9
        0x101,
        (
            "#1002FThese are the Testaments of\x01",
            "the Septian Church, aren't they?\x02\x03",

            "Do you think this could be the\x01",
            "'words of the Goddess' the clue\x01",
            "was talking about?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5BB")

    ChrTalk(    #10
        0x103,
        (
            "#026FSpot on.\x02\x03",

            "#020FThe Testaments are supposed to\x01",
            "be the great tidings brought about\x01",
            "by the Goddess in book form.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_756")

    label("loc_5BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_640")

    ChrTalk(    #11
        0x108,
        (
            "#070FProbably.\x02\x03",

            "The Testaments are supposed to\x01",
            "be the great tidings brought about\x01",
            "by the Goddess in book form.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_756")

    label("loc_640")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6C6")

    ChrTalk(    #12
        0x104,
        (
            "#035FMost likely.\x02\x03",

            "#030FThe Testaments are meant to be\x01",
            "be exalted tidings of the Goddess\x01",
            "immortalized on paper.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_756")

    label("loc_6C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_756")

    ChrTalk(    #13
        0x106,
        (
            "#053FYou're right on target.\x02\x03",

            "#050FThe Testaments are supposed\x01",
            "to be stuff the Goddess said put to\x01",
            "paper, so it makes sense.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_756")

    OP_8C(0x101, 0, 400)

    ChrTalk(    #14
        0x101,
        (
            "#1015F#4PNow that you mention it,\x01",
            "I remember learning something\x01",
            "about that in Sunday School...\x02\x03",

            "#1000FAnyway, let's check it out.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "\x07\x05When Estelle investigated the book, she found an iron medal\x01",
            "wedged between the pages.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #16
        "Found a #2C#16Imedal with a two-winged horse and sword design#0C.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_8C(0x101, 0, 400)

    ChrTalk(    #17
        0x101,
        (
            "#1001F#4PSweet! We found it!\x02\x03",

            "#1016FBut, man, just look at this thing.\x01",
            "A little imposing for a medal, don't\x01",
            "you think?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9DC")

    ChrTalk(    #18
        0x104,
        (
            "#031FIt certainly is. That's the Erebonian\x01",
            "way.\x02\x03",

            "By comparison, Liberlians tend to\x01",
            "lean towards keeping things simple\x01",
            "and elegant.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9F")

    label("loc_9DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A4B")

    ChrTalk(    #19
        0x105,
        (
            "#045FImposing is right.\x02\x03",

            "Still, I'd say the design is pretty apt\x01",
            "for an Erebonian medal.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9F")

    label("loc_A4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AD3")

    ChrTalk(    #20
        0x108,
        (
            "#070FThat's the Empire in a nutshell: big\x01",
            "and imposing.\x02\x03",

            "I'd say the design is pretty apt for an\x01",
            "Erebonian medal.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9F")

    label("loc_AD3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B9F")

    ChrTalk(    #21
        0x103,
        (
            "#021FI'd say it fits Erebonian's character\x01",
            "quite well, actually.\x02\x03",

            "They're a country built on military might.\x01",
            "The more imposing an image they can\x01",
            "project to other countries, the better.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9F")


    ChrTalk(    #22
        0x101,
        (
            "#1011F#4PSo it's a cultural thing? I never would've\x01",
            "guessed.\x02\x03",

            "#1016FPlus, what with Ambassador Crainagh\x01",
            "wearing it and all, this medal's gonna\x01",
            "need the impact of a boot to the head.\x02\x03",

            "It kind of works, in a way.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D18")

    ChrTalk(    #23
        0x106,
        (
            "#051FThat's one way of putting it.\x02\x03",

            "Any less showy on a guy with that\x01",
            "kinda presence and nobody would\x01",
            "notice the damn thing's even there. \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E71")

    label("loc_D18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D6E")

    ChrTalk(    #24
        0x107,
        (
            "#067FYeah, maybe.\x02\x03",

            "He's kind of scary, so I think it\x01",
            "suits him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E71")

    label("loc_D6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DF5")

    ChrTalk(    #25
        0x103,
        (
            "#020FWell said.\x02\x03",

            "Anything less would just look cheap\x01",
            "by comparison. That man's presence\x01",
            "is something to behold. \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E71")

    label("loc_DF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E71")

    ChrTalk(    #26
        0x108,
        (
            "#071FWell said.\x02\x03",

            "It wouldn't look right on him\x01",
            "otherwise. He's the picture of\x01",
            "an intimidating Erebonian.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ED9")

    ChrTalk(    #27
        0x108,
        (
            "#070FMore so than ever, too.\x02\x03",

            "He's obviously on edge from the\x01",
            "medal being stolen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_106E")

    label("loc_ED9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F71")

    ChrTalk(    #28
        0x105,
        (
            "#040FAnd that might be even more true\x01",
            "now than ever.\x02\x03",

            "He's looked scarier than usual,\x01",
            "probably because of the medal\x01",
            "being stolen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_106E")

    label("loc_F71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FFF")

    ChrTalk(    #29
        0x103,
        (
            "#020FThat's more true than ever, too.\x02\x03",

            "The medal being stolen has\x01",
            "no doubt been more than a little\x01",
            "frustrating for him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_106E")

    label("loc_FFF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_106E")

    ChrTalk(    #30
        0x104,
        (
            "#030FThat applies more than ever, too.\x02\x03",

            "Losing the medal does seem to\x01",
            "have put him on edge.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_106E")


    ChrTalk(    #31
        0x101,
        (
            "#1015F#4PNow that you mention it...\x02\x03",

            "#1001FWell, whatever. At least we found it!\x01",
            "Let's go give it back to him.\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x1, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1132   ._SN", 110, 0, 0)
    IdleLoop()
    Return()

    # Function_0_AA end

    def Function_1_10FE(): pass

    label("Function_1_10FE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x381), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_110B")
    Return()

    label("loc_110B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_111D")
    Return()

    label("loc_111D")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x8)"), scpexpr(EXPR_END)), "loc_1158")
    Call(1, 2)
    Jump("loc_122F")

    label("loc_1158")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x3E8)"), scpexpr(EXPR_END)), "loc_1167")
    Call(1, 2)
    Jump("loc_122F")

    label("loc_1167")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xFF)"), scpexpr(EXPR_END)), "loc_11D9")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #32
        "\x07\x05Tried showing them the photograph, but they didn't recognize her.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_122F")

    label("loc_11D9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #33
        "\x07\x05There's no one to show the photograph to nearby.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_122F")

    OP_0D()
    ClearMapFlags(0x80)
    Return()

    # Function_1_10FE end

    def Function_2_1236(): pass

    label("Function_2_1236")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_12B4")

    ChrTalk(    #34
        0x8,
        (
            "I shall pray that you find the girl\x01",
            "in this photograph.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "Do what you must, and may you\x01",
            "never lose hope.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13BF")

    label("loc_12B4")


    ChrTalk(    #36
        0x8,
        (
            "You'd like to know what happened\x01",
            "to the girl in this photograph?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "Forgive me--I'm afraid I have no\x01",
            "recollection of her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        (
            "Still, I'm sure you'll come to meet\x01",
            "with her if you follow the Goddess'\x01",
            "path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "Do what you must, and may you\x01",
            "never lose hope.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_13BF")

    TalkEnd(0x8)
    Return()

    # Function_2_1236 end

    SaveToFile()

Try(main)
