from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3111_1 ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3111.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T3111   ._SN',
            'ED6_DT01/T3111_1 ._SN',
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
        "Function_1_7E2",          # 01, 1
    )


    def Function_0_66(): pass

    label("Function_0_66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_238")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_134")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A")
    TurnDirection(0x102, 0x1, 400)
    Jump("loc_A1")

    label("loc_9A")

    TurnDirection(0x102, 0x0, 400)

    label("loc_A1")


    ChrTalk(    #0
        0x102,
        (
            "#010F(Hmm...\x01",
            "No reaction from Antoine yet.)\x02\x03",

            "#010F(More importantly, we need to\x01",
            "check out the factory chief's\x01",
            "office on the second floor.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22D")

    label("loc_134")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #1
        0x102,
        (
            "#010F(We checked it out earlier,\x01",
            "but no reaction.)\x02\x03",

            "#010F(As it stands, we should have\x01",
            "a look inside the workshop.)\x02\x03",

            "#010F(There may be a hint somewhere\x01",
            "in there, like Dr. Miriam said.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #2
        0x101,
        "#003F(I guess that's our only option.)\x02",
    )

    CloseMessageWindow()

    label("loc_22D")

    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)
    Jump("loc_7E1")

    label("loc_238")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DD")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(-10040, 0, -1620, 0)
    SetChrPos(0x101, -8960, 0, -1680, 228)
    SetChrPos(0x102, -8920, 0, -530, 225)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29F")
    SetChrPos(0x107, -7480, 0, -1290, 224)

    label("loc_29F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BE")
    SetChrPos(0x106, -7720, 0, -160, 225)

    label("loc_2BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DD")
    SetChrPos(0x13C, -8770, 0, -2870, 290)

    label("loc_2DD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F7")

    def lambda_2EF():
        TurnDirection(0x0, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2EF)

    label("loc_2F7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_311")

    def lambda_309():
        TurnDirection(0x1, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_309)

    label("loc_311")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32B")

    def lambda_323():
        TurnDirection(0x2, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_323)

    label("loc_32B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_345")

    def lambda_33D():
        TurnDirection(0x3, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_33D)

    label("loc_345")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35F")

    def lambda_357():
        TurnDirection(0x4, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_357)

    label("loc_35F")

    OP_0D()
    Sleep(400)
    OP_4A(0xA, 255)
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x0, 400)
    Sleep(800)

    ChrTalk(    #3
        0xA,
        "What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xA,
        (
            "Sorry, but I'm in the middle\x01",
            "of something important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xA,
        (
            "Come back later if you\x01",
            "need me.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 0, 400)
    OP_4B(0xA, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_717")
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #6
        0x101,
        (
            "#003F(Hmm... I don't get the\x01",
            "feeling that he particularly\x01",
            "wants to be questioned.)\x02\x03",

            "#004F(Oh, yeah...\x01",
            "Any reaction out of Antoine?)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4BB():
        TurnDirection(0x102, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4BB)

    def lambda_4C9():
        TurnDirection(0x107, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_4C9)
    TurnDirection(0x101, 0x13C, 400)

    ChrTalk(    #7
        0x13C,
        "...\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    TurnDirection(0x13C, 0x101, 400)

    ChrTalk(    #8
        0x13C,
        "...Nyao?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x107,
        "#063F(Nothing...)\x02",
    )

    CloseMessageWindow()
    OP_28(0x2C, 0x1, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_70D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_601")

    ChrTalk(    #10
        0x101,
        (
            "#505FHmmm... He didn't respond\x01",
            "to either of them.\x02\x03",

            "I guess we'll have to go back\x01",
            "to where he was reacting and\x01",
            "look around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x102,
        (
            "#010FThat'd be the factory chief's\x01",
            "office upstairs.\x02\x03",

            "Let's get over there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70D")

    label("loc_601")

    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #12
        0x101,
        (
            "#004F(Hmm... I guess neither\x01",
            "of them is the culprit.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x102,
        (
            "#013F(No clues to be found...)\x02\x03",

            "#010F(As it stands, we should keep\x01",
            "on looking.)\x02\x03",

            "#010F(There may be a hint somewhere\x01",
            "in there, like Dr. Miriam said.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#003F(Hmm... I guess you're right.)\x02",
    )

    CloseMessageWindow()
    OP_28(0x2C, 0x1, 0x80)

    label("loc_70D")

    Sleep(50)
    EventEnd(0x4)
    Jump("loc_7E1")

    label("loc_717")

    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)
    TurnDirection(0x101, 0x102, 400)
    Sleep(400)

    ChrTalk(    #15
        0x101,
        (
            "#003F(I-I guess there's nothing\x01",
            "we can do right now.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #16
        0x102,
        (
            "#017F(They seem to be in a meeting.)\x02\x03",

            "(Now's not the best time to\x01",
            "bother them.)\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x2C, 0x1, 0x8)
    ClearMapFlags(0x80)

    label("loc_7E1")

    Return()

    # Function_0_66 end

    def Function_1_7E2(): pass

    label("Function_1_7E2")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -115940, -4000, -111340, 180)
    SetChrPos(0x102, -116620, -4000, -110300, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_82A")
    SetChrPos(0x107, -115430, -4000, -109960, 180)

    label("loc_82A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_849")
    SetChrPos(0x106, -116050, -4000, -109140, 180)

    label("loc_849")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_868")
    SetChrPos(0x108, -116050, -4000, -109140, 180)

    label("loc_868")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_887")
    SetChrPos(0x110, -116740, -4000, -108860, 180)

    label("loc_887")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A6")
    SetChrPos(0x13C, -116740, -4000, -108860, 180)

    label("loc_8A6")

    OP_6D(-116920, -4000, -112310, 2000)
    OP_0D()

    ChrTalk(    #17
        0x101,
        "#000FFaye? Do you have a minute?\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xE, 0x10)
    TalkBegin(0xE)
    OP_4A(0xE, 255)
    ClearChrFlags(0xE, 0x10)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #18
        0xFE,
        "#4PHm? What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#000FI've got a letter for you.\x02\x03",

            "Here you go.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #20
        "\x07\x00Handed over \x07\x02Letter to Faye\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_3F(0x35E, 1)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #21
        0xFE,
        "#4PWhat...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "#4PWait... Is this from Private Brahm\x01",
            "at the Wolf Fort?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#000FYeah...\x02\x03",

            "#002F(Okay! Now's the perfect time\x01",
            "to give her the gift!)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x14D)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_40(0x1B2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x14A)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AEC")
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #24
        0x101,
        (
            "#008F(...Or it would be, if I hadn't\x01",
            "forgotten to buy it!)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    Jump("loc_F2C")

    label("loc_AEC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x14D)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x1B2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x14A)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B77")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Work Gloves]\x01",      # 0
            "[Cancel]\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B68"),
        (1, "loc_B6E"),
        (SWITCH_DEFAULT, "loc_B74"),
    )


    label("loc_B68")

    OP_A2(0xB)
    Jump("loc_B74")

    label("loc_B6E")

    OP_A2(0xE)
    Jump("loc_B74")

    label("loc_B74")

    Jump("loc_F2C")

    label("loc_B77")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x14D)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_40(0x1B2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x14A)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C04")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Seasonal Tart]\x01",      # 0
            "[Cancel]\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_BF5"),
        (1, "loc_BFB"),
        (SWITCH_DEFAULT, "loc_C01"),
    )


    label("loc_BF5")

    OP_A2(0xC)
    Jump("loc_C01")

    label("loc_BFB")

    OP_A2(0xE)
    Jump("loc_C01")

    label("loc_C01")

    Jump("loc_F2C")

    label("loc_C04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x14D)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_40(0x1B2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x14A)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C93")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Woolly Knit-Hat]\x01",      # 0
            "[Cancel]\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C84"),
        (1, "loc_C8A"),
        (SWITCH_DEFAULT, "loc_C90"),
    )


    label("loc_C84")

    OP_A2(0xD)
    Jump("loc_C90")

    label("loc_C8A")

    OP_A2(0xE)
    Jump("loc_C90")

    label("loc_C90")

    Jump("loc_F2C")

    label("loc_C93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x14D)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x1B2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x14A)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D37")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Work Gloves]\x01",        # 0
            "[Seasonal Tart]\x01",      # 1
            "[Cancel]\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D22"),
        (1, "loc_D28"),
        (2, "loc_D2E"),
        (SWITCH_DEFAULT, "loc_D34"),
    )


    label("loc_D22")

    OP_A2(0xB)
    Jump("loc_D34")

    label("loc_D28")

    OP_A2(0xC)
    Jump("loc_D34")

    label("loc_D2E")

    OP_A2(0xE)
    Jump("loc_D34")

    label("loc_D34")

    Jump("loc_F2C")

    label("loc_D37")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x14D)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x1B2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x14A)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DDD")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Work Gloves]\x01",          # 0
            "[Woolly Knit-Hat]\x01",      # 1
            "[Cancel]\x01",               # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_DC8"),
        (1, "loc_DCE"),
        (2, "loc_DD4"),
        (SWITCH_DEFAULT, "loc_DDA"),
    )


    label("loc_DC8")

    OP_A2(0xB)
    Jump("loc_DDA")

    label("loc_DCE")

    OP_A2(0xD)
    Jump("loc_DDA")

    label("loc_DD4")

    OP_A2(0xE)
    Jump("loc_DDA")

    label("loc_DDA")

    Jump("loc_F2C")

    label("loc_DDD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x14D)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_40(0x1B2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x14A)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E85")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Seasonal Tart]\x01",        # 0
            "[Woolly Knit-Hat]\x01",      # 1
            "[Cancel]\x01",               # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E70"),
        (1, "loc_E76"),
        (2, "loc_E7C"),
        (SWITCH_DEFAULT, "loc_E82"),
    )


    label("loc_E70")

    OP_A2(0xC)
    Jump("loc_E82")

    label("loc_E76")

    OP_A2(0xD)
    Jump("loc_E82")

    label("loc_E7C")

    OP_A2(0xE)
    Jump("loc_E82")

    label("loc_E82")

    Jump("loc_F2C")

    label("loc_E85")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Work Gloves]\x01",          # 0
            "[Seasonal Tart]\x01",        # 1
            "[Woolly Knit-Hat]\x01",      # 2
            "[Cancel]\x01",               # 3
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F17"),
        (1, "loc_F1A"),
        (2, "loc_F20"),
        (3, "loc_F26"),
        (SWITCH_DEFAULT, "loc_F2C"),
    )


    label("loc_F17")

    OP_A2(0xB)

    label("loc_F1A")

    OP_A2(0xC)
    Jump("loc_F2C")

    label("loc_F20")

    OP_A2(0xD)
    Jump("loc_F2C")

    label("loc_F26")

    OP_A2(0xE)
    Jump("loc_F2C")

    label("loc_F2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_11B1")

    ChrTalk(    #25
        0x101,
        (
            "#000FAnd this is a present to\x01",
            "go with it.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #26
        "\x07\x00Handed over \x07\x02Work Gloves\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_62(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #27
        0xFE,
        (
            "#4PWork gloves? What kind of\x01",
            "gift are these meant to be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "#4PW-Well... I'll accept them...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 270, 200)

    ChrTalk(    #29
        0xFE,
        (
            "#4P*sigh* I just don't think he\x01",
            "really gets me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "#4P...\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #31
        0x101,
        (
            "#509F(Ack...)\x02\x03",

            "(Well, that was a lousy present...)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_8C(0xFE, 0, 400)

    ChrTalk(    #32
        0xFE,
        "#4P...Oh, I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "#4PThank you for taking the\x01",
            "time to deliver it to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "#4PWell...\x01",
            "I should get back to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#506FS-Sure.\x01",
            "See you later.\x02",
        )
    )

    CloseMessageWindow()
    OP_3F(0x14D, 1)
    OP_28(0x31, 0x1, 0x40)
    OP_2B(0x31, 0x2)
    Jump("loc_1890")

    label("loc_11B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_1471")

    ChrTalk(    #36
        0x101,
        "#000FAnd this is a present to go with it.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #37
        "\x07\x00Handed over \x07\x02Seasonal Tart\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_62(0xFE, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #38
        0xFE,
        (
            "#4PTh-Thank you...\x01",
            "It's very nice...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "#4PIt's just that I'm trying to\x01",
            "cut back on sweets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "#4PAnd he still sent me this...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 270, 200)

    ChrTalk(    #41
        0xFE,
        (
            "#4P*sigh* I guess it just shows that\x01",
            "he doesn't really listen to me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "#4P...\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #43
        0x101,
        (
            "#509F(Ack...)\x02\x03",

            "(Well, that was a lousy present...)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_8C(0xFE, 0, 400)

    ChrTalk(    #44
        0xFE,
        "#4P...Oh, I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "#4PThank you for taking the\x01",
            "time to deliver it to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "#4PWell...\x01",
            "I should get back to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#506FS-Sure.\x01",
            "See you later.\x02",
        )
    )

    CloseMessageWindow()
    OP_3F(0x1B2, 1)
    OP_28(0x31, 0x1, 0x80)
    OP_2B(0x31, 0x2)
    Jump("loc_1890")

    label("loc_1471")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_166B")

    ChrTalk(    #48
        0x101,
        "#000FAnd this is a present to go with it.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #49
        "\x07\x00Handed over \x07\x02Woolly Knit-Hat\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    ChrTalk(    #50
        0xFE,
        "#4POh, how cute.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        "#4PI see, now. Finally...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "#4PI know he still thinks\x01",
            "about me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "#4PBut I just wish he'd come\x01",
            "sooner...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        "#4P...\x02",
    )

    CloseMessageWindow()
    Sleep(800)

    ChrTalk(    #55
        0xFE,
        "#4P...Oh, I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "#4PThank you for taking the\x01",
            "time to deliver it to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "#4PWell...\x01",
            "I should get back to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        "#000FSure. See you later.\x02",
    )

    CloseMessageWindow()
    OP_3F(0x14A, 1)
    OP_28(0x31, 0x1, 0x20)
    OP_2B(0x31, 0x4)
    Jump("loc_1890")

    label("loc_166B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_16AC")

    ChrTalk(    #59
        0x101,
        (
            "#505F(Hmm... Not bad, but it \x01",
            "wasn't quite perfect.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16AC")

    Sleep(400)

    ChrTalk(    #60
        0xFE,
        "#4PHmmm...okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "#4PHe's trying, in his own special\x01",
            "way, to show me that he still\x01",
            "thinks about me.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 270, 200)

    ChrTalk(    #62
        0xFE,
        (
            "#4PBut he sends me a letter\x01",
            "now, of all things...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "#4P...\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #64
        0x101,
        (
            "#509F(Ack...)\x02\x03",

            "(Maybe I should have given\x01",
            "her a present... )\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_8C(0xFE, 0, 400)

    ChrTalk(    #65
        0xFE,
        "#4P...Oh, I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "#4PThank you for taking the\x01",
            "time to deliver it to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "#4PWell...\x01",
            "I should get back to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        (
            "#506FS-Sure.\x01",
            "See you later.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x31, 0x1, 0x100)

    label("loc_1890")

    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #69
        "\x07\x00Quest \x07\x02[Messenger of Love] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x31, 0x4, 0x10)
    OP_28(0x31, 0x1, 0x10)
    OP_A2(0xA)
    EventEnd(0x0)
    OP_4B(0xE, 255)
    Return()

    # Function_1_7E2 end

    SaveToFile()

Try(main)
