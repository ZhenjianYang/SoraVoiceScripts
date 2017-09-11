from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C2209_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C2200.x',
        MapIndex            = 84,
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
    )

    ScpFunction(
        "Function_0_66",           # 00, 0
        "Function_1_9D",           # 01, 1
        "Function_2_E7C",          # 02, 2
        "Function_3_1C8A",         # 03, 3
        "Function_4_1F3F",         # 04, 4
        "Function_5_270F",         # 05, 5
        "Function_6_2C0C",         # 06, 6
        "Function_7_3323",         # 07, 7
        "Function_8_4CEF",         # 08, 8
        "Function_9_4D01",         # 09, 9
        "Function_10_4D53",        # 0A, 10
        "Function_11_4DA5",        # 0B, 11
        "Function_12_4DF7",        # 0C, 12
        "Function_13_4DFF",        # 0D, 13
        "Function_14_4E14",        # 0E, 14
        "Function_15_4E3D",        # 0F, 15
        "Function_16_4E66",        # 10, 16
    )


    def Function_0_66(): pass

    label("Function_0_66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_98")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E")
    OP_A2(0x0)
    Call(1, 1)
    Jump("loc_95")

    label("loc_8E")

    OP_A2(0x0)
    Call(1, 2)

    label("loc_95")

    Jump("loc_9C")

    label("loc_98")

    Call(1, 4)

    label("loc_9C")

    Return()

    # Function_0_66 end

    def Function_1_9D(): pass

    label("Function_1_9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x40)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B2")
    Return()

    label("loc_B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E7B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_D6")
    Call(1, 2)
    Jump("loc_E7B")

    label("loc_D6")

    SetChrFlags(0x8, 0x10)
    TalkBegin(0x8)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_51(0x9, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DEE")
    OP_28(0x1C, 0x4, 0x2)
    OP_28(0x1C, 0x4, 0x4)
    OP_28(0x1C, 0x1, 0x1)
    OP_28(0x1C, 0x1, 0x2)
    OP_69(0x9, 0x7D0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21E")
    Sleep(1000)

    ChrTalk(    #0
        0x8,
        "Hmm...what to do, what to do?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "I wouldn't feel right leaving\x01",
            "the lighthouse unattended to\x01",
            "go get help...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "But on the other hand, I can't\x01",
            "very well leave things as they\x01",
            "are, either...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21E")

    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(    #3
        0x8,
        "My, my, who have we here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "What brings ya to the Varenne\x01",
            "Lighthouse?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#000FNothing much.\x01",
            "Just looking around.\x02\x03",

            "How about you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #6
        0x8,
        (
            "Why, I belong here. I'm the\x01",
            "lighthouse keeper, ya see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "Though I must say, it's not an\x01",
            "easy task maintaining a light-\x01",
            "house of this size.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_428")

    ChrTalk(    #8
        0x8,
        "...Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        "#501FSomething wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "That...emblem on your chest\x01",
            "wouldn't happen to be...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#508FOh, that?\x02\x03",

            "Yeah, we're bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        "#010FJunior bracers, at any rate.\x02",
    )

    CloseMessageWindow()
    Jump("loc_542")

    label("loc_428")

    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #13
        0x8,
        "...Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "Hold on a moment. Let me get\x01",
            "a closer look at that emblem\x01",
            "on your chest...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #15
        0x101,
        "#007FUhh...not TOO close, okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        (
            "#017F(Oh boy...)\x02\x03",

            "#010FThat's correct, sir.\x01",
            "We are, in fact, bracers.\x02\x03",

            "Junior bracers, but bracers\x01",
            "nonetheless.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_542")

    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #17
        0x8,
        (
            "Well, why didn't ya say\x01",
            "so earlier?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "Y'all should rush to the assistance of an\x01",
            "octogenarian in need--not pretend like\x01",
            "ya didn't notice his forlorn expression!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #19
        0x101,
        (
            "#004FEr...what?\x02\x03",

            "What are you talking about, old man?\x01",
            "Why didn't YOU say anything to US?!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #20
        0x8,
        "Because ya didn't ask!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "Shouldn't the first words out of your mouth as\x01",
            "bracers be something like, 'Are ya in need of\x01",
            "any assistance, my elderly friend?'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "I tell ya, young bracers these days\x01",
            "are all fight, no care! Where's the\x01",
            "LOVE? Where's the COMPASSION?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 45, 400)
    Sleep(1000)

    ChrTalk(    #23
        0x8,
        (
            "Y'all are worlds apart from that manly bracer\x01",
            "I worked with before. Now THAT was a bracer\x01",
            "ya could set your clocks by, yesiree!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "I reckon that was...seven years ago?\x01",
            "Eight, perhaps? However long ago\x01",
            "it was...he was better than you two!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#509FUhh... While I can't tell you how much I'm simply\x01",
            "LOVING this abusive lecture of yours, you were\x01",
            "saying something about needing assistance?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #26
        0x8,
        (
            "I was? ...Oh, rightrightright!\x01",
            "Yes, dire need, dire need indeed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "Ya see, I was out cutting the grass\x01",
            "earlier, and silly me, I forgot to\x01",
            "shut the door when I left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "And wouldn't ya know it, by the\x01",
            "time I got back there were monsters!\x01",
            "Monsters all over the place!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "And with monsters skittering\x01",
            "about, I daren't go back in\x01",
            "there. I'm not THAT senile yet!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#006FSo basically, you want us to\x01",
            "exterminate the monsters, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        "That's the idea, yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "Don't know how many of them\x01",
            "there are, though, so try not\x01",
            "to die, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#505FUh, okay. We'll definitely do that! I do\x01",
            "have to wonder, though, why monsters\x01",
            "would wander into a lighthouse...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    TurnDirection(0x101, 0x102, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BFC")
    TurnDirection(0x105, 0x102, 400)
    Jump("loc_C10")

    label("loc_BFC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C10")
    TurnDirection(0x136, 0x102, 400)

    label("loc_C10")


    ChrTalk(    #34
        0x102,
        (
            "#010FThey're probably drawn\x01",
            "to the septium.\x02\x03",

            "That light is produced by a\x01",
            "particularly large orbment,\x01",
            "as you might imagine.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #35
        0x8,
        "Spot on, whippersnapper.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x102, 0x8, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CDA")
    TurnDirection(0x105, 0x8, 400)
    Jump("loc_CEE")

    label("loc_CDA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CEE")
    TurnDirection(0x136, 0x8, 400)

    label("loc_CEE")


    ChrTalk(    #36
        0x8,
        (
            "When this happened before, the\x01",
            "monsters were all gathered together\x01",
            "at the top.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#000FOh. Well, that makes sense.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(    #38
        0x8,
        (
            "Well, if it makes sense, then get going,\x01",
            "girl! Use that brutish body of yours\x01",
            "and show those monsters what's what!\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 3)
    Jump("loc_E78")

    label("loc_DEE")

    OP_69(0x9, 0x3E8)
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(    #39
        0x8,
        (
            "Well, if it makes sense, then get going,\x01",
            "girl! Use that brutish body of yours\x01",
            "and show those monsters what's what!\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 3)

    label("loc_E78")

    TalkEnd(0x8)

    label("loc_E7B")

    Return()

    # Function_1_9D end

    def Function_2_E7C(): pass

    label("Function_2_E7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C89")
    SetChrFlags(0x8, 0x10)
    TalkBegin(0x8)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_51(0x9, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BF9")
    OP_28(0x1C, 0x4, 0x2)
    OP_28(0x1C, 0x4, 0x4)
    OP_28(0x1C, 0x1, 0x1)
    OP_28(0x1C, 0x1, 0x2)
    OP_28(0x1C, 0x1, 0x4)
    OP_28(0x1D, 0x1, 0x8)
    OP_28(0x1D, 0x1, 0x1000)
    OP_69(0x9, 0x7D0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE1")
    Sleep(1000)

    ChrTalk(    #40
        0x8,
        "Hmm...what to do, what to do?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        (
            "I wouldn't feel right leaving\x01",
            "the lighthouse unattended to\x01",
            "go get help...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "But on the other hand, I can't\x01",
            "very well leave things as they\x01",
            "are, either...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE1")

    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(    #43
        0x8,
        "My, my, who have we here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "What brings ya to the Varenne\x01",
            "Lighthouse?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#000FAre you, by any chance, the\x01",
            "lighthouse keeper, Vogt?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #46
        0x8,
        "Ho-ho! I certainly am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "That...emblem on your chest...\x01",
            "wouldn't happen to be...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#508FOh, that?\x02\x03",

            "Yeah, we're bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x102,
        "#010FJunior bracers, at any rate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "Well, why didn't ya say so\x01",
            "earlier?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        (
            "Y'all should rush to the assistance of an\x01",
            "octogenarian in need--not pretend like\x01",
            "ya didn't notice his forlorn expression!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #52
        0x101,
        (
            "#004FEr...what?\x02\x03",

            "What are you talking about, old man?\x01",
            "Why didn't YOU say anything to US?!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #53
        0x8,
        "Because ya didn't ask!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        (
            "Shouldn't the first words out of your mouth as\x01",
            "bracers be something like, 'Are ya in need of\x01",
            "any assistance, my elderly friend?'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x8,
        (
            "I tell ya, young bracers these days\x01",
            "are all fight, no care! Where's the\x01",
            "LOVE? Where's the COMPASSION?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 45, 400)
    Sleep(1000)

    ChrTalk(    #56
        0x8,
        (
            "Y'all are worlds apart from that manly bracer\x01",
            "I worked with before. Now THAT was a bracer\x01",
            "ya could set your clocks by, yesiree!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "I reckon that was...seven years ago?\x01",
            "Eight, perhaps? However long ago\x01",
            "it was...he was better than you two!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        (
            "#509FUhh... While I can't tell you how much I'm simply\x01",
            "LOVING this abusive lecture of yours, you were\x01",
            "saying something about needing assistance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x105,
        (
            "#045F(He really is just as the\x01",
            "factory owner said...)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #60
        0x8,
        (
            "I was? ...Oh, rightrightright!\x01",
            "Yes, dire need, dire need indeed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        (
            "Ya see, I was out cutting the grass\x01",
            "earlier, and silly me, I forgot to\x01",
            "shut the door when I left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x8,
        (
            "And wouldn't ya know it, by the\x01",
            "time I got back there were monsters!\x01",
            "Monsters all over the place!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x8,
        (
            "And with monsters skittering\x01",
            "about, I daren't go back in\x01",
            "there. I'm not THAT crazy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#002FSo before we hand over the maintenance kit,\x01",
            "you want us to do some good old-fashioned\x01",
            "monster-smashing--is that the gist?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x102,
        (
            "#010FI...think that pretty much goes\x01",
            "without saying, doesn't it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #66
        0x8,
        (
            "Maintenance kit? What in blazes\x01",
            "are ya talking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x102,
        (
            "#010FThat's why we're here. We've come in\x01",
            "response to a request, to deliver a\x01",
            "maintenance kit to this lighthouse.\x02\x03",

            "But clearly, there are bigger\x01",
            "concerns at the moment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x8,
        "Indeed, it's just as ya say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        (
            "Can't exactly do any inspections\x01",
            "if it's not safe in there!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#002FDo you have any idea how many\x01",
            "of them there are?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #71
        0x8,
        (
            "Not in the slightest. All I know is,\x01",
            "it's not just one--so be on your\x01",
            "guard, and don't die!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        (
            "#000FDon't you worry: Bracers never\x01",
            "say die!\x02\x03",

            "#505FI do have to wonder, though, why\x01",
            "monsters would wander into a\x01",
            "lighthouse...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    def lambda_1A2A():
        TurnDirection(0x101, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A2A)

    def lambda_1A38():
        TurnDirection(0x105, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1A38)

    ChrTalk(    #73
        0x102,
        (
            "#010FProbably drawn to the septium.\x02\x03",

            "That light is produced by a\x01",
            "particularly large orbment,\x01",
            "as you might imagine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        "Spot on, whippersnapper.\x02",
    )

    CloseMessageWindow()

    def lambda_1ADC():
        TurnDirection(0x102, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1ADC)

    def lambda_1AEA():
        TurnDirection(0x101, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1AEA)

    def lambda_1AF8():
        TurnDirection(0x105, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1AF8)

    ChrTalk(    #75
        0x8,
        (
            "When this happened before, the\x01",
            "monsters were all gathered together\x01",
            "at the top.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        "#508FOh. Well, that makes sense.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        (
            "Well, if it makes sense, then get going,\x01",
            "girl! Use that brutish body of yours\x01",
            "and show those monsters what's what!\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 3)
    Jump("loc_1C83")

    label("loc_1BF9")

    OP_69(0x9, 0x3E8)
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(    #78
        0x8,
        (
            "Well, if it makes sense, then get going,\x01",
            "girl! Use that brutish body of yours\x01",
            "and show those monsters what's what!\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 3)

    label("loc_1C83")

    TalkEnd(0x8)
    Jump("loc_1C89")

    label("loc_1C89")

    Return()

    # Function_2_E7C end

    def Function_3_1C8A(): pass

    label("Function_3_1C8A")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Help the old man]\x01",      # 0
            "[Don't do it]\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1CFC"),
        (1, "loc_1E56"),
        (SWITCH_DEFAULT, "loc_1F32"),
    )


    label("loc_1CFC")

    OP_28(0x1C, 0x4, 0x8)
    OP_28(0x1C, 0x1, 0x4)

    ChrTalk(    #79
        0x101,
        "#006FYou bet. Let's do it to it!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #80
        0x8,
        (
            "It's almost inspection time, so please,\x01",
            "take care of these...these THINGS as\x01",
            "quickly as ya can, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x8,
        (
            "And make sure ya don't let your\x01",
            "guard down, as those things are\x01",
            "pretty nimble!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x102,
        "#012FUnderstood.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #83
        0x101,
        "#002FI'm ready. Let's do this thing!\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_21()
    NewScene("ED6_DT01/C2219   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1F32")

    label("loc_1E56")


    ChrTalk(    #84
        0x101,
        (
            "#505FI'm really sorry, but we can't\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #85
        0x8,
        (
            "Inspection time is right around\x01",
            "the corner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x8,
        (
            "I need y'all to take care of this\x01",
            "as soon as ya possibly can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        "#000FOkay. We'll see what we can do.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F32")

    label("loc_1F32")

    EventEnd(0x1)
    TalkEnd(0x8)
    OP_8C(0x8, 0, 0)
    Return()

    # Function_3_1C8A end

    def Function_4_1F3F(): pass

    label("Function_4_1F3F")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_24C3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_21A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2065")
    OP_A2(0x0)

    ChrTalk(    #88
        0x8,
        "Oh-ho, welcome back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x8,
        "How did the monster-busting go?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #90
        0x101,
        (
            "#505FLooks like it's going to take\x01",
            "just a little more time yet.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #91
        0xFE,
        (
            "I see. Well, do hurry,\x01",
            "if you'd please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x8,
        (
            "Can't exactly do any inspections\x01",
            "if it's not safe in there!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_219F")

    label("loc_2065")


    ChrTalk(    #93
        0x8,
        (
            "What treachery is this? Are ya, perhaps,\x01",
            "intending to go off on some other job,\x01",
            "leaving me alone and defenseless?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x8,
        (
            "Well, I suppose y'all ARE bracers. An urgent\x01",
            "mission or two is to be expected every now\x01",
            "and again. Just...hurry back, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x8,
        (
            "Can't exactly do any inspections\x01",
            "if it's not safe in there!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_219F")

    Jump("loc_24C0")

    label("loc_21A2")

    OP_28(0x1D, 0x1, 0x1000)

    ChrTalk(    #96
        0x8,
        "Oh-ho, welcome back!\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #97
        0x8,
        "Hmm? And what's this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x8,
        (
            "I see a rather large kit in your\x01",
            "hands there. Is that...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        (
            "#000FYep. Maintenance kit-o-rama.\x02\x03",

            "Full of tools you need for your\x01",
            "inspection, no doubt!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x8,
        (
            "Excellent, excellent! It is that\x01",
            "time of the year, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x102,
        (
            "#010FWe came to deliver this kit to\x01",
            "you, as per the request.\x02\x03",

            "But with things as they are, it looks\x01",
            "like you might have a tough time doing\x01",
            "much of anything in there...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #102
        0x8,
        "Indeed, it's just as ya say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x8,
        (
            "Can't exactly do any inspections\x01",
            "if it's not safe in there!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#002FSo I guess we really do need to\x01",
            "get rid of those monsters before\x01",
            "you can get back to work!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #105
        0xFE,
        (
            "Yes, please. As soon as ya can.\x01",
            "I really do have a lot to do!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        "Your help is appreciated.\x02",
    )

    CloseMessageWindow()

    label("loc_24C0")

    Jump("loc_270B")

    label("loc_24C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25D1")
    OP_A2(0x0)

    ChrTalk(    #107
        0x8,
        "Oh-ho, welcome back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x8,
        "How did the monster-busting go?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #109
        0x101,
        (
            "#505FLooks like it's going to take\x01",
            "just a little more time yet.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #110
        0xFE,
        (
            "I see. Well, do hurry,\x01",
            "if you'd please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "Can't exactly do any inspections\x01",
            "if it's not safe in there!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_270B")

    label("loc_25D1")


    ChrTalk(    #112
        0x8,
        (
            "What treachery is this? Are ya, perhaps,\x01",
            "intending to go off on some other job,\x01",
            "leaving me alone and defenseless?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x8,
        (
            "Well, I suppose y'all ARE bracers. An urgent\x01",
            "mission or two is to be expected every now\x01",
            "and again. Just...hurry back, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "Can't exactly do any inspections\x01",
            "if it's not safe in there!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_270B")

    TalkEnd(0x8)
    Return()

    # Function_4_1F3F end

    def Function_5_270F(): pass

    label("Function_5_270F")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    OP_8C(0x8, 180, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_273C")
    SetChrFlags(0x105, 0x80)
    Jump("loc_274E")

    label("loc_273C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_274E")
    SetChrFlags(0x136, 0x80)

    label("loc_274E")

    SetChrPos(0x101, -20, 750, 2830, 0)
    SetChrPos(0x102, -20, 750, 2830, 0)
    OP_6D(-20, 750, 830, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_27A2")
    SetChrPos(0x105, -20, 750, 2830, 0)
    Jump("loc_27C0")

    label("loc_27A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_27C0")
    SetChrPos(0x136, -20, 750, 2830, 0)

    label("loc_27C0")

    Sleep(2000)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_8C(0x8, 0, 400)
    Sleep(1200)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x50)
    OP_73(0x0)

    def lambda_27FA():

        label("loc_27FA")

        TurnDirection(0x8, 0x101, 0)
        OP_48()
        Jump("loc_27FA")

    QueueWorkItem2(0x8, 1, lambda_27FA)
    OP_43(0x9, 0x1, 0x1, 0x8)
    OP_43(0x101, 0x1, 0x1, 0x9)
    Sleep(500)
    OP_43(0x102, 0x1, 0x1, 0xA)
    Sleep(500)
    OP_43(0x105, 0x1, 0x1, 0xB)
    WaitChrThread(0x102, 0x1)
    Sleep(1000)
    OP_72(0x0, 0x800)
    OP_22(0xD3, 0x0, 0x64)
    OP_6F(0x0, 80)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    OP_71(0x0, 0x800)
    OP_44(0x8, 0xFF)

    ChrTalk(    #115
        0x8,
        "How did the monster-busting go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        (
            "#001FHeh! Stick a fork in it, old man,\x01",
            "because this job is DONE!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x102,
        (
            "#010FThe monsters have all been taken\x01",
            "care of. Everything should be\x01",
            "back to normal in there now.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #118
        0x8,
        "Oh, my! That's splendid news!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x1, 0x1000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B0A")
    OP_28(0x1D, 0x1, 0x1000)

    ChrTalk(    #119
        0x8,
        (
            "Finally, I can put my mind\x01",
            "at ease!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x101,
        (
            "#000FYou sure can.\x02\x03",

            "And now we can give you that\x01",
            "maintenance kit we brought, too!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #121
        0x8,
        "Ehh? Maintenance kit, ya say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x102,
        (
            "#010FThat's why we're here. We've come in\x01",
            "response to a request, to deliver a\x01",
            "maintenance kit to this lighthouse.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #123
        0x8,
        (
            "Oh, I see. Inspection time is\x01",
            "right around the corner, so\x01",
            "that's exactly what I needed!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B99")

    label("loc_2B0A")


    ChrTalk(    #124
        0x8,
        (
            "At long last, I can hold the maintenance kit\x01",
            "in my hands, and use its contents to make this\x01",
            "lighthouse--nay, this world!--a better place.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B99")


    ChrTalk(    #125
        0x8,
        (
            "So, what are we waiting for?\x01",
            "If it's safe now, then let's\x01",
            "get inside, shall we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        "#000FLet's!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/C2219   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_270F end

    def Function_6_2C0C(): pass

    label("Function_6_2C0C")

    OP_28(0x1D, 0x4, 0x10)
    OP_28(0x1D, 0x1, 0x80)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrPos(0x101, 200, 750, 2830, 0)
    SetChrPos(0x102, -500, 750, 2830, 0)
    SetChrPos(0x105, 500, 750, 2830, 0)
    Sleep(2000)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x50)
    OP_73(0x0)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x105, 0x80)

    def lambda_2C8B():
        OP_90(0x101, 0x0, 0x0, 0xFFFFDECC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C8B)
    Sleep(500)

    def lambda_2CAB():
        OP_90(0x102, 0x0, 0x0, 0xFFFFE2B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2CAB)
    Sleep(600)

    def lambda_2CCB():
        OP_90(0x105, 0x0, 0x0, 0xFFFFE69C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2CCB)
    Sleep(1200)
    OP_72(0x0, 0x800)
    OP_22(0xD3, 0x0, 0x64)
    OP_6F(0x0, 80)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    OP_71(0x0, 0x800)
    OP_6D(200, 0, -4800, 3000)
    WaitChrThread(0x105, 0x1)

    ChrTalk(    #127
        0x101,
        "#505F...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #128
        0x101,
        (
            "#002F...So are you thinking what\x01",
            "I'm thinking, Joshua?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #129
        0x102,
        (
            "#010FYeah, I couldn't help but\x01",
            "read into it myself.\x02\x03",

            "Seven or eight years ago WOULD\x01",
            "be right on the money...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #130
        0x105,
        (
            "#040FThe bracer to whom Vogt was\x01",
            "comparing you? The, uh, 'manly'\x01",
            "fellow?\x02\x03",

            "Is it someone you know?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #131
        0x101,
        (
            "#505FYeah, you could say that.\x02\x03",

            "I'm pretty sure he was talking\x01",
            "about our dad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x105,
        "#044FOh?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #133
        0x102,
        (
            "#010FIf that IS who he was talking about,\x01",
            "though, then of course we're not going\x01",
            "to measure up.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 400)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #134
        0x101,
        (
            "#007FYeah, seriously...\x02\x03",

            "...Though I guess we are bracers like him\x01",
            "now, so it's...kind of flattering, in a way,\x01",
            "to be compared to him at all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x102,
        (
            "#010FIf we want to make names for ourselves like him,\x01",
            "though, we really have to take it one step at a\x01",
            "time. Catch up bit by bit, day by day.\x02\x03",

            "But even then, I think he's\x01",
            "a little out of our league...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x101,
        (
            "#506FHa ha. Yeah, maybe.\x02\x03",

            "#006FBut I can only believe that one day,\x01",
            "we'll totally outclass him. I mean,\x01",
            "we pretty much rule!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #137
        0x105,
        (
            "#041FHa ha ha. That's a very 'Estellish'\x01",
            "thing to say.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #138
        0x101,
        (
            "#001FHeh. Thanks, I think!\x02\x03",

            "Anyway, we'd best get going. This is no time to\x01",
            "be horsing around. If we're gonna become world-\x01",
            "class bracers, we've gotta get movin'!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x102,
        (
            "#010FYou're absolutely right.\x02\x03",

            "Let's hit the road, and see\x01",
            "where it takes us...\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #140
        "\x07\x00Quest \x07\x02[Lighthouse Monsters] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #141
        "\x07\x00Quest \x07\x02[Maintenance Delivery] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_6_2C0C end

    def Function_7_3323(): pass

    label("Function_7_3323")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    OP_8C(0x8, 180, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3350")
    SetChrFlags(0x105, 0x80)
    Jump("loc_3362")

    label("loc_3350")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3362")
    SetChrFlags(0x136, 0x80)

    label("loc_3362")

    SetChrPos(0x101, -20, 750, 2830, 0)
    SetChrPos(0x102, -20, 750, 2830, 0)
    OP_6D(-20, 750, 830, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_33B6")
    SetChrPos(0x105, -20, 750, 2830, 0)
    Jump("loc_33D4")

    label("loc_33B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_33D4")
    SetChrPos(0x136, -20, 750, 2830, 0)

    label("loc_33D4")

    Sleep(2000)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_8C(0x8, 0, 400)
    Sleep(1200)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x50)
    OP_73(0x0)

    def lambda_340E():

        label("loc_340E")

        TurnDirection(0x8, 0x101, 0)
        OP_48()
        Jump("loc_340E")

    QueueWorkItem2(0x8, 1, lambda_340E)
    OP_43(0x9, 0x1, 0x1, 0x8)
    OP_43(0x101, 0x1, 0x1, 0x9)
    Sleep(500)
    OP_43(0x102, 0x1, 0x1, 0xA)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_344F")
    Sleep(500)
    OP_43(0x105, 0x1, 0x1, 0xB)
    Jump("loc_3468")

    label("loc_344F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3468")
    Sleep(500)
    OP_43(0x136, 0x1, 0x1, 0xB)

    label("loc_3468")

    WaitChrThread(0x102, 0x1)
    Sleep(1000)
    OP_72(0x0, 0x800)
    OP_22(0xD3, 0x0, 0x64)
    OP_6F(0x0, 80)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    OP_71(0x0, 0x800)
    OP_44(0x8, 0xFF)

    ChrTalk(    #142
        0x8,
        "How did the monster-busting go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x101,
        (
            "#001FHeh! Stick a fork in it, old man,\x01",
            "because this job is DONE!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x102,
        (
            "#010FThe monsters have all been taken\x01",
            "care of. Everything should be\x01",
            "back to normal in there now.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #145
        0x8,
        "Oh, my! That's splendid news!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x8,
        (
            "Finally, I can put my mind\x01",
            "at ease!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #147
        0x8,
        (
            "Thank you for all your\x01",
            "hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x8,
        (
            "And don't forget, as ya flex your bracer muscles\x01",
            "in the future, to flex hardest the strongest\x01",
            "muscle of them all: the CARING muscle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x101,
        (
            "#508FWe, uh, certainly will try to do that.\x01",
            "You take care as well, you old fossil!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x102,
        "#010FIf you'll excuse us...\x02",
    )

    CloseMessageWindow()

    def lambda_36F1():

        label("loc_36F1")

        TurnDirection(0x8, 0x101, 0)
        OP_48()
        Jump("loc_36F1")

    QueueWorkItem2(0x8, 1, lambda_36F1)
    SetChrPos(0x9, 300, 750, -5000, 0)
    OP_51(0x9, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x9, 0x1, 0x1, 0xC)
    OP_43(0x101, 0x1, 0x1, 0xD)
    Sleep(300)
    OP_43(0x102, 0x1, 0x1, 0xE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3782")
    Sleep(300)
    OP_43(0x105, 0x1, 0x1, 0xF)
    Jump("loc_379B")

    label("loc_3782")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_379B")
    Sleep(300)
    OP_43(0x136, 0x1, 0x1, 0xF)

    label("loc_379B")


    ChrTalk(    #151
        0x8,
        "...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)
    OP_44(0x8, 0xFF)

    ChrTalk(    #152
        0x8,
        (
            "...Hey! Just what do ya\x01",
            "think you're doing?!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    def lambda_37FC():
        TurnDirection(0x101, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_37FC)

    def lambda_380A():
        TurnDirection(0x102, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_380A)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3830")

    def lambda_3825():
        TurnDirection(0x105, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3825)
    Jump("loc_384B")

    label("loc_3830")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_384B")

    def lambda_3843():
        TurnDirection(0x136, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_3843)

    label("loc_384B")


    ChrTalk(    #153
        0x101,
        "#501F???\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x8,
        "Aren't y'all...forgetting something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x101,
        "#505FHuh? Uh, I don't think so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x8,
        (
            "What about, 'Is there anything\x01",
            "else we can do for ya before\x01",
            "we go, my good man?'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x101,
        "#004FUhhh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x8,
        (
            "I'm not hearing it. Observe my mouth,\x01",
            "and mimic its movements: 'Is. There.\x01",
            "Anything. Else. We. Can. Do...'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x8,
        (
            "Ya get the picture! It's proper etiquette--\x01",
            "nay, proper CARING--to check with your client\x01",
            "to ensure there are no other issues!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3AB9")
    OP_62(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #160
        0x105,
        (
            "#043F(Oh, my... I guess being a\x01",
            "bracer has its downsides,\x01",
            "just like anything else.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B43")

    label("loc_3AB9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3B3E")
    OP_62(0x136, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #161
        0x136,
        (
            "#043F(Oh, my... I guess being a\x01",
            "bracer has its downsides,\x01",
            "just like anything else.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B43")

    label("loc_3B3E")

    Sleep(1000)

    label("loc_3B43")


    ChrTalk(    #162
        0x8,
        (
            "That dashing young lad who helped me before\x01",
            "certainly knew how to leave a good impression.\x01",
            "Y'all could've learned a thing or two from him!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x8,
        (
            "Hard to believe you're in the same\x01",
            "organization that he was. Like\x01",
            "comparing Poms to a dragon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x101,
        (
            "#009FYou're really trying my patience,\x01",
            "you old windbag.\x02\x03",

            "If that 'dashing' young man really was\x01",
            "Aidios' gift to bracers, then why don't\x01",
            "you give us a few pointers, hmm?\x02\x03",

            "Tell us more about this man-crush of\x01",
            "yours, so we can better ourselves in\x01",
            "his image and get you off our backs!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x8,
        (
            "Oh, he's just a dapper fellow who\x01",
            "came to lend me a hand seven or\x01",
            "eight years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x8,
        (
            "But what a man he was! Far different\x01",
            "from you, girl, that's for sure. He was a\x01",
            "REAL bracer, not some cheap imitation!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x8,
        (
            "In fact, the only way in which I could\x01",
            "POSSIBLY compare the two of you would\x01",
            "be...hair color, I suppose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x8,
        (
            "The same sort of reddish-brown.\x01",
            "Exact same, in fact!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #169
        0x8,
        (
            "Hmm...and looking closely, I'd\x01",
            "say the color of your eyes is\x01",
            "about the same, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x102,
        (
            "#014FReddish-brown hair...and the same\x01",
            "color eyes as Estelle...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x101,
        (
            "#004FW-Wait...\x01",
            "Are you talking about...?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3FD4")
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #172
        0x105,
        "#044F?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FF4")

    label("loc_3FD4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3FF4")
    TurnDirection(0x136, 0x101, 400)

    ChrTalk(    #173
        0x136,
        "#044F?\x02",
    )

    CloseMessageWindow()

    label("loc_3FF4")


    ChrTalk(    #174
        0x8,
        (
            "I was really hoping you'd be just\x01",
            "like him, when ya said y'all were\x01",
            "bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x8,
        (
            "But, I guess that was just wishful\x01",
            "thinking. I doubt anyone could be\x01",
            "as amazing as that man was...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_40C5")
    TurnDirection(0x105, 0x8, 400)
    Jump("loc_40D9")

    label("loc_40C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_40D9")
    TurnDirection(0x136, 0x8, 400)

    label("loc_40D9")


    ChrTalk(    #176
        0x8,
        (
            "Can't hurt to try, though. Be\x01",
            "diligent, and maybe you'll be\x01",
            "a real bracer one day yourself!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #177
        0x8,
        (
            "And even if you're not dashing, ya did help me\x01",
            "out, and I am truly grateful. Always remember\x01",
            "to care for your clients, and...you'll do fine.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_41D9():

        label("loc_41D9")

        TurnDirection(0x101, 0x8, 0)
        OP_48()
        Jump("loc_41D9")

    QueueWorkItem2(0x101, 1, lambda_41D9)

    def lambda_41EA():

        label("loc_41EA")

        TurnDirection(0x102, 0x8, 0)
        OP_48()
        Jump("loc_41EA")

    QueueWorkItem2(0x102, 1, lambda_41EA)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4216")

    def lambda_4208():

        label("loc_4208")

        TurnDirection(0x105, 0x8, 0)
        OP_48()
        Jump("loc_4208")

    QueueWorkItem2(0x105, 1, lambda_4208)
    Jump("loc_4234")

    label("loc_4216")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4234")

    def lambda_4229():

        label("loc_4229")

        TurnDirection(0x136, 0x8, 0)
        OP_48()
        Jump("loc_4229")

    QueueWorkItem2(0x136, 1, lambda_4229)

    label("loc_4234")

    OP_8E(0x8, 0x0, 0x2EE, 0xFFFFFB6E, 0x7D0, 0x0)
    OP_8C(0x8, 0, 0)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x50)
    OP_73(0x0)
    OP_8E(0x8, 0xFFFFFFEC, 0x2EE, 0xB0E, 0x7D0, 0x0)
    OP_72(0x0, 0x800)
    OP_22(0xD3, 0x0, 0x64)
    OP_6F(0x0, 80)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    OP_71(0x0, 0x800)
    SetChrFlags(0x8, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_42B5")
    OP_44(0x105, 0xFF)
    Jump("loc_42C6")

    label("loc_42B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_42C6")
    OP_44(0x136, 0xFF)

    label("loc_42C6")

    Sleep(1000)

    ChrTalk(    #178
        0x101,
        (
            "#002F...\x02\x03",

            "...So, what do you think?\x01",
            "Was he talking about...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #179
        0x102,
        (
            "#010FYeah, I couldn't help but\x01",
            "read into it myself.\x02\x03",

            "Seven or eight years ago WOULD\x01",
            "be right on the money...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_44D8")
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #180
        0x105,
        (
            "#040FThe bracer to whom Vogt was\x01",
            "comparing you? The, uh, 'manly'\x01",
            "fellow?\x02\x03",

            "Is it someone you know?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #181
        0x101,
        (
            "#505FYeah, you could say that.\x02\x03",

            "I'm pretty sure he was talking\x01",
            "about our dad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x105,
        "#044FOh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x102,
        (
            "#010FIf that IS who he was talking about,\x01",
            "though, then of course we're not going\x01",
            "to measure up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46B1")

    label("loc_44D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4623")
    TurnDirection(0x136, 0x101, 400)

    ChrTalk(    #184
        0x136,
        (
            "#040FThe bracer to whom Vogt was\x01",
            "comparing you? The, uh, 'manly'\x01",
            "fellow?\x02\x03",

            "Is it someone you know?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x136, 400)

    ChrTalk(    #185
        0x101,
        (
            "#505FYeah, you could say that.\x02\x03",

            "I'm pretty sure he was talking\x01",
            "about our dad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x136,
        "#044FOh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x102,
        (
            "#010FIf that IS who he was talking about,\x01",
            "though, then of course we're not going\x01",
            "to measure up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46B1")

    label("loc_4623")


    ChrTalk(    #188
        0x101,
        (
            "#004FSo...he WAS talking about\x01",
            "our dad, then, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x102,
        (
            "#010FI think so.\x02\x03",

            "If so, though, then of course we're\x01",
            "not going to measure up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46B1")

    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #190
        0x101,
        (
            "#007FYeah, seriously...\x02\x03",

            "...Though I guess we are bracers like him\x01",
            "now, so it's...kind of flattering, in a way,\x01",
            "to be compared to him at all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x102,
        (
            "#010FIf we want to make names for ourselves like him,\x01",
            "though, we really have to take it one step at a\x01",
            "time. Catch up bit by bit, day by day.\x02\x03",

            "But even then, I think he's\x01",
            "a little out of our league...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_49A1")

    ChrTalk(    #192
        0x101,
        (
            "#506FHa ha. Yeah, maybe.\x02\x03",

            "#006FBut I can only believe that one day,\x01",
            "we'll totally outclass him. I mean,\x01",
            "we pretty much rule!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #193
        0x105,
        (
            "#041FHa ha ha. That's a very 'Estellish'\x01",
            "thing to say.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #194
        0x101,
        (
            "#001FHeh. Thanks, I think!\x02\x03",

            "#508FAnyway, we'd best get going. This is no time to\x01",
            "be horsing around. If we're gonna become world-\x01",
            "class bracers, we've gotta get movin'!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C34")

    label("loc_49A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4B2A")

    ChrTalk(    #195
        0x101,
        (
            "#506FHa ha. Yeah, maybe.\x02\x03",

            "#006FBut I can only believe that one day,\x01",
            "we'll totally outclass him. I mean,\x01",
            "we pretty much rule!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x136, 0x101, 400)

    ChrTalk(    #196
        0x136,
        (
            "#041FHa ha ha. That's a very 'Estellish'\x01",
            "thing to say.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x136, 400)

    ChrTalk(    #197
        0x101,
        (
            "#001FHeh. Thanks, I think!\x02\x03",

            "#508FAnyway, we'd best get going. This is no time to\x01",
            "be horsing around. If we're gonna become world-\x01",
            "class bracers, we've gotta get movin'!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C34")

    label("loc_4B2A")


    ChrTalk(    #198
        0x101,
        (
            "#506FHa ha. Yeah, maybe.\x02\x03",

            "#006FBut I can only believe that one day,\x01",
            "we'll totally outclass him. I mean,\x01",
            "we pretty much rule!\x02\x03",

            "Anyway, we'd best get going. This is no time to\x01",
            "be horsing around. If we're gonna become world-\x01",
            "class bracers, we've gotta get movin'!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C34")


    ChrTalk(    #199
        0x102,
        (
            "#010FYou're absolutely right.\x02\x03",

            "Let's hit the road, and see\x01",
            "where it takes us...\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #200
        "\x07\x00Quest \x07\x02[Lighthouse Monsters] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    ClearMapFlags(0x400000)
    Return()

    # Function_7_3323 end

    def Function_8_4CEF(): pass

    label("Function_8_4CEF")

    OP_6D(-750, 750, -2430, 2000)
    Return()

    # Function_8_4CEF end

    def Function_9_4D01(): pass

    label("Function_9_4D01")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4D17():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4D17)
    OP_8E(0xFE, 0x0, 0x2EE, 0xFFFFFB6E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFD12, 0x2EE, 0xFFFFF682, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 400)
    Return()

    # Function_9_4D01 end

    def Function_10_4D53(): pass

    label("Function_10_4D53")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4D69():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4D69)
    OP_8E(0xFE, 0x0, 0x2EE, 0xFFFFFB6E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFD1C, 0x2EE, 0xFFFFFA24, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 400)
    Return()

    # Function_10_4D53 end

    def Function_11_4DA5(): pass

    label("Function_11_4DA5")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4DBB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4DBB)
    OP_8E(0xFE, 0x0, 0x2EE, 0xFFFFFB6E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x208, 0x2EE, 0xFFFFFACE, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 400)
    Return()

    # Function_11_4DA5 end

    def Function_12_4DF7(): pass

    label("Function_12_4DF7")

    OP_69(0x9, 0x7D0)
    Return()

    # Function_12_4DF7 end

    def Function_13_4DFF(): pass

    label("Function_13_4DFF")

    OP_8E(0xFE, 0x12C, 0x2EE, 0xFFFFEC78, 0x7D0, 0x0)
    Return()

    # Function_13_4DFF end

    def Function_14_4E14(): pass

    label("Function_14_4E14")

    OP_8E(0xFE, 0xFFFFFD12, 0x2EE, 0xFFFFF682, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFDA8, 0x2EE, 0xFFFFF18C, 0x7D0, 0x0)
    Return()

    # Function_14_4E14 end

    def Function_15_4E3D(): pass

    label("Function_15_4E3D")

    OP_8E(0xFE, 0xFFFFFD1C, 0x2EE, 0xFFFFFA24, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFD12, 0x2EE, 0xFFFFF682, 0x7D0, 0x0)
    Return()

    # Function_15_4E3D end

    def Function_16_4E66(): pass

    label("Function_16_4E66")

    Return()

    # Function_16_4E66 end

    SaveToFile()

Try(main)
