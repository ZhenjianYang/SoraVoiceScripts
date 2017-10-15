from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0110_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0110_1 ._SN',
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
        "Function_1_612",          # 01, 1
        "Function_2_DD6",          # 02, 2
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #0
        0xFE,
        "Why, hello, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "Luke's finally woken up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "He's already back to his old self.\x01",
            "He's even running around outside.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34D, 0)), scpexpr(EXPR_END)), "loc_1E5")

    ChrTalk(    #3
        0x101,
        (
            "#1017FHaha, yeah, we saw him.\x02\x03",

            "If anything, he's even MORE hyper\x01",
            "than before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "I'm almost worried he'll get too ahead\x01",
            "of himself and get hurt, at this point!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27F")

    label("loc_1E5")


    ChrTalk(    #5
        0x101,
        (
            "#1001FHaha. Well, it's way better than the alternative.\x02\x03",

            "I'll visit him and see how he is later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "Please do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "He's really quite fond of you.\x02",
    )

    CloseMessageWindow()

    label("loc_27F")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #8
        0xFE,
        (
            "All that aside, though. I get the impression\x01",
            "you have a purpose in coming over today,\x01",
            "hmm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#1008FOh, you could tell, huh?\x02\x03",

            "Actually, yeah, I have something I'd like\x01",
            "to ask you about, Miss Maggy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "Go right ahead!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "\x07\x05Estelle explained that she was looking for the stew recipe\x01",
            "she'd heard about from Radford.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #12
        0xFE,
        "A strong pepper stew, hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "I've heard of it, yes,\x01",
            "but I've never made it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "I was always so busy helping my parents.\x01",
            "Our meals were very simple, really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        "#1007FOh... I see. Great.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_535")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #16
        0x103,
        "#020FEither way, let's report the recipe we found.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #17
        0x101,
        (
            "#1015FYeah, about all we can do\x01",
            "at this point.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_608")

    label("loc_535")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x400)"), scpexpr(EXPR_END)), "loc_5A6")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #18
        0x103,
        (
            "#020FPerhaps we should just check Rhett's\x01",
            "house like he said?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #19
        0x101,
        "#1015FMaybe.\x02",
    )

    CloseMessageWindow()
    Jump("loc_608")

    label("loc_5A6")


    ChrTalk(    #20
        0x103,
        "#020FPerhaps we should visit someone else.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #21
        0xFE,
        "I'm sorry I couldn't be of more help.\x02",
    )

    CloseMessageWindow()

    label("loc_608")

    OP_A2(0x9)
    OP_28(0x75, 0x1, 0x10)
    Return()

    # Function_0_AA end

    def Function_1_612(): pass

    label("Function_1_612")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 91960, 0, 162870, 90)
    SetChrPos(0xF7, 91150, 0, 162270, 90)
    SetChrPos(0xF8, 90480, 0, 163570, 90)
    SetChrPos(0xF9, 91330, 0, 164280, 135)
    OP_8C(0xFE, 270, 0)
    OP_6D(91870, 0, 163740, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_4A(0xFE, 255)
    OP_0D()

    ChrTalk(    #22
        0xFE,
        "#2PAh, Estelle. What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#1000FNothing too important, really.\x02\x03",

            "Just kind of admiring your massive\x01",
            "collection of books!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "#2PHeheh! Indeedy.\x01",
            "I'm quite proud of my collection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "#2PCollecting old books is my calling,\x01",
            "and this is my cathedral, more or less.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#1015FOld books...as a calling?\x02\x03",

            "I wonder. Maybe it's worth asking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x103,
        (
            "#027F#3PA bit of wild grasping at straws never\x01",
            "hurt anyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "#2PEr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "#2PYou've lost me, I'm afraid.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #30
        (
            "\x07\x05Estelle explained that she was looking for Bloom's\x01",
            "recipe book as part of a guild request.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #31
        0x101,
        (
            "#1011FSo that's the story.\x02\x03",

            "It's the wildest of guesses, but I don't\x01",
            "suppose you have that book?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "#2PMiss Bloom's recipe book, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "#2POh, yeah, I asked her to give that to\x01",
            "me a while back.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #34
        0x101,
        "#1004FW-Wait, seriously?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "#2PSure! She said it had a lot of traditional\x01",
            "local recipes, so I wanted to make\x01",
            "sure I preserved it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "#2PI asked her for it, and she entrusted it\x01",
            "to my care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#1011FOkay. Cool!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF0")

    ChrTalk(    #38
        0x107,
        "#060FYeah, that sounds right!\x02",
    )

    CloseMessageWindow()
    Jump("loc_BCD")

    label("loc_AF0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B2F")

    ChrTalk(    #39
        0x105,
        "#040FThat does sound like our objective.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BCD")

    label("loc_B2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B64")

    ChrTalk(    #40
        0x108,
        "#070FSounds like what we need.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BCD")

    label("loc_B64")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B9F")

    ChrTalk(    #41
        0x104,
        "#030FHeh, our objective is in sight.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BCD")

    label("loc_B9F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BCD")

    ChrTalk(    #42
        0x106,
        "#051FSounds like our book.\x02",
    )

    CloseMessageWindow()

    label("loc_BCD")


    ChrTalk(    #43
        0x103,
        (
            "#021F#3PHeehee! Grope for straws, and eventually\x01",
            "you come up big.\x02\x03",

            "Let's have a look at the infinite wisdom\x01",
            "of the ancients, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        "#1000FDo you mind, Rhett?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "#2PI don't mind at all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "#2PThe hitch would be... I'm not entirely\x01",
            "sure where it is, come to think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "#2PIt's definitely in my archive.\x01",
            "I know that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "#2PI think it would be faster if\x01",
            "you just search yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#1006FOh, yeah, sure.\x02\x03",

            "I mean, we're the ones asking the favor,\x01",
            "really, so we can handle that at least.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x75, 0x1, 0x400)
    OP_65(0x0, 0x1)
    EventEnd(0x0)
    Return()

    # Function_1_612 end

    def Function_2_DD6(): pass

    label("Function_2_DD6")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #50
        "\x07\x05Bloom's recipe book is on the shelf!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "Read It!\x01",           # 0
            "Piffle, Words\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE1")
    OP_B8(0x236, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x800)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FDE")
    Sleep(400)
    OP_3E(0x236, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #51
        "\x07\x00Received #566i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #52
        0x101,
        (
            "#1028FOkay! Got the recipe written down.\x02\x03",

            "#1007FTo be totally honest, I'm not sure it\x01",
            "makes any sense, buuuuuuut...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x103,
        (
            "#020FWe can leave figuring it out to the\x01",
            "professionals.\x02\x03",

            "We have the ingredients list, at least,\x01",
            "so let's go and report.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x75, 0x1, 0x800)

    label("loc_FDE")

    Jump("loc_FE1")

    label("loc_FE1")

    TalkEnd(0xFF)
    Return()

    # Function_2_DD6 end

    SaveToFile()

Try(main)
