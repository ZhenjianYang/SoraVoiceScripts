from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T3132_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T3132_1 ._SN',
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
        "Function_1_388",          # 01, 1
        "Function_2_60C",          # 02, 2
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x8, -1700, 0, 2400, 192)
    SetChrPos(0x101, -2340, 0, 450, 0)
    SetChrPos(0xF7, -1190, 0, 350, 0)
    SetChrPos(0xF8, -2290, 0, -670, 0)
    SetChrPos(0xF9, -1120, 0, -670, 0)
    OP_6D(-2000, 0, 50, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #0
        0x8,
        "Welcome to the Zahnrad Hotel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        "Do you have a reservation?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#1011FSorry, that's not why we're here.\x02\x03",

            "We came from the guild.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #3
        0x8,
        "Oh, are you bracers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        "Pardon me. We've been waiting for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        "Can you begin the search immediately?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C3")

    ChrTalk(    #6
        0x101,
        "#1006FYeah, no problem.\x02",
    )

    CloseMessageWindow()
    Call(1, 2)
    Jump("loc_387")

    label("loc_2C3")


    ChrTalk(    #7
        0x101,
        (
            "#1007FAh, sorry.\x02\x03",

            "We're a bit busy, so we can't do it\x01",
            "right this second.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        "Oh, I see. That is a problem...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "Well, when you have finished your\x01",
            "business, come back immediately.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x71, 0x1, 0x8000)
    EventEnd(0x0)
    Return()

    label("loc_387")

    Return()

    # Function_0_AA end

    def Function_1_388(): pass

    label("Function_1_388")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x8, -1700, 0, 2400, 192)
    SetChrPos(0x101, -2340, 0, 450, 0)
    SetChrPos(0xF7, -1190, 0, 350, 0)
    SetChrPos(0xF8, -2290, 0, -670, 0)
    SetChrPos(0xF9, -1120, 0, -670, 0)
    OP_6D(-2000, 0, 50, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #10
        0x8,
        (
            "Hello again. I've been eagerly\x01",
            "awaiting your return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        "My request is quite urgent.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        "Have you finished your other business?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53B")

    ChrTalk(    #13
        0x101,
        (
            "#1006FSorry to keep you waiting.\x01",
            "We're all ready to go now.\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 2)
    Jump("loc_60B")

    label("loc_53B")


    ChrTalk(    #14
        0x101,
        "#1007FS-Sorry... Actually, we're still a bit tied up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        "*sigh* I see that you are quite busy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "I suppose I don't have a choice,\x01",
            "but please come as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        "#1006FYeah, will do.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    label("loc_60B")

    Return()

    # Function_1_388 end

    def Function_2_60C(): pass

    label("Function_2_60C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_619")
    OP_A2(0x4)

    label("loc_619")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_696")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as met Jimmy in previous game\x01",      # 0
            "No change\x01",                              # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_690"),
        (SWITCH_DEFAULT, "loc_696"),
    )


    label("loc_690")

    OP_A2(0x4)
    Jump("loc_696")

    label("loc_696")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F3")

    ChrTalk(    #18
        0x108,
        (
            "#070FAccording to the request, a customer\x01",
            "hasn't been back in a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_79E")

    label("loc_6F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_74D")

    ChrTalk(    #19
        0x104,
        (
            "#030FThe request mentioned a customer\x01",
            "hasn't returned in some time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_79E")

    label("loc_74D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_79E")

    ChrTalk(    #20
        0x105,
        (
            "#040FWe saw the request. You say a\x01",
            "customer hasn't come back?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_79E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7D9")

    ChrTalk(    #21
        0x106,
        "#050F#6PSo in other words, they're missing?\x02",
    )

    CloseMessageWindow()
    Jump("loc_80A")

    label("loc_7D9")


    ChrTalk(    #22
        0x103,
        "#022F#6PSo in other words, they're missing?\x02",
    )

    CloseMessageWindow()

    label("loc_80A")


    ChrTalk(    #23
        0x8,
        "Yes, that's exactly the case.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        "He's been gone for three days.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1002FThree days, huh? That is kinda\x01",
            "worrisome.\x02\x03",

            "Lately, the monsters on the roads\x01",
            "have been pretty nasty, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        "I almost wish that was where he had gone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "This particular guest... He...\x01",
            "He's gone to the Limestone Cave.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #28
        0x101,
        (
            "#1004FThe Limestone Cave?!\x02\x03",

            "The one that's, like, in the middle\x01",
            "of the Kaldia Tunnel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        "Yes, exactly. The Kaldia Limestone Cave.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        "We tried to stop him, but...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A77")

    ChrTalk(    #31
        0x108,
        (
            "#072FYeah... That's pretty bad.\x02\x03",

            "That's not the kind of place your\x01",
            "average citizen should go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B36")

    label("loc_A77")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AD6")

    ChrTalk(    #32
        0x106,
        (
            "#057F#6PWhoa, whoa, you're kiddin', right?\x02\x03",

            "That place is a monster pit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B36")

    label("loc_AD6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B36")

    ChrTalk(    #33
        0x103,
        (
            "#022F#6PThat's bad...\x02\x03",

            "The Kaldia Tunnel is infamous for\x01",
            "ferocious monsters.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B36")


    ChrTalk(    #34
        0x101,
        (
            "#1003FI can't believe this. Why go there\x01",
            "without an escort?\x02\x03",

            "#1002FWho was this crazy guest?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "He seemed to be a fairly ordinary\x01",
            "young man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        "He checked in as 'Jimmy' from Ruan.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_E60")
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #37
        0x101,
        (
            "#1004FJ-Jimmy from Ruan?\x02\x03",

            "#1019FC-Could it be...?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C53():
        TurnDirection(0xF7, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_C53)
    Sleep(50)

    def lambda_C66():
        TurnDirection(0xF8, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_C66)
    Sleep(100)
    TurnDirection(0xF9, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_C9C")

    ChrTalk(    #38
        0x106,
        "#052FYou know him?\x02",
    )

    CloseMessageWindow()
    Jump("loc_CB7")

    label("loc_C9C")


    ChrTalk(    #39
        0x103,
        "#023FDo you know him?\x02",
    )

    CloseMessageWindow()

    label("loc_CB7")

    TurnDirection(0x101, 0xF7, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D9A")

    ChrTalk(    #40
        0x101,
        (
            "#1002FYeah, I've done a job for someone with\x01",
            "that name before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x105,
        (
            "#043FAs I recall, it was a treasure hunt\x01",
            "of some kind.\x02\x03",

            "Most likely, he went to the Limestone\x01",
            "Cave searching for something again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E5D")

    label("loc_D9A")


    ChrTalk(    #42
        0x101,
        (
            "#1002FYeah, I've done a job before for someone\x01",
            "with that name.\x02\x03",

            "#1015FI think it was a search for treasure?\x02\x03",

            "I wonder if he went to the Limestone\x01",
            "Cave looking for something like that\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E5D")

    Jump("loc_E93")

    label("loc_E60")


    ChrTalk(    #43
        0x101,
        (
            "#1015FJimmy from Ruan?\x02\x03",

            "Sounds normal enough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F28")

    ChrTalk(    #44
        0x104,
        (
            "#032FWe'd best away to the Limestone Cave\x01",
            "immediately.\x02\x03",

            "If fortune doesn't favor this young man,\x01",
            "we might already be too late.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1039")

    label("loc_F28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FBF")

    ChrTalk(    #45
        0x107,
        (
            "#062FAnyway, we'd better hurry to the\x01",
            "Limestone Cave.\x02\x03",

            "There have been some really strong\x01",
            "monsters lately, so this could be bad.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1039")

    label("loc_FBF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1039")

    ChrTalk(    #46
        0x108,
        (
            "#072FWe'd best go to the Limestone Cave\x01",
            "immediately.\x02\x03",

            "In the worst case, we might already\x01",
            "be too late.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1039")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_10E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_109D")

    ChrTalk(    #47
        0x106,
        "#053FYeah, we should hurry.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x8, 400)

    ChrTalk(    #48
        0x106,
        "#050F#6P...Got any other information?\x02",
    )

    CloseMessageWindow()
    Jump("loc_10E5")

    label("loc_109D")


    ChrTalk(    #49
        0x106,
        (
            "#053F#6PYeah, we should hurry.\x02\x03",

            "#050F...Got any other information?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10E5")

    Jump("loc_1196")

    label("loc_10E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_114C")

    ChrTalk(    #50
        0x103,
        "#022FYes, we should hurry.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x8, 400)

    ChrTalk(    #51
        0x103,
        "#022F#6P...Do you have any other information?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1196")

    label("loc_114C")


    ChrTalk(    #52
        0x103,
        (
            "#022F#6PYes, we should hurry.\x02\x03",

            "...Do you have any other information?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1196")


    def lambda_119C():
        OP_8C(0x101, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_119C)
    Sleep(50)

    def lambda_11AF():
        OP_8C(0xF8, 0, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_11AF)
    Sleep(100)
    OP_8C(0xF9, 0, 400)
    WaitChrThread(0xF8, 0x1)

    ChrTalk(    #53
        0x8,
        "I've told you everything I can.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        "Please, take care of our guest.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        "#1002FWe're on it.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_124D")

    ChrTalk(    #56
        0x106,
        "#050F#6PLet's move.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1264")

    label("loc_124D")


    ChrTalk(    #57
        0x103,
        "#022F#6PLet's go.\x02",
    )

    CloseMessageWindow()

    label("loc_1264")

    OP_28(0x71, 0x4, 0x4)
    OP_28(0x71, 0x4, 0x8)
    OP_28(0x71, 0x1, 0x1)
    OP_28(0x71, 0x1, 0x2)
    EventEnd(0x0)
    Return()

    # Function_2_60C end

    SaveToFile()

Try(main)
