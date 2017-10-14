from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0131_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T0131.x',
        MapIndex            = 7,
        MapDefaultBGM       = "ed60010",
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
        "Function_1_473",          # 01, 1
        "Function_2_6AC",          # 02, 2
        "Function_3_15E4",         # 03, 3
        "Function_4_2057",         # 04, 4
        "Function_5_25B1",         # 05, 5
        "Function_6_2EC3",         # 06, 6
        "Function_7_30F2",         # 07, 7
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 38600, 0, 127160, 270)
    SetChrPos(0x103, 39970, 0, 126320, 270)
    SetChrPos(0xF8, 41010, 0, 126700, 270)
    SetChrPos(0xF9, 39700, 0, 127590, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_124")
    SetChrPos(0xF9, 41010, 0, 126700, 270)
    SetChrPos(0xF8, 39700, 0, 127590, 270)

    label("loc_124")

    OP_8C(0xB, 90, 0)
    OP_6D(38020, 0, 128180, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_4A(0xB, 255)
    OP_0D()

    ChrTalk(    #0
        0xB,
        "Hey there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xB,
        "Finally, my Tabitha's woken up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xB,
        "Sorry for kicking up such a fuss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#1000F#7POh, no, please, don't let it bother you.\x02\x03",

            "It's all part of the job, really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x103,
        (
            "#2P#020FYes, it's as Estelle said.\x02\x03",

            "...Incidentally, apparently you have some\x01",
            "kind of job for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xB,
        "Oh, I see. So you're here on business, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xB,
        (
            "Well, what I'd like to ask you to do is to\x01",
            "investigate a certain recipe and find its\x01",
            "ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xB,
        "How about it? Got the time?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_395")
    Call(1, 2)
    Jump("loc_470")

    label("loc_395")


    ChrTalk(    #8
        0x101,
        "#1015F#7PSorry. I don't think we can right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xB,
        "Oh, no good?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xB,
        (
            "Still as busy as ever even with\x01",
            "the fog cleared, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xB,
        "Well, come on back when you've got some time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        "#1000F#7PYeah, we will.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x10)
    OP_28(0x75, 0x1, 0x8000)

    label("loc_470")

    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_473(): pass

    label("Function_1_473")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 38600, 0, 127160, 270)
    SetChrPos(0x103, 39970, 0, 126320, 270)
    SetChrPos(0xF8, 41010, 0, 126700, 270)
    SetChrPos(0xF9, 39700, 0, 127590, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4ED")
    SetChrPos(0xF9, 41010, 0, 126700, 270)
    SetChrPos(0xF8, 39700, 0, 127590, 270)

    label("loc_4ED")

    OP_8C(0xB, 90, 0)
    OP_6D(38020, 0, 128180, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_555")

    ChrTalk(    #13
        0xB,
        "What, you'll do it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D5")

    label("loc_555")


    ChrTalk(    #14
        0xB,
        "Oh, hey. Back already, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xB,
        (
            "It's a recipe investigation and the\x01",
            "collection of its ingredients...\x01",
            "Feel like taking it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D5")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_626")
    Call(1, 2)
    Jump("loc_6A9")

    label("loc_626")


    ChrTalk(    #16
        0x101,
        "#1007F#7PSorry, I still can't.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xB,
        "Mmm, well that's no good. Too bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xB,
        (
            "Well, when you do get some time,\x01",
            "come on back.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)

    label("loc_6A9")

    EventEnd(0x0)
    Return()

    # Function_1_473 end

    def Function_2_6AC(): pass

    label("Function_2_6AC")


    ChrTalk(    #19
        0x101,
        (
            "#1006F#7PYeah, no prob.\x02\x03",

            "So, what recipe am I investigating?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xB,
        (
            "Right, so what I'd like you to find\x01",
            "is the recipe for a certain stew.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xB,
        (
            "We'll call it...\x01",
            "'Rolent-Style Hodgepodge Stew' for now.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(100)
    OP_62(0x103, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D1")
    OP_62(0xF8, 0x0, 2300, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_80F")

    label("loc_7D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F8")
    OP_62(0xF8, 0x0, 1700, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_80F")

    label("loc_7F8")

    OP_62(0xF8, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_80F")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83B")
    OP_62(0xF9, 0x0, 2300, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_879")

    label("loc_83B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_862")
    OP_62(0xF9, 0x0, 1700, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_879")

    label("loc_862")

    OP_62(0xF9, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_879")

    Sleep(1000)

    ChrTalk(    #22
        0x101,
        (
            "#1019F#7PR-Rolent-Style Hodgepodge Stew...?\x02\x03",

            "To be honest, that sounds about as appetizing\x01",
            "as that Potluck we found in a chest once...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x103,
        (
            "#2P#025FEr, yes... It sounds like it'd be\x01",
            "hard to keep down.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #24
        0xB,
        "N-Now, now, it's just a temporary name.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xB,
        "Anyway, I want you to investigate that recipe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xB,
        (
            "If you ask around town,\x01",
            "I'm sure you'll find something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xB,
        (
            "Apparently every home used to\x01",
            "make it back in the old days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#1015F#7PHmmm, we should probably ask some\x01",
            "old folks who know about cooking, then.\x02\x03",

            "Doesn't seem like younger people'd\x01",
            "know about what old families cooked.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B37")

    ChrTalk(    #29
        0x106,
        (
            "#051FThat's actually a sensible suggestion\x01",
            "from you for once.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE1")

    label("loc_B37")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B72")

    ChrTalk(    #30
        0x104,
        "#035FOh ho. A reasonable conclusion.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BE1")

    label("loc_B72")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BA8")

    ChrTalk(    #31
        0x108,
        "#4P#070FMmm, a good suggestion.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BE1")

    label("loc_BA8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BE1")

    ChrTalk(    #32
        0x105,
        "#040FYes, I think that's a good idea.\x02",
    )

    CloseMessageWindow()

    label("loc_BE1")


    ChrTalk(    #33
        0x103,
        (
            "#2P#026FWell, that's fine for a direction to\x01",
            "begin our investigation, but...\x02\x03",

            "We still don't have enough information\x01",
            "about the recipe itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#1007F#7PYeah, you might be right...\x02\x03",

            "#1002FIt'd be nice to know what\x01",
            "goes into it at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xB,
        "Yeah, that's a good point, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xB,
        (
            "Sorry, but you'll need to ask\x01",
            "Radford about the recipe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#1004F#7PHuh?\x02\x03",

            "I thought this was your request,\x01",
            "but you want us to ask Radford?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xB,
        (
            "Well, here's the thing... He's the one\x01",
            "who brought it up in the first place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xB,
        (
            "Apparently he ate this nostalgic\x01",
            "meal in his dreams.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xB,
        (
            "He's been begging me to make\x01",
            "it for him ever since.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E9D")

    ChrTalk(    #41
        0x107,
        (
            "#560FOoooh, so that's why\x01",
            "you requested the job...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FC3")

    label("loc_E9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EE6")

    ChrTalk(    #42
        0x105,
        "#040FI see. So that's how this request came about.\x02",
    )

    CloseMessageWindow()
    Jump("loc_FC3")

    label("loc_EE6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F2F")

    ChrTalk(    #43
        0x108,
        "#4P#070FAh, I see. That's how this job came about.\x02",
    )

    CloseMessageWindow()
    Jump("loc_FC3")

    label("loc_F2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F79")

    ChrTalk(    #44
        0x104,
        (
            "#030FHeh, I understand now.\x01",
            "The food of dreams, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FC3")

    label("loc_F79")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FC3")

    ChrTalk(    #45
        0x106,
        (
            "#050FAh, got it. So that's why you\x01",
            "posted the request.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FC3")


    ChrTalk(    #46
        0x101,
        (
            "#1015F#7PBut, a guild job just for a stew?\x02\x03",

            "I mean, was it really that good?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x103,
        (
            "#2P#020FMm, it might not necessarily be\x01",
            "because of the flavor.\x02\x03",

            "Perhaps it's a memory of some kind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xB,
        (
            "The old man's not saying much either\x01",
            "way, but I'm sure that's the case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xB,
        (
            "Anyway, that's the story, so I'd really\x01",
            "like to serve it to him if I could.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11A0")

    ChrTalk(    #50
        0x104,
        (
            "#031FAhhhh, what a moving tale.\x02\x03",

            "To make reality a sweet dream of memories\x01",
            "past... I shall be glad to assist.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1282")

    label("loc_11A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11EC")

    ChrTalk(    #51
        0x108,
        (
            "#4P#070FWhat a moving story.\x02\x03",

            "I will be glad to help.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1282")

    label("loc_11EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1236")

    ChrTalk(    #52
        0x106,
        (
            "#051FHeh. Nice little story, there.\x02\x03",

            "Happy to help.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1282")

    label("loc_1236")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1282")

    ChrTalk(    #53
        0x105,
        (
            "#040FWhat a nice story.\x02\x03",

            "I hope we'll be able to help...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1282")

    OP_8C(0x101, 90, 400)

    ChrTalk(    #54
        0x101,
        (
            "#1006F#3PYeah, Radford's finally awake.\x02\x03",

            "Let's feed him to celebrate his recovery.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1309")

    ChrTalk(    #55
        0x107,
        "#061FHeehee... Yeah.\x02",
    )

    CloseMessageWindow()

    label("loc_1309")

    OP_8C(0x101, 270, 400)

    ChrTalk(    #56
        0x103,
        (
            "#2P#020FSo, then, we'll start by asking\x01",
            "Radford about the recipe.\x02\x03",

            "...Is there anything else we need\x01",
            "to know before we go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xB,
        (
            "Ah, well after you sort out\x01",
            "finding the recipe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xB,
        (
            "Would you mind also picking up\x01",
            "the ingredients needed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xB,
        (
            "It might use some kind of\x01",
            "rare ingredients, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        (
            "#1000F#7PNo problem.\x02\x03",

            "If ingredients are what you want,\x01",
            "then ingredients you shall have!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xB,
        "Good to hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xB,
        (
            "Can't believe how fired up I'm getting\x01",
            "over this! I can't wait to see\x01",
            " what kind of recipe it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x103,
        (
            "#2P#020FWell, don't you worry. We'll leave\x01",
            "no stone unturned in the search.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1006F#7PYup, what she said. Expect some\x01",
            "good news to come your way soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xB,
        "Thanks.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x14)
    OP_28(0x75, 0x4, 0x4)
    OP_28(0x75, 0x4, 0x8)
    OP_28(0x75, 0x1, 0x1)
    OP_28(0x75, 0x1, 0x2)
    OP_28(0x75, 0x1, 0x4)
    Return()

    # Function_2_6AC end

    def Function_3_15E4(): pass

    label("Function_3_15E4")

    EventBegin(0x0)
    OP_8C(0x11, 270, 0)
    Fade(1000)
    SetChrPos(0x101, 38190, 0, 75500, 270)
    SetChrPos(0x103, 38230, 0, 74290, 294)
    SetChrPos(0xF8, 39580, 0, 75500, 270)
    SetChrPos(0xF9, 39000, 0, 74690, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1665")
    SetChrPos(0xF9, 39580, 0, 75500, 270)
    SetChrPos(0xF8, 39000, 0, 74690, 270)

    label("loc_1665")

    OP_6D(37010, 0, 76590, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #66
        0x11,
        "#2PHmmm... Isn't the meal ready yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x11,
        (
            "#2PIt's an old recipe, so I'm sure\x01",
            "the chef is having trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        "#1000F#2PRadford, can we have a moment?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x101, 400)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #69
        0x11,
        "#1POhh, who's this but Cassius' girl.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x11,
        "#1PYou need something from me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#1015F#2PYes, we'd like to ask you about the\x01",
            "recipe you ordered from Densel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x11,
        "#1POh, that dish?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x11,
        "#1PDo you mean the stew I dreamed of?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x103,
        (
            "#5P#020FYes, that recipe.\x02\x03",

            "Actually, we've got a request from Densel...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #75
        (
            "\x07\x05They explained that they had been hired by Densel\x01",
            "to investigate the recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TurnDirection(0x11, 0x103, 400)

    ChrTalk(    #76
        0x11,
        "#5POhh, so then you'll be looking for the stew?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x11,
        "#5PHo ho. I can taste your success already.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x11,
        "#5PI'm counting on you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        (
            "#1008F#2PTh-Thanks.\x02\x03",

            "#1006FBut, we need your help before we start, sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x103,
        (
            "#5P#020FWe'd like to hear the details about that recipe.\x02\x03",

            "Not just what went into it or the flavoring,\x01",
            "but where you had it... Anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x11,
        "#5PI see, I see... Well, then...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x101, 400)

    ChrTalk(    #82
        0x11,
        (
            "#1PFirst, as I'm sure you know,\x01",
            "the recipe was for a stew.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x11,
        (
            "#1PI seem to remember the base\x01",
            "flavor was...black pepper?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x11,
        "#1PIt was a spicy, invigorating stew.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        (
            "#1015F#2PRight, right... Strong black pepper... Got it.\x02\x03",

            "#1011FAh... Go on, please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x11,
        (
            "#1PThe main ingredient was meat...I think.\x01",
            "Though you could probably also use white fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x11,
        "#1PBut I like meat, so we'll say meat for now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x11,
        (
            "#1PA big chunk of meat, bone and all,\x01",
            "so tender that it just falls off...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 180, 400)

    ChrTalk(    #89
        0x11,
        "#2PAlso, I know some herbs were used.\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x11)

    ChrTalk(    #90
        0x11,
        "#2PBut I can't remember what kind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x11,
        (
            "#2PI remember the smell, but I can't\x01",
            "remember what it was the smell of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x11,
        "#2PArgh, it's so frustrating...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#1015F#2PUhh... So the main ingredient was meat or\x01",
            "fish, but you want meat, bone and all...\x01",
            "Okay. Check.\x02\x03",

            "And, lastly there were herbs used, but\x01",
            "you don't know the exact types...\x02\x03",

            "#1000FIs that it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x103,
        "#5P#020FWell, that's fairly specific.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E9A")

    ChrTalk(    #95
        0x106,
        "#2P#051FYeah, that should be plenty to start with.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F8B")

    label("loc_1E9A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EDB")

    ChrTalk(    #96
        0x108,
        "#2P#070FYes, it should be plenty to go on.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F8B")

    label("loc_1EDB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F4A")

    ChrTalk(    #97
        0x104,
        (
            "#2P#030FMmm, yes. This should be sufficient information\x01",
            "for us to begin our recipe hunt.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F8B")

    label("loc_1F4A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F8B")

    ChrTalk(    #98
        0x105,
        "#2P#040FWe should be able to begin with this.\x02",
    )

    CloseMessageWindow()

    label("loc_1F8B")

    OP_8C(0x11, 90, 400)

    ChrTalk(    #99
        0x11,
        "#1PI hope that helped a bit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        "#1006F#2PIt's plenty. Thanks very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x11,
        "#1PWell, then, happy hunting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x11,
        (
            "#1PI'm really looking forward to hearing\x01",
            "you've found the recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)
    OP_28(0x75, 0x1, 0x8)
    EventEnd(0x0)
    Return()

    # Function_3_15E4 end

    def Function_4_2057(): pass

    label("Function_4_2057")

    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #103
        0x8,
        (
            "Estelle, I hope you'll find some\x01",
            "time to come by the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x8,
        "Elissa and I will be looking forward to it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        (
            "#1001FYeah, I'll come visit sometime.\x02\x03",

            "#1011FAh, speaking of...\x02\x03",

            "Actually, we're investigating something\x01",
            "for Densel, but...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #106
        (
            "\x07\x05Estelle explained she was looking for a stew recipe\x01",
            "for Radford.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #107
        0x8,
        (
            "Ah, that recipe. My husband asked\x01",
            "me about it just a bit ago himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x103,
        (
            "#027FWhich, of course means...\x02\x03",

            "... You don't know it either, Tabitha.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x103, 400)

    ChrTalk(    #109
        0x8,
        "That's right, unfortunately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x8,
        (
            "When I started learning to cook\x01",
            "no one made it anymore.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_238C")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #111
        0x103,
        "#020FAnyway, we should go report that recipe.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #112
        0x101,
        "#1015FYeah, looks like that's our only choice.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #113
        0x8,
        (
            "My husband is pretty troubled over this,\x01",
            "so I hope you can help him out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25A7")

    label("loc_238C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x400)"), scpexpr(EXPR_END)), "loc_244A")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #114
        0x103,
        "#020FWhy don't we just check Rhett's house already?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #115
        0x101,
        "#1015FMaybe...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #116
        0x8,
        (
            "My husband is pretty troubled over this,\x01",
            "so I hope you can help him out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25A7")

    label("loc_244A")


    ChrTalk(    #117
        0x101,
        (
            "#1025FAh, I see...\x02\x03",

            "#1015FGuess we really do have to\x01",
            "ask mostly older people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x103,
        (
            "#020FYes, that's probably best.\x02\x03",

            "...Well, then, let's continue our investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x101,
        (
            "#1000FAh, right...\x02\x03",

            "Tabitha, thanks for the help.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #120
        0x8,
        "I should be the one thanking you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x8,
        (
            "My husband is pretty troubled over this,\x01",
            "so I hope you can help him out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25A7")

    OP_A2(0x12)
    OP_28(0x75, 0x1, 0x80)
    Return()

    # Function_4_2057 end

    def Function_5_25B1(): pass

    label("Function_5_25B1")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 38600, 0, 127160, 270)
    SetChrPos(0x103, 39970, 0, 126320, 270)
    SetChrPos(0xF8, 41010, 0, 126700, 270)
    SetChrPos(0xF9, 39700, 0, 127590, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_262B")
    SetChrPos(0xF9, 41010, 0, 126700, 270)
    SetChrPos(0xF8, 39700, 0, 127590, 270)

    label("loc_262B")

    OP_8C(0xB, 90, 0)
    OP_6D(38020, 0, 128180, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_4A(0xB, 255)
    OP_0D()

    ChrTalk(    #122
        0xB,
        "Hey, Estelle. How's the investigation going?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x101,
        "#1001F#7PRight, well, we've found A recipe.\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #124
        0xB,
        "Whoa, whoa, you already found it?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xB,
        (
            "Maaan, you guys are fast.\x01",
            "Bracers are incredible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        "#1015F#7PMmmmm, might wanna hold that praise...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xB,
        "Oh, why's that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x103,
        "#2P#020FWell, you see...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #129
        (
            "\x07\x05They explained that the recipe they found was an altered\x01",
            "version of the original.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #130
        0xB,
        "I see... So that's it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xB,
        (
            "Still, can't be too greedy.\x01",
            "I'll call it a job finished with that recipe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        (
            "#1007F#7PSorry, Densel.\x02\x03",

            "It'd have been best if we'd found\x01",
            "the original, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xB,
        (
            "Ehh, the basic parts probably won't\x01",
            "be that different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xB,
        (
            "I'll smooth over the rest with my instinct\x01",
            "and experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x103,
        "#2P#021FHmm... Pretty confident.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29C6")

    ChrTalk(    #136
        0x104,
        "#031FAh, now that is a chef.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A75")

    label("loc_29C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A07")

    ChrTalk(    #137
        0x105,
        "#040FAs expected from a professional chef.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A75")

    label("loc_2A07")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A43")

    ChrTalk(    #138
        0x108,
        "#4P#070FAs I would expect from a pro.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A75")

    label("loc_2A43")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A75")

    ChrTalk(    #139
        0x107,
        "#061FWow... Now that's a cook.\x02",
    )

    CloseMessageWindow()

    label("loc_2A75")


    ChrTalk(    #140
        0x101,
        (
            "#1006F#7PWell, anyway, let me go over the\x01",
            "results of our investigation.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #141
        "\x07\x05Estelle read off the details of Bloom's recipe.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #142
        0xB,
        "Hmm... I see, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xB,
        (
            "It's more or less what I'd expected,\x01",
            "but it does use some surprising ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xB,
        "All right, now I can really get to cooking this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x101,
        "#1011F#7PSo, then, we're all done here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xB,
        "Yeah, pretty much...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xB,
        (
            "...is what I'd like to say, but I also\x01",
            "asked for the ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x103,
        (
            "#2P#020FTrue, that was part of the job.\x02\x03",

            "#027FShall we go and collect them, then?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #149
        0x101,
        "#1015F#6PUmmm, just a sec...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x388, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "OP_40(0x389, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x396, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x397, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x399, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x39A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x39C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x3A1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D32")
    OP_A2(0x15)

    label("loc_2D32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_2D73")
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #150
        0x101,
        "#1006F#7PYeah... We've got everything.\x02",
    )

    CloseMessageWindow()
    Call(1, 7)
    Jump("loc_2EC0")

    label("loc_2D73")

    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x101)
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #151
        0x101,
        (
            "#1007F#7PS-Sorry, Densel.\x02\x03",

            "Doesn't look like we have all\x01",
            "the ingredients yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xB,
        "Oh, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xB,
        "Well, then, come by later to deliver them.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x101,
        "#1003F#7PY-Yeah. Will do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x103,
        (
            "#2P#022F*sigh* It's because you slacked\x01",
            "off on checking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x101,
        "#1007F#7PCan't really argue with that...\x02",
    )

    CloseMessageWindow()
    OP_28(0x75, 0x1, 0x4000)

    label("loc_2EC0")

    EventEnd(0x0)
    Return()

    # Function_5_25B1 end

    def Function_6_2EC3(): pass

    label("Function_6_2EC3")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 38600, 0, 127160, 270)
    SetChrPos(0x103, 39970, 0, 126320, 270)
    SetChrPos(0xF8, 41010, 0, 126700, 270)
    SetChrPos(0xF9, 39700, 0, 127590, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F3D")
    SetChrPos(0xF9, 41010, 0, 126700, 270)
    SetChrPos(0xF8, 39700, 0, 127590, 270)

    label("loc_2F3D")

    OP_8C(0xB, 90, 0)
    OP_6D(38020, 0, 128180, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_4A(0xB, 255)
    OP_0D()

    ChrTalk(    #157
        0xB,
        "Oh, got all the ingredients?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x388, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "OP_40(0x389, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x396, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x397, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x399, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x39A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x39C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x3A1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_300E")
    OP_A2(0x15)

    label("loc_300E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_3049")

    ChrTalk(    #158
        0x101,
        "#1006F#7PYup! We've brought everything.\x02",
    )

    CloseMessageWindow()
    Call(1, 7)
    Jump("loc_30EF")

    label("loc_3049")


    ChrTalk(    #159
        0x101,
        "#1008F#7PAh, s-sorry. We're still not ready.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xB,
        "Seems like you're having a hard time of it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xB,
        (
            "Well, whatever. Come on back when\x01",
            "you've got the ingredients.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30EF")

    EventEnd(0x0)
    Return()

    # Function_6_2EC3 end

    def Function_7_30F2(): pass

    label("Function_7_30F2")

    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #162
        (
            "#0C#904i x1\x01",
            "#905i x1\x01",
            "#918i x2\x01",
            "#919i x5\x01",
            "#921i x5\x01",
            "#922i x2\x01",
            "#924i x4\x01",
            "#929i x2 ingredients handed over.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x388, 1)
    OP_3F(0x389, 1)
    OP_3F(0x396, 2)
    OP_3F(0x397, 5)
    OP_3F(0x399, 5)
    OP_3F(0x39A, 2)
    OP_3F(0x39C, 4)
    OP_3F(0x3A1, 2)

    ChrTalk(    #163
        0xB,
        "Phew! Good work. Now we're set.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xB,
        (
            "Whether I can make a meal that'll satisfy the\x01",
            "old man or not... The rest is up to my skill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xB,
        "All riiight! Bang a gong, we are on!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_8E(0xB, 0x8F20, 0x0, 0x1EE74, 0x7D0, 0x0)
    OP_8E(0xB, 0x8F20, 0x0, 0x1E8D4, 0x7D0, 0x0)
    OP_8C(0xB, 270, 400)
    OP_0D()
    OP_22(0x13, 0x0, 0x64)
    OP_22(0xCA, 0x0, 0x64)
    SetChrSubChip(0x13, 6)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x11, 36530, 0, 74730, 180)
    OP_4A(0x11, 255)
    SetChrPos(0x101, 36500, 0, 73200, 0)
    SetChrPos(0x103, 37870, 0, 73310, 315)
    SetChrPos(0xF8, 37500, 0, 72090, 0)
    SetChrPos(0xF9, 36500, 0, 71860, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3337")
    SetChrPos(0xF9, 37500, 0, 72090, 0)
    SetChrPos(0xF8, 36500, 0, 71860, 0)

    label("loc_3337")

    SetChrPos(0xB, 33950, 0, 75000, 90)
    OP_4A(0xB, 255)
    SetChrPos(0xA, 33590, 0, 75990, 120)
    OP_4A(0xC, 255)
    SetChrPos(0xC, 33500, 0, 76920, 120)
    OP_4A(0xA, 255)
    SetChrPos(0x12, 45380, 0, 70160, 300)
    Sleep(5000)
    OP_6D(24580, 0, 77920, 0)
    OP_67(0, 5980, -10000, 0)
    OP_6B(2950, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)

    def lambda_33CF():
        OP_6D(34820, 0, 74740, 4000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_33CF)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x11, 0x1)

    ChrTalk(    #166
        0x11,
        "#4P...I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x11,
        "#4PSo you couldn't find the original recipe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x101,
        (
            "#1003F#1PYeah. I'm really sorry.\x02\x03",

            "We asked a lot of people, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x103,
        (
            "#026F#2PIn the end, we never found anyone who\x01",
            "knew it. We're terribly sorry, sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x11,
        (
            "#4PNo, no, ultimately it was my selfish request,\x01",
            "anyway...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x11,
        "#4PYou don't need to be so worried.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x11,
        (
            "#4PWell, I'll admit it's a bit sad to know I'll\x01",
            "never taste that flavor again, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xB,
        "#3PBut, Radford...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xB,
        "#3PIt might be a bit early to give up.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0xB, 400)

    ChrTalk(    #175
        0x11,
        "#4POh...?!\x02",
    )

    CloseMessageWindow()

    def lambda_35FB():
        TurnDirection(0xF6, 0xB, 400)
        ExitThread()

    QueueWorkItem(0xF6, 1, lambda_35FB)
    Sleep(100)

    def lambda_360E():
        OP_8C(0xF7, 270, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_360E)

    def lambda_361C():
        TurnDirection(0xF8, 0xB, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_361C)
    Sleep(100)

    def lambda_362F():
        TurnDirection(0xF9, 0xB, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_362F)

    ChrTalk(    #176
        0xB,
        (
            "#3PI'm sure the meal I made will\x01",
            "be close to that flavor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xB,
        (
            "#3PThe recipe you guys brought\x01",
            "still has a nostalgic flavor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xA,
        (
            "Yes, yes, and while you all\x01",
            "are talking it's getting cold.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_36FE():
        OP_8C(0x101, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36FE)
    Sleep(100)

    def lambda_3711():
        OP_8C(0xF7, 315, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_3711)

    def lambda_371F():
        OP_8C(0xF8, 0, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_371F)
    Sleep(100)

    def lambda_3732():
        OP_8C(0xF9, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3732)
    TurnDirection(0x11, 0xB, 400)

    ChrTalk(    #179
        0x101,
        (
            "#1P#1016FAhaha, yeah.\x02\x03",

            "It looks pretty good! You should\x01",
            "eat it while it's hot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x103,
        (
            "#025FReally, I'd like you to think of us\x01",
            "watching on the sidelines.\x02\x03",

            "I've been sitting here dealing with\x01",
            "such a lovely smell for a while now.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3867")

    ChrTalk(    #181
        0x107,
        "#067FHeehee... My stomach is rumbling...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A73")

    label("loc_3867")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38FF")

    ChrTalk(    #182
        0x106,
        (
            "#551FYeah, it really does smell good.\x02\x03",

            "#550FDamn... Now I'm hungry.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #183
        0x101,
        "#2P#1019FWhy the heck are you angry about that...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A73")

    label("loc_38FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_398A")

    ChrTalk(    #184
        0x108,
        "#071FHaha, now I'm getting a bit peckish myself.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(    #185
        0x101,
        (
            "#2P#1007F'Peckish' sounds weird coming\x01",
            "out of you, Zin.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A73")

    label("loc_398A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A73")

    ChrTalk(    #186
        0x104,
        (
            "#031FHmmm, such a delectable bouquet.\x01",
            "Quite the scent to lure out an appetite.\x02\x03",

            "#037FNow, if only there was a fitting wine,\x01",
            "that would be the crowning touch...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #187
        0x101,
        "#2P#1007FI'm dying for a taste of this...\x02",
    )

    CloseMessageWindow()

    label("loc_3A73")

    TurnDirection(0x11, 0x101, 400)

    ChrTalk(    #188
        0x11,
        "#4PAh, we got to talking a bit too much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x11,
        "#4PWell, then let me have at it.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 270, 400)

    def lambda_3ADB():
        OP_6D(34820, 0, 74740, 1500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3ADB)

    def lambda_3AF3():
        TurnDirection(0xF6, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xF6, 1, lambda_3AF3)
    Sleep(100)

    def lambda_3B06():
        TurnDirection(0xF7, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_3B06)

    def lambda_3B14():
        TurnDirection(0xF8, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_3B14)
    Sleep(100)

    def lambda_3B27():
        TurnDirection(0xF9, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3B27)
    Sleep(1000)

    ChrTalk(    #190
        0x11,
        "#4P*slurp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x11,
        "#4P*chew chew*\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #192
        0x101,
        "#1002F#1P*g-gulp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xB,
        "#3P(Th-This is a bit nerve-racking.)\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x11)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #194
        0x11,
        "#4PHmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x11,
        "#4P...I know this flavor...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x101,
        "#1002F#1PWh-What is it?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 180, 400)

    ChrTalk(    #197
        0x11,
        "#4PThis... This is it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x11,
        (
            "#3S#4PThis is the stew I ate in my dreams!\x01",
            "Wahoooooooooo!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D39")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3D77")

    label("loc_3D39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D60")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3D77")

    label("loc_3D60")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3D77")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D9E")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3DDC")

    label("loc_3D9E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DC5")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3DDC")

    label("loc_3DC5")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3DDC")


    ChrTalk(    #199
        0x103,
        "#023FOh, my...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xA,
        "*gasp*\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E1D")

    ChrTalk(    #201
        0x108,
        "#073FOh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E88")

    label("loc_3E1D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E46")

    ChrTalk(    #202
        0x106,
        "#052FSeriously...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E88")

    label("loc_3E46")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E67")

    ChrTalk(    #203
        0x105,
        "#044FMy...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E88")

    label("loc_3E67")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E88")

    ChrTalk(    #204
        0x104,
        "#033FHo ho...\x02",
    )

    CloseMessageWindow()

    label("loc_3E88")


    ChrTalk(    #205
        0xC,
        "R-Really?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0xC, 400)

    ChrTalk(    #206
        0x11,
        "#4PY-Yes, really.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x11,
        (
            "#4PIt's not even slightly different from\x01",
            "the nostalgic flavor I remember.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x11,
        (
            "#4PWhat I wanted to eat--what I DREAMED\x01",
            "of eating--was exactly this.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #209
        0x101,
        (
            "#1001FThat's incredible, Densel!\x02\x03",

            "You perfectly replicated a recipe from a dream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xB,
        (
            "#3PH-Hmm... I mean, I was pretty\x01",
            "confident in it, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xB,
        "#3PThat's a bit too generous.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0xB, 400)

    ChrTalk(    #212
        0x11,
        "#4PNo, no, don't be humble.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x11, 400)

    ChrTalk(    #213
        0x11,
        (
            "#4PThe meal is perfect. This is\x01",
            "what I wanted in every way.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 0, 400)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x11)

    ChrTalk(    #214
        0x11,
        "#6PAh, it brings me back...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x11,
        "#6PTo those lost days of my youth...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x11,
        (
            "#6PThe girl I admired was ever so\x01",
            "good at this recipe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x11,
        "#6PI shed many manly tears the day she wed...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #218
        0x101,
        "#1016F#1PW-Well, this is getting a bit soppy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xC,
        "Huh. Never heard of that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xC,
        (
            "Sounds like you were quite the passionate\x01",
            "one in your youth, old guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x103,
        "#021FThat's the beauty of youth.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 180, 400)

    ChrTalk(    #222
        0x11,
        "#4PThe beauty of youth, indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x11,
        "#4PEverything, everything, has changed since then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x11,
        "#4PEven that angel of a girl is now a dried apricot.\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    ClearChrFlags(0x12, 0x80)
    OP_4A(0x12, 255)
    SetChrPos(0x12, 44480, 0, 71450, 270)

    NpcTalk(    #225
        0x12,
        "Old Woman's Voice",
        (
            "#5PWho're you calling a 'dried apricot,'\x01",
            "you old fart?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_434B():

        label("loc_434B")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_434B")

    QueueWorkItem2(0x101, 3, lambda_434B)

    def lambda_435C():

        label("loc_435C")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_435C")

    QueueWorkItem2(0x103, 3, lambda_435C)

    def lambda_436D():

        label("loc_436D")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_436D")

    QueueWorkItem2(0xF8, 3, lambda_436D)

    def lambda_437E():

        label("loc_437E")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_437E")

    QueueWorkItem2(0xF9, 3, lambda_437E)

    def lambda_438F():

        label("loc_438F")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_438F")

    QueueWorkItem2(0xB, 3, lambda_438F)

    def lambda_43A0():

        label("loc_43A0")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_43A0")

    QueueWorkItem2(0xC, 3, lambda_43A0)

    def lambda_43B1():

        label("loc_43B1")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_43B1")

    QueueWorkItem2(0xA, 3, lambda_43B1)
    OP_8C(0x11, 90, 400)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x11)

    ChrTalk(    #226
        0x11,
        "#6PTh-That voice is...\x02",
    )

    CloseMessageWindow()
    OP_6D(40740, 0, 75420, 3000)
    Sleep(1000)

    def lambda_441A():
        OP_6D(35940, 0, 74450, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_441A)
    OP_8E(0x12, 0x9DDA, 0x0, 0x12354, 0x7D0, 0x0)
    OP_8E(0x12, 0x9628, 0x0, 0x123F4, 0x7D0, 0x0)
    OP_44(0x101, 0x3)
    OP_44(0x103, 0x3)
    OP_44(0xF8, 0x3)
    OP_44(0xF9, 0x3)
    OP_44(0xB, 0x3)
    OP_44(0xC, 0x3)
    OP_44(0xA, 0x3)

    ChrTalk(    #227
        0xB,
        "Miss Bloom...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x12,
        (
            "Really, to badmouth a lady in front\x01",
            "of such a crowd...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x12,
        "You're as twisted an old man as ever, you.\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_63(0x11)

    ChrTalk(    #230
        0x11,
        "#6PN-No, it was just a play on words...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xB,
        (
            "What is it, ma'am?\x01",
            "We don't see you here much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xA,
        "#6PYeah, yeah, it's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x12,
        (
            "These people came by my home to ask\x01",
            "about the recipe a bit ago, and, well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x12,
        "I was curious, so I came by to see.\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0xB)

    ChrTalk(    #235
        0xB,
        "Huh, so this recipe's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x12,
        (
            "Yes, it's a cooking style passed down\x01",
            "in my family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x12,
        "This stew was my best recipe when I was a girl.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x12,
        "I made it often for Radford here.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #239
        0x101,
        "#1004FSo, that means...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xA,
        "#6PThe girl this old man admired was...\x02",
    )

    CloseMessageWindow()

    def lambda_4745():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4745)
    Sleep(150)

    def lambda_4758():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_4758)

    def lambda_4766():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_4766)
    Sleep(150)

    def lambda_4779():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xF8, 3, lambda_4779)

    def lambda_4787():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xF9, 3, lambda_4787)
    Sleep(1000)
    OP_62(0x11, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #241
        0x11,
        "#6P*cough*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x11,
        "#6P*siiigh* Time is a cruel master, indeed...\x02",
    )

    CloseMessageWindow()

    def lambda_47F9():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_47F9)

    def lambda_4807():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_4807)

    def lambda_4815():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0xF8, 3, lambda_4815)

    def lambda_4823():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0xF9, 3, lambda_4823)
    Sleep(1000)
    TurnDirection(0x12, 0x101, 400)

    ChrTalk(    #243
        0x12,
        "Hmm? What did you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x101,
        "#1016FN-Nothing...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x11, 400)

    ChrTalk(    #245
        0x12,
        "Well, one way or the other...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x12,
        (
            "I'm just happy to see people eating\x01",
            "this old recipe again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x12,
        (
            "Here, since I've come down all this way,\x01",
            "let me make it for the first time in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x12,
        (
            "You all should enjoy the flavor\x01",
            "of tradition yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x101,
        "#1018FHooray! Don't mind if I do. ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xB,
        "Yeah, please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xB,
        (
            "I'd love the chance to observe some\x01",
            "of the tricks to this recipe firsthand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x12,
        "Well, then, let me borrow the kitchen.\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_28(0x75, 0x1, 0x1000)
    OP_28(0x75, 0x4, 0x10)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A9C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x20)"), scpexpr(EXPR_END)), "loc_4A5E")
    Jump("loc_4A9C")

    label("loc_4A5E")

    OP_AC(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #253
        "\x06Learned [#2CPepper Pottage#0W] recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_4A9C")

    OP_3F(0x236, 1)
    Sleep(400)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x17, 0x0, 0x64)

    AnonymousTalk(    #254
        "Quest #2C[Nostalgic Recipe] #0Ccompleted!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    NewScene("ED6_DT21/T0100   ._SN", 114, 0, 0)
    IdleLoop()
    Return()

    # Function_7_30F2 end

    SaveToFile()

Try(main)
