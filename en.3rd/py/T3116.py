from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3116   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3116.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Professor Russell',                    # 9
        'Erika',                                # 10
        'Karl',                                 # 11
        'Target Camera',                        # 12
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
        'ED6_DT07/CH01190 ._CH',             # 00
        'ED6_DT07/CH02020 ._CH',             # 01
        'ED6_DT07/CH00060 ._CH',             # 02
        'ED6_DT27/CH03970 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01190P._CP',             # 00
        'ED6_DT07/CH02020P._CP',             # 01
        'ED6_DT07/CH00060P._CP',             # 02
        'ED6_DT27/CH03970P._CP',             # 03
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2000,
        Z                   = 0,
        Y                   = 3410,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
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
        "Function_0_14A",          # 00, 0
        "Function_1_17B",          # 01, 1
        "Function_2_17C",          # 02, 2
        "Function_3_357",          # 03, 3
        "Function_4_18E5",         # 04, 4
    )


    def Function_0_14A(): pass

    label("Function_0_14A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15B")
    ClearChrFlags(0x12, 0x80)

    label("loc_15B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_17A")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_17A")

    Return()

    # Function_0_14A end

    def Function_1_17B(): pass

    label("Function_1_17B")

    Return()

    # Function_1_17B end

    def Function_2_17C(): pass

    label("Function_2_17C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_353")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_24B")
    OP_8C(0xFE, 270, 0)

    ChrTalk(    #0
        0xFE,
        "Hmm... To cut, or not to cut...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "One thing's for sure: if we don't work out a way\x01",
            "to cut production costs at least a teeeeeny tiny\x01",
            "bit, we won't stack up to the Empire...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_353")

    label("loc_24B")


    ChrTalk(    #2
        0xFE,
        "You're looking for Erika Russell?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "I haven't seen her today. Sorry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "If I haven't, though, it makes me wonder\x01",
            "whether she's finished that project she was\x01",
            "plowing through...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "She's been hogging all the equipment to herself\x01",
            "to work on it lately.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_353")

    TalkEnd(0xFE)
    Return()

    # Function_2_17C end

    def Function_3_357(): pass

    label("Function_3_357")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(1280, 0, 12800, 0)
    OP_67(0, 5000, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, -30, 0, 12840, 180)
    SetChrPos(0x11, -360, 0, 10320, 0)
    SetChrFlags(0x107, 0x4)
    SetChrPos(0x107, -2800, 0, 3260, 0)
    OP_22(0xE0, 0x1, 0x64)
    OP_71(0x2001, 0x0)
    ExitThread()
    OP_71(0x2002, 0x0)
    ExitThread()
    OP_70(0x1, 0x3)
    OP_70(0x2, 0x3)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #6
        0x10,
        (
            "#101F#5PThis tool here's brand new. It can cut with ten\x01",
            "times more precision than the previous model!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x11,
        (
            "#1457F#12PBah... I had no idea you had something like this\x01",
            "here now.\x02\x03",

            "#1456FI think I might have to go over the designs again!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x6D, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #8
        0x107,
        (
            "#560F#1POh, Mom!\x02\x03",

            "Here you are.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    ClearChrFlags(0x107, 0x4)
    SetChrPos(0x107, -360, 0, 3120, 0)

    def lambda_550():
        OP_8E(0xFE, 0xFFFFFE98, 0x0, 0x2256, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_550)
    Sleep(100)
    OP_22(0x6D, 0x0, 0x64)
    WaitChrThread(0x107, 0x1)
    Sleep(300)

    ChrTalk(    #9
        0x11,
        (
            "#1450F#5PWelcome back, Tita.\x02\x03",

            "Did you manage to do what I asked?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x107,
        (
            "#061F#12PYup. Mr. Murdock said he'll take care of\x01",
            "the paperwork right away.\x02\x03",

            "He's probably working on it right now.\x02\x03",

            "#560FBut now that I've done that, Mom...\x02\x03",

            "...I want to be part of the Orbal Gear's\x01",
            "development team, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x11, 180, 500)
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_72(0x2002, 0x0)
    ExitThread()
    OP_23(0xE0)
    OP_22(0x9A, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #11
        0x11,
        "#1454F#5P...You?\x02",
    )

    CloseMessageWindow()
    OP_43(0x10, 0x3, 0x0, 0x4)

    ChrTalk(    #12
        0x107,
        (
            "#063F#12PYeah. I didn't write this in any of my letters...\x02\x03",

            "...but I ended up spending some time with\x01",
            "Renne while she was in Liberl.\x02\x03",

            "#062FAnd even if she's a member of the society,\x01",
            "she's also my friend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x11,
        (
            "#1452F#5PRenne...?\x02\x01",

            "#1457FNow, where have I heard that before...?\x02\x03",

            "#1453FOh! Wasn't she the girl Pater-Mater belongs to?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x10, 0x3)

    ChrTalk(    #14
        0x10,
        (
            "#100F#5PUmm... Erika... If I might be permitted to say\x01",
            "my piece here...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x10, 500)
    Sleep(300)

    ChrTalk(    #15
        0x11,
        "#1830F#11PSay your piece?!\x02",
    )

    CloseMessageWindow()

    def lambda_8CF():
        OP_6D(-1660, -120, 12880, 1500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_8CF)

    def lambda_8E7():
        OP_67(0, 4320, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_8E7)

    def lambda_8FF():
        OP_6C(36000, 1500)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_8FF)

    def lambda_90F():

        label("loc_90F")

        TurnDirection(0xFE, 0x11, 500)
        OP_48()
        Jump("loc_90F")

    QueueWorkItem2(0x107, 2, lambda_90F)

    def lambda_920():
        OP_8E(0xFE, 0xFFFFF3BC, 0x0, 0x2878, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_920)
    WaitChrThread(0x11, 0x1)

    def lambda_940():
        OP_8E(0xFE, 0xFFFFF3BC, 0x0, 0x2DF0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_940)
    WaitChrThread(0x11, 0x1)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    OP_22(0x8F, 0x0, 0x64)
    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x10, 0x4)

    def lambda_992():
        OP_9E(0xFE, 0xF, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_992)

    def lambda_9AC():
        OP_95(0xFE, 0x0, 0x12C, 0x0, 0x12C, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_9AC)
    WaitChrThread(0x10, 0x1)
    Sleep(500)
    OP_44(0x107, 0x2)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_9EA():
        OP_8E(0xFE, 0xFFFFF358, 0x0, 0x2580, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_9EA)
    WaitChrThread(0x107, 0x1)

    def lambda_A0A():
        OP_8E(0xFE, 0xFFFFF358, 0x0, 0x26AC, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_A0A)
    WaitChrThread(0x107, 0x1)
    Sleep(300)

    ChrTalk(    #16
        0x107,
        "#065FM-Mom?! What are you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x11,
        (
            "#1457F#6PYou better have a DAMN GOOD explanation\x01",
            "for this one, Albert.\x02\x03",

            "My daughter ended up making friends with a\x01",
            "member of OUROBOROS?!\x02\x03",

            "#1459FWhy is this the first I'm hearing of this? This\x01",
            "wasn't in any of what you sent me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10,
        (
            "#104F#5PWell...\x02\x03",

            "...it was kind of hard to say...\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x10, 0x20)

    def lambda_B76():
        OP_8E(0xFE, 0xFFFFF3BC, 0x0, 0x3110, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_B76)

    def lambda_B91():
        OP_8F(0xFE, 0xFFFFF380, 0x12C, 0x3318, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_B91)
    WaitChrThread(0x11, 0x1)
    Sleep(300)
    ClearChrFlags(0x10, 0x20)

    ChrTalk(    #19
        0x11,
        (
            "#1459F#6PDon't you give me that!\x02\x03",

            "As if you hadn't already exposed her to enough\x01",
            "danger to make me want to strangle you, and\x01",
            "now I'm hearing THIS?!\x02\x03",

            "#1830F#3SJust what have you been doing with my\x01",
            "daughter while I've been away?!#2S\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x107,
        (
            "#062FM-Mom! I'm serious! I want to be involved in the\x01",
            "Orbal Gear's development!\x02\x03",

            "I'm completely powerless on my own, but I still\x01",
            "want to find some way to talk to her.\x02\x03",

            "And the Orbal Gear's going to be able to fight\x01",
            "on equal terms with Pater-Mater, right?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #21
        0x107,
        (
            "#068FTh-Then I want to be involved! Because I want\x01",
            "the kind of power that Estelle has!\x02",
        )
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_20(0xBB8)
    OP_44(0x10, 0x2)
    Sleep(500)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #22
        0x11,
        "#1453F#5P...Tita?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x4)

    def lambda_E66():
        OP_96(0xFE, 0xFFFFF31C, 0x0, 0x337C, 0xA, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_E66)
    WaitChrThread(0x10, 0x1)
    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x8E, 0x0, 0x32)
    OP_22(0xD1, 0x0, 0x64)
    Sleep(300)
    TurnDirection(0x11, 0x107, 500)
    Sleep(300)

    def lambda_EB5():
        OP_8E(0xFE, 0xFFFFF3BC, 0x0, 0x2F1C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_EB5)
    WaitChrThread(0x11, 0x1)

    ChrTalk(    #23
        0x11,
        (
            "#1452F#5PCorrect me if I'm wrong, but...\x02\x03",

            "...you're not considering using the Orbal Gear\x01",
            "to fight Pater-Mater yourself, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x107,
        (
            "#564F#12PWhat...?\x02\x03",

            "Th-That wasn't what I meant... I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x11,
        (
            "#1457F#5PI want to make very sure of this.\x02\x03",

            "Do you understand just what we're making here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x107,
        (
            "#064F#12PUmm... Well...\x02\x03",

            "#560FWell, I only got a quick look at the blueprints,\x01",
            "but it looked like a bipedal...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x11,
        (
            "#1453F#5PThat's not what I mean.\x02\x03",

            "The Orbal Gear is a weapon. No matter how you\x01",
            "try to dress that fact up, that's the reality.\x02\x03",

            "#1452FIt's a tool designed to be used by people to hurt\x01",
            "other people. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x107,
        (
            "#063F#12PB-But...\x02\x03",

            "But you're not making it because you want to hurt\x01",
            "people, are you?\x02\x03",

            "Even the patrol airships used by the army are made\x01",
            "to protect the country, not to hurt people...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x11,
        (
            "#1457F#5PIt doesn't matter what I think. It doesn't matter\x01",
            "what the developer of any new weapon thinks.\x02\x03",

            "We're not the ones actually going out and using\x01",
            "the things we make.\x02\x03",

            "#1453FThe devices we pour our hearts into making go\x01",
            "on to cause unspeakable suffering to people,\x01",
            "and there's nothing we can do to stop it.\x02\x03",

            "#1452FHave you ever stopped to think about that?\x02\x03",

            "And after having it pointed out to you, can you\x01",
            "still say you want power?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x107,
        "#065F#12PWell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x11,
        (
            "#1453F#5PWe're doing what we're doing fully aware of what\x01",
            "the potential consequences may be down the line,\x01",
            "but can you?\x02\x03",

            "#1457FYou know how much I love you, Tita.\x02\x03",

            "And I understand that you care deeply about\x01",
            "your friend. I do.\x02\x03",

            "But that's all the more reason why I can't\x01",
            "permit you to take part in this.\x02\x03",

            "#1452FCan you understand where I'm coming from?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x107,
        (
            "#065F#12P#40W...\x02\x03",

            "#562FB-But...I...I...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #33
        0x107,
        (
            "#069F#12P#3SI'm not taking this lightly, either,\x01",
            "you know!\x02",
        )
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x96)
    CloseMessageWindow()
    OP_8C(0x107, 90, 600)

    def lambda_15B5():
        OP_8E(0xFE, 0xFFFFFAEC, 0x0, 0x2580, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_15B5)
    WaitChrThread(0x107, 0x1)

    def lambda_15D5():
        OP_8E(0xFE, 0xFFFFFAEC, 0x0, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_15D5)
    WaitChrThread(0x107, 0x1)
    OP_22(0x6D, 0x0, 0x64)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_22(0x6D, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #34
        0x10,
        (
            "#104F#5PI appreciate how you feel, Erika, but I'm sure\x01",
            "Tita's been thinking about this a lot herself,\x01",
            "especially after all she went through.\x02\x03",

            "#102FWhy not show her a little more respect?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x11,
        (
            "#1457F#6PI'm sure she has, but that doesn't mean I can\x01",
            "let her be involved in developing a weapon.\x02\x03",

            "We researchers don't get a say in how our\x01",
            "inventions end up being used down the line.\x01",
            "That's just our fate.\x02\x03",

            "#1453FThat's what we have to accept when we're\x01",
            "doing our jobs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10,
        "#104F#5P...That we do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x11,
        (
            "#1452F#6PI know where she's coming from, but I absolutely\x01",
            "can't let her be a part of this.\x02\x03",

            "#1457FShe doesn't need to be shouldering this kind of\x01",
            "burden. Not at her age.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_18C3():
        OP_6B(2960, 3000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_18C3)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3112   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_357 end

    def Function_4_18E5(): pass

    label("Function_4_18E5")


    def lambda_18EB():
        OP_8E(0xFE, 0xFFFFFFE2, 0x0, 0x3700, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_18EB)
    WaitChrThread(0x10, 0x1)

    def lambda_190B():
        OP_8E(0xFE, 0xFFFFF768, 0x0, 0x3700, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_190B)
    WaitChrThread(0x10, 0x1)

    def lambda_192B():
        OP_8E(0xFE, 0xFFFFF380, 0x0, 0x3318, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_192B)
    WaitChrThread(0x10, 0x1)

    def lambda_194B():
        OP_8E(0xFE, 0xFFFFF380, 0x0, 0x2FF8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_194B)
    WaitChrThread(0x10, 0x1)

    def lambda_196B():

        label("loc_196B")

        TurnDirection(0xFE, 0x11, 500)
        OP_48()
        Jump("loc_196B")

    QueueWorkItem2(0x10, 2, lambda_196B)
    Return()

    # Function_4_18E5 end

    SaveToFile()

Try(main)
